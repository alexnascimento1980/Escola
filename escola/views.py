from escola.models import Estudante, Curso
from escola.serializers import EstudanteSerializer, CursoSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response    

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
