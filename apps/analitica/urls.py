from django.urls import path
from apps.analitica.views import (
    VistaMisResultados,
    VistaResultadosCurso,
    VistaAvanceEstudiante,
    VistaModeloConocimientoEstudiante,
    VistaPatronesCurso,
    VistaResumenCurso,
)

urlpatterns = [
    # Estudiante
    path('mis-resultados/', VistaMisResultados.as_view(), name='mis_resultados'),

    # Docente — resumen y patrones del curso
    path('curso/<int:curso_id>/resumen/', VistaResumenCurso.as_view(), name='resumen_curso'),
    path('curso/<int:curso_id>/patrones/', VistaPatronesCurso.as_view(), name='patrones_curso'),
    path('curso/<int:curso_id>/resultados/', VistaResultadosCurso.as_view(), name='resultados_curso'),

    # Docente — por estudiante
    path('curso/<int:curso_id>/estudiante/<int:estudiante_id>/', VistaAvanceEstudiante.as_view(), name='avance_estudiante'),
    path('curso/<int:curso_id>/estudiante/<int:estudiante_id>/conocimiento/', VistaModeloConocimientoEstudiante.as_view(), name='modelo_conocimiento'),
]
