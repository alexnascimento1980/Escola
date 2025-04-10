from django.contrib import admin
from django.urls import path, include
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculasEstudantes, ListaMatriculasCursos
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'estudantes', EstudanteViewSet, basename='Estudantes')
router.register(r'cursos', CursoViewSet, basename='Cursos')
router.register(r'matriculas', MatriculaViewSet, basename='Matriculas')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('estudantes/<int:pk>/matriculas/', ListaMatriculasEstudantes.as_view(), name='ListaMatriculasEstudantes'),
    path('cursos/<int:pk>/matriculas/', ListaMatriculasCursos.as_view(), name='ListaMatriculasCursos'),
    
]
