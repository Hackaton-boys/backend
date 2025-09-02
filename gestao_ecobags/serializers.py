from rest_framework.serializers import ModelSerializer
from .models import Usuario, Comentario, Estado, Cidade, Ponto, Movimentacao    

from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # senha só para escrita

    class Meta:
        model = Usuario
        fields = ['id_usuario', 'nome', 'email', 'telefone', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = Usuario(**validated_data)
        if password:
            user.set_password(password)  # criptografa a senha
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)  # criptografa ao atualizar
        instance.save()
        return instance

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