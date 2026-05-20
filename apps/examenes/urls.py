from django.urls import path
from apps.examenes.views import (
    VistaCrearCurso,
    VistaInscribirse,
    VistaCrearExamen,
    VistaEstudiantesCurso,
    VistaMisCursos,
    VistaExamenesCurso,
)

urlpatterns = [
    path('cursos/', VistaCrearCurso.as_view(), name='cursos'),
    path('inscribirse/', VistaInscribirse.as_view(), name='inscribirse'),
    path('examenes/', VistaCrearExamen.as_view(), name='examenes'),
    path('cursos/<int:curso_id>/estudiantes/', VistaEstudiantesCurso.as_view(), name='estudiantes_curso'),
    path('cursos/<int:curso_id>/estudiantes/<int:estudiante_id>/', VistaEstudiantesCurso.as_view(), name='eliminar_estudiante'),
    path('mis-cursos/', VistaMisCursos.as_view(), name='mis_cursos'),
    path('mis-cursos/<int:curso_id>/examenes/', VistaExamenesCurso.as_view(), name='examenes_curso'),
]
