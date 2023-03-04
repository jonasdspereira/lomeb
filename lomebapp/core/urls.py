from django.contrib import admin
from django.urls import path, include
from .views import home, cadastrar_cliente, lista_clientes, atualizar_cliente, excluir_cliente, cadastrar_produto, lista_produtos

urlpatterns = [
    path('', home),
    path('clientes/cadastrar/', cadastrar_cliente, name='cadastrar_cliente'),
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('clientes/atualizar/<int:pk>/',
         atualizar_cliente, name='atualizar_cliente'),
    path('clientes/<int:pk>/excluir/', excluir_cliente, name='excluir_cliente'),
    path('produtos/cadastrar/', cadastrar_produto, name='cadastrar_produto'),
    path('produtos/', lista_produtos, name='lista_produtos'),
]
