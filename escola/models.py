from django.db import models

# Create your models here.

class Estudante(models.Model):
    
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=False)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    numero_celular = models.CharField(max_length=14)

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    codigo = models.CharField(max_length=10, unique=True)
    descricao = models.CharField(max_length=255, blank=False)
    nivel = models.CharField(max_length=1, choices=NIVEL, null=False, blank=False, default='B')
    
    def __str__(self):
        return self.codigo
    
