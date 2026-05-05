from django.db import models


DIFICULTAD_CHOICES = [
    (1, 'Fácil'),
    (2, 'Medio'),
    (3, 'Difícil'),
]

MODO_CHOICES = [
    ('fijo', 'Fijo'),
    ('maestria', 'Maestría'),
]


class Examen(models.Model):
    curso = models.ForeignKey(
        'Curso',
        on_delete=models.CASCADE,
        related_name='examenes'
    )
    titulo = models.CharField(max_length=200)
    tema = models.CharField(max_length=200)
    tiempo = models.IntegerField(help_text='Duración total en minutos')
    num_preguntas = models.IntegerField(help_text='Mínimo de preguntas. En modo fijo es el total exacto')
    retroalimentacion = models.BooleanField(default=False)
    dificultad_inicial = models.IntegerField(choices=DIFICULTAD_CHOICES, default=2)
    max_intentos = models.IntegerField(default=1, help_text='Número de intentos permitidos. 0 = ilimitado')
    es_guiado = models.BooleanField(default=False, help_text='Si True, el agente genera una explicación antes de cada pregunta')
    modo = models.CharField(max_length=10, choices=MODO_CHOICES, default='fijo', help_text='Fijo: termina en num_preguntas. Maestría: termina cuando el estudiante domina los conceptos')
    max_preguntas = models.IntegerField(default=20, help_text='Solo en modo maestría. Tope máximo para evitar examen infinito')
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'examenes'
