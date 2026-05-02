from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiResponse, inline_serializer
from rest_framework import serializers as drf_serializers
from apps.users.serializers.serializador_iniciar_sesion import SerializadorIniciarSesion


@extend_schema(
    tags=['Usuarios'],
    summary='Iniciar sesión',
    description='Autentica al usuario con correo y contraseña. Retorna access y refresh token.',
    request=SerializadorIniciarSesion,
    responses={
        200: inline_serializer(
            name='RespuestaIniciarSesion',
            fields={
                'access': drf_serializers.CharField(),
                'refresh': drf_serializers.CharField(),
            }
        ),
        400: OpenApiResponse(description='Credenciales incorrectas'),
    },
    auth=[],
)
class VistaIniciarSesion(APIView):
    permission_classes = [AllowAny]

    def post(self, peticion):
        serializador = SerializadorIniciarSesion(data=peticion.data)
        serializador.is_valid(raise_exception=True)
        return Response(serializador.validated_data, status=status.HTTP_200_OK)
