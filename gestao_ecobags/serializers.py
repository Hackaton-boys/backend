from rest_framework.serializers import ModelSerializer
from .models import Usuario, Comentario, Estado, Cidade, Ponto, Movimentacao    
from rest_framework import serializers


class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # não retorna a senha

    class Meta:
        model = Usuario
        fields = ["id_usuario", "username", "email", "telefone", "password"]

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = Usuario(**validated_data)
        if password:
            user.set_password(password)  # 🔑 aqui é a mágica
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)  # 🔑 também no update
        instance.save()
        return instance

class ComentarioSerializer(ModelSerializer):
    usuario = serializers.StringRelatedField(source="fk_usuario", read_only=True)

    def create(self, validated_data):
        username = validated_data.pop("username")
        try:
            user = Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            raise serializers.ValidationError({"username": "Usuário não encontrado"})
        
        return Comentario.objects.create(fk_usuario=user, **validated_data)

    class Meta:
        model = Comentario
        fields = ["id_comentario", "comentario", "usuario", "username", "data_hora"]
    
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
