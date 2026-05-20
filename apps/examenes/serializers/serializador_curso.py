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


class SerializadorCursoEstudiante(serializers.ModelSerializer):
    docente = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = ['id', 'nombre', 'descripcion', 'docente', 'creado_en']

    def get_docente(self, obj):
        d = obj.docente
        return f"{d.first_name} {d.first_last_name}".strip()
