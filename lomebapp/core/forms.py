from django import forms
from .models import Clientes, Produtos


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nome', 'cpf', 'telefone']


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['url_imagem', 'nome', 'descricao', 'preco', 'codigo_barras']
