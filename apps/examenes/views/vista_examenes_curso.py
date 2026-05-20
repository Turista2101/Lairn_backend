from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiResponse
from core.permissions.permisos_rol import EsEstudiante
from apps.examenes.models import Curso, Examen, Inscripcion
from apps.examenes.serializers import SerializadorExamen


@extend_schema(
    tags=['Exámenes'],
    summary='Exámenes de un curso (estudiante)',
    description=(
        'Retorna todos los exámenes disponibles en un curso. '
        'El estudiante debe estar inscrito en el curso para poder verlos.'
    ),
    responses={
        200: SerializadorExamen(many=True),
        403: OpenApiResponse(description='No estás inscrito en este curso o no eres estudiante'),
        404: OpenApiResponse(description='Curso no encontrado'),
    },
)
class VistaExamenesCurso(APIView):
    permission_classes = [EsEstudiante]

    def get(self, request, curso_id):
        try:
            curso = Curso.objects.get(id=curso_id)
        except Curso.DoesNotExist:
            return Response({'detalle': 'Curso no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        if not Inscripcion.objects.filter(estudiante=request.user, curso=curso).exists():
            return Response(
                {'detalle': 'No estás inscrito en este curso.'},
                status=status.HTTP_403_FORBIDDEN,
            )

        examenes = Examen.objects.filter(curso=curso)
        serializador = SerializadorExamen(examenes, many=True)
        return Response(serializador.data)
