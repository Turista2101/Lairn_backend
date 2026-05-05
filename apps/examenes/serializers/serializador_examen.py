from rest_framework import serializers
from apps.examenes.models import Examen


class SerializadorCrearExamen(serializers.ModelSerializer):
    class Meta:
        model = Examen
        fields = [
            'id', 'curso', 'titulo', 'tema', 'tiempo', 'num_preguntas',
            'retroalimentacion', 'dificultad_inicial', 'max_intentos', 'es_guiado',
            'modo', 'max_preguntas', 'creado_en'
        ]
        read_only_fields = ['creado_en']

    def validate_max_intentos(self, value):
        if value < 0 or value > 10:
            raise serializers.ValidationError('max_intentos debe ser entre 0 (ilimitado) y 10.')
        return value

    def validate(self, data):
        if data.get('modo') == 'maestria':
            num = data.get('num_preguntas', 1)
            max_p = data.get('max_preguntas', 20)
            if max_p < num:
                raise serializers.ValidationError(
                    'max_preguntas debe ser mayor o igual a num_preguntas en modo maestría.'
                )
        return data


class SerializadorExamen(serializers.ModelSerializer):
    class Meta:
        model = Examen
        fields = [
            'id', 'titulo', 'tema', 'tiempo', 'num_preguntas',
            'retroalimentacion', 'dificultad_inicial', 'max_intentos', 'es_guiado',
            'modo', 'max_preguntas', 'creado_en'
        ]
