from rest_framework import serializers
from apps.examenes.models import Curso


class SerializadorCrearCurso(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nombre', 'descripcion', 'codigo', 'creado_en']
        read_only_fields = ['codigo', 'creado_en']


class SerializadorCurso(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nombre', 'descripcion', 'codigo', 'creado_en']
