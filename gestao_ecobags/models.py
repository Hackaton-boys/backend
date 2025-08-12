from django.db import models
from django.core.exceptions import ValidationError

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    
class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    comentario = models.TextField(max_length=750)
    fk_usuario = models.ForeignKey(
        'Usuario',
        on_delete=models.CASCADE,
        db_column='fk_usuario'
    )
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fk_usuario.nome} comentou: {self.comentario[:30]}..."
    
class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=35)
    sigla = models.CharField(max_length=3)

    def __str__(self):
        return self.sigla 

class Cidade(models.Model):
    id_cidade = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    sigla = models.CharField(max_length=5)
    fk_estado = models.ForeignKey(
        "Estado",
        on_delete=models.CASCADE,
        db_column='fk_estado'
    )

    def __str__(self):
        return f"{self.nome} - {self.fk_estado.sigla}"

class Ponto(models.Model):
    id_ponto = models.AutoField(primary_key=True)
    descricao = models.TextField(max_length=500)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    endereco = models.CharField(max_length=255)
    estoque = models.IntegerField()
    fk_usuario = models.ForeignKey(
        'Usuario',
        on_delete=models.CASCADE,
        db_column='fk_usuario'
    )
    fk_cidade = models.ForeignKey(
        'Cidade',
        on_delete=models.CASCADE,
        db_column='fk_cidade'
    )

    def __str__(self):
        return f"{self.endereco} Estoque: {self.estoque}"
    
class Movimentacao(models.Model):
    Tipo_Choices = (
        (1, 'Entrada'),
        (2, 'Saída'),
    )

    id_movimentacao = models.AutoField(primary_key=True)
    tipo = models.PositiveSmallIntegerField(choices=Tipo_Choices)
    quantidade = models.IntegerField()
    data_hora = models.DateTimeField(auto_now_add=True)
    fk_usuario = models.ForeignKey(
        'Usuario',
        on_delete=models.CASCADE,
        db_column='fk_usuario'
    )

    def __str__(self):
        return f"{self.get_tipo_display()} de {self.quantidade} por {self.fk_usuario.nome} em {self.data_hora}"
