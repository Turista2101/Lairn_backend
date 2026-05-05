from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiResponse
from core.permissions.permisos_rol import EsDocente
from apps.examenes.models import Curso
from apps.examenes.serializers import SerializadorCrearCurso


@extend_schema_view(
    get=extend_schema(
        tags=['Cursos'],
        summary='Listar mis cursos',
        description='Retorna todos los cursos creados por el docente autenticado.',
        responses={
            200: SerializadorCrearCurso(many=True),
            403: OpenApiResponse(description='Solo los docentes pueden acceder'),
        },
    ),
    post=extend_schema(
        tags=['Cursos'],
        summary='Crear curso',
        description='Crea un nuevo curso. El sistema genera automáticamente un código único de 8 caracteres que el docente puede compartir con sus estudiantes.',
        request=SerializadorCrearCurso,
        responses={
            201: SerializadorCrearCurso,
            400: OpenApiResponse(description='Datos inválidos'),
            403: OpenApiResponse(description='Solo los docentes pueden crear cursos'),
        },
    ),
)
class VistaCrearCurso(APIView):
    permission_classes = [EsDocente]

    def post(self, request):
        serializador = SerializadorCrearCurso(data=request.data)
        if serializador.is_valid():
            serializador.save(docente=request.user)
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        cursos = Curso.objects.filter(docente=request.user)
        serializador = SerializadorCrearCurso(cursos, many=True)
        return Response(serializador.data)
