from django.contrib import admin
from .models import Usuario
from .models import Comentario
from .models import Estado
from .models import Cidade
from .models import Ponto
from .models import Movimentacao

admin.site.register(Usuario)
admin.site.register(Comentario)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Ponto)
admin.site.register(Movimentacao)