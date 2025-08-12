from rest_framework.serializers import ModelSerializer
from .models import Usuario, Comentario, Estado, Cidade, Ponto, Movimentacao    

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'
    
class EstadoSerializer(ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class CidadeSerializer(ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'  

class PontoSerializer(ModelSerializer):
    class Meta:
        model = Ponto
        fields = '__all__'

class MovimentacaoSerializer(ModelSerializer):
    class Meta:
        model = Movimentacao
        fields = '__all__'