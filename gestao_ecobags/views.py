from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from rest_framework import generics, permissions
from .models import Usuario, Comentario, Estado, Cidade, Ponto, Movimentacao
from .serializers import UsuarioSerializer, ComentarioSerializer, EstadoSerializer, CidadeSerializer, PontoSerializer, MovimentacaoSerializer




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

class ComentarioListCreateView(generics.ListCreateAPIView):
    queryset = Comentario.objects.all().order_by("-data_hora")
    serializer_class = ComentarioSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]  # 🔥 GET público
        return [permissions.IsAuthenticated()]  # POST precisa de token