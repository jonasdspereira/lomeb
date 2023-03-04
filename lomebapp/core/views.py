from django.shortcuts import get_object_or_404, render, redirect
from .models import Clientes, Produtos
from .forms import ClienteForm, ProdutoForm

# Create your views here.


def home(request):
    return render(request, "index.html")


def cadastrar_cliente(request):

    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_clientes')

    context = {
        'title': 'Cadastrar Cliente',
        'form': form
    }
    return render(request, 'cadastrar_cliente.html', context)


def lista_clientes(request):
    clientes = Clientes.objects.all()
    context = {
        'title': 'Clientes',
        'clientes': clientes,
    }
    return render(request, 'lista_clientes.html', context)


def excluir_cliente(request, pk):
    clientes = get_object_or_404(Clientes, pk=pk)
    if request.method == 'POST':
        clientes.delete()
        return redirect('lista_clientes')
    context = {'cliente': clientes}
    return render(request, 'excluir_cliente.html', context)


def atualizar_cliente(request, pk):
    clientes = get_object_or_404(Clientes, pk=pk)
    form = ClienteForm(request.POST or None, instance=clientes)
    if form.is_valid():
        form.save()
        return redirect('lista_clientes')
    context = {
        'form': form,
        'title': 'Atualizar cliente',
    }
    return render(request, 'cadastrar_cliente.html', context)


def cadastrar_produto(request):

    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')

    context = {
        'title': 'Cadastrar produto',
        'form': form
    }
    return render(request, 'cadastrar_produto.html', context)


def lista_produtos(request):
    produtos = Produtos.objects.all()
    context = {
        'title': 'Clientes',
        'clientes': produtos,
    }
    return render(request, 'lista_produtos.html', context)
