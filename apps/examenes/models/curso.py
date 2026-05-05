import random
import string
from django.conf import settings
from django.db import models


def generar_codigo():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, default='')
    docente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cursos'
    )
    codigo = models.CharField(max_length=8, unique=True, default=generar_codigo)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cursos'
