from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Presente(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL,
                                null=True)
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    preco = models.CharField(max_length=50)
    foto = models.ImageField(upload_to=f'{settings.BASE_DIR}/static/imgs', null=True, blank=True)
    criado = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.nome}"
    
    def preco_real(self):
        valor = str(self.preco)
        if 'R$' in valor:
            valor = valor.replace('R$', '')
            print(valor)
        if ',' in valor:
            valor = valor.replace(',', '.')
            print(valor)
        try:
            valor = float(valor)
            return f'R$ {valor:,.2f}'
        except Exception:
            return 'R$ 0.00'
