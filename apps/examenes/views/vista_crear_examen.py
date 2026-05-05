from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiResponse
from core.permissions.permisos_rol import EsDocente
from apps.examenes.models import Curso, Examen
from apps.examenes.serializers import SerializadorCrearExamen


@extend_schema_view(
    get=extend_schema(
        tags=['Exámenes'],
        summary='Listar mis exámenes',
        description='Retorna todos los exámenes creados en los cursos del docente autenticado.',
        responses={
            200: SerializadorCrearExamen(many=True),
            403: OpenApiResponse(description='Solo los docentes pueden acceder'),
        },
    ),
    post=extend_schema(
        tags=['Exámenes'],
        summary='Crear examen',
        description=(
            'Crea un examen dentro de un curso. El agente de IA generará las preguntas en tiempo real '
            'cuando el estudiante lo presente.\n\n'
            '**Parámetros clave:**\n'
            '- `num_preguntas`: En modo fijo es el total exacto. En modo maestría es el mínimo garantizado.\n'
            '- `max_intentos`: 0 = ilimitado, 1-10 = número exacto de intentos.\n'
            '- `dificultad_inicial`: 1=Fácil, 2=Medio, 3=Difícil.\n'
            '- `modo`: `fijo` termina al llegar a num_preguntas. `maestria` termina cuando el '
            'estudiante domina todos los conceptos o alcanza max_preguntas.\n'
            '- `es_guiado`: Si es true, el agente genera una explicación del concepto antes de cada pregunta.\n'
            '- `retroalimentacion`: Si es true, el estudiante ve si acertó o falló después de cada respuesta.'
        ),
        request=SerializadorCrearExamen,
        responses={
            201: SerializadorCrearExamen,
            400: OpenApiResponse(description='Datos inválidos o max_preguntas menor que num_preguntas en modo maestría'),
            403: OpenApiResponse(description='Solo los docentes pueden crear exámenes o el curso no le pertenece'),
        },
    ),
)
class VistaCrearExamen(APIView):
    permission_classes = [EsDocente]

    def post(self, request):
        serializador = SerializadorCrearExamen(data=request.data)
        if not serializador.is_valid():
            return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)

        curso = serializador.validated_data['curso']
        if curso.docente != request.user:
            return Response(
                {'detalle': 'No tienes permiso para crear exámenes en este curso.'},
                status=status.HTTP_403_FORBIDDEN
            )

        serializador.save()
        return Response(serializador.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        cursos_docente = Curso.objects.filter(docente=request.user)
        examenes = Examen.objects.filter(curso__in=cursos_docente)
        serializador = SerializadorCrearExamen(examenes, many=True)
        return Response(serializador.data)
