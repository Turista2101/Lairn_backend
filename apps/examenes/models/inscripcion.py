from django.conf import settings
from django.db import models


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )
    curso = models.ForeignKey(
        'Curso',
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'inscripciones'
        unique_together = ('estudiante', 'curso')
