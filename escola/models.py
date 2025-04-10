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
    
'''Relacionar com o modelo Estudante
Se o Estudante for deletado, todas as matrículas daquele estudante devem ser deletadas
Relacionar com o modelo Curso
Se o Curso for deletado, todas as matriculas daquele curso devem ser deletadas
Período (Matutino, Vespertino, Noturno)
Não pode estar em Branco
Não pode ser Nulo
Por padrão deve ser Matutino'''

class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    )
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, null=False, blank=False, default='M')
    
    def __str__(self):
        return f'{self.estudante} - {self.curso}'