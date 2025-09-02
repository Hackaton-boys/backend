from django.db import models
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nome, telefone=None, password=None, **extra_fields):
        if not email:
            raise ValueError("O usuário precisa de um email")
        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, telefone=telefone, **extra_fields)
        user.set_password(password)  # criptografa a senha
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, telefone=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, nome, telefone, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)

    # Flags do Django
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)   # acesso ao Django Admin
    is_superuser = models.BooleanField(default=False)  # superusuário

    USERNAME_FIELD = "email"          # login será feito com email
    REQUIRED_FIELDS = ["nome"]        # campos obrigatórios ao criar superuser

    objects = UsuarioManager()

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
