from django import forms
from .models import Presente

class PresenteForm(forms.ModelForm):
    class Meta:
        model = Presente
        fields = ['nome', 'descricao', 'preco', 'foto']

