from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="home"),  
    path("ver_cursos", views.ver_cursos, name="cursos"),
    path("alumnos", views.alumnos, name="alumnos"),
    path("profesores", views.profesores, name="profesores"),
    path("alta_curso", views.curso_formulario, name="alta_curso"),
    path("buscar_curso", views.buscar_curso, name="buscar_curso"),
    path("buscar", views.buscar),
    path("elimina_curso/<int:id>" , views.elimina_curso , name="elimina_curso"),
    path("editar_curso/<int:id>" , views.editar , name="editar_curso"),
    path("", views.home, name="home"),
    path("registro_escuela", views.registro_escuela, name="registro_escuela"),
    path("agregar_alumno", views.agregar_alumno, name="agregar_alumno"),
    path("agregar_profesor", views.agregar_profesor, name="agregar_profesor"),
    path("confirmacion_profesor", views.confirmacion_profesor, name="confirmacion_profesor"),
    path("confirmacion_alumno", views.confirmacion_alumno, name="confirmacion_alumno"),
]
