from rest_framework import serializers
from apps.examenes.models import Curso, Inscripcion


class SerializadorInscribirse(serializers.Serializer):
    codigo = serializers.CharField(max_length=8)

    def validate_codigo(self, value):
        if not Curso.objects.filter(codigo=value.upper()).exists():
            raise serializers.ValidationError('Código de curso inválido.')
        return value.upper()


class SerializadorInscripcion(serializers.ModelSerializer):
    class Meta:
        model = Inscripcion
        fields = ['id', 'curso', 'fecha']
