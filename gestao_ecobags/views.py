from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Usuario, Comentario, Estado, Cidade, Ponto, Movimentacao
from .serializers import UsuarioSerializer, ComentarioSerializer, EstadoSerializer, CidadeSerializer, PontoSerializer, MovimentacaoSerializer 

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class CidadeViewSet(ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class PontoViewSet(ModelViewSet):
    queryset = Ponto.objects.all()
    serializer_class = PontoSerializer  

class MovimentacaoViewSet(ModelViewSet):
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    user = request.user
    return Response({
        "id_usuario": getattr(user, "id_usuario", None),
        "nome": getattr(user, "nome", None),
        "email": getattr(user, "email", None),
        "telefone": getattr(user, "telefone", None),
    })