from django.db import models
from empresa.models import Empresa
from produto.models import Produto
from django.contrib.auth.models import User

class Movimentacoes(models.Model):
    qtde = models.IntegerField()
    data = models.DateField(auto_now_add=True)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return f"Movimento de {self.qtde} unidades"
