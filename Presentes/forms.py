from django import forms
from .models import Presente

class PresenteForm(forms.ModelForm):
    preco = forms.CharField(label='Preço', max_length=100)
    class Meta:
        model = Presente
        fields = ['nome', 'descricao', 'preco', 'foto']

    @property
    def preco_real(self):
        valor = str(self['preco'])
        if 'R$' in valor:
            valor = valor.replace('R$', '')
        if ',' in valor:
            valor = valor.replace(',', '.')
        try:
            valor = float(valor)
            return f'R$ {valor:,.2f}'
        except Exception:
            return 'R$ 0.00'