from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola.validators import cpf_invalido, nome_invalido, numero_celular_invalido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'numero_celular']
    
    def validate(self,dados):
        if cpf_invalido(dados["cpf"]):
            raise serializers.ValidationError({'cpf':'O CPF deve ter um valor válido.'})
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome':'O nome deve conter apenas letras.'})    
        if numero_celular_invalido(dados['numero_celular']):
            raise serializers.ValidationError({'numero_celular':'O número de numero_celular deve seguir a seguinte formatação: ## #####-####(repseitando traços e espaços).'})
        return dados

        

    
    
        
    # def validate_cpf(self, cpf):
    #     # if len(cpf) != 11:
    #     #     raise serializers.ValidationError('O CPF deve conter 11 dígitos.')
    #     # return cpf
    
    # def validate_nome(self, nome):
    #     if not nome.isalpha():
    #         raise serializers.ValidationError('O nome deve conter apenas letras.')
    #     return nome
    # def validate_numero_celular(self, numero_celular):
    #     if len(numero_celular) != 13:
    #         raise serializers.ValidationError('O número de numero_celular deve conter 13 dígitos.')
    #     return numero_celular
    
    
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []
        
class ListaMatriculasEstudandesSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
class ListaMatriculasCursosSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome']
    def get_periodo(self, obj):
        return obj.get_periodo_display()
                     