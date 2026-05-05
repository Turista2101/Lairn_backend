from rest_framework import serializers
from apps.examenes.models import Inscripcion


class SerializadorEstudianteCurso(serializers.ModelSerializer):
    estudiante_id = serializers.IntegerField(source='estudiante.id', read_only=True)
    nombre = serializers.SerializerMethodField()
    email = serializers.EmailField(source='estudiante.email', read_only=True)

    def get_nombre(self, obj):
        return f"{obj.estudiante.first_name} {obj.estudiante.first_last_name}"

    class Meta:
        model = Inscripcion
        fields = ['id', 'estudiante_id', 'nombre', 'email', 'fecha']
