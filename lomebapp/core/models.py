# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AquisicoesProdutos(models.Model):
    id = models.BigAutoField(primary_key=True)
    data_aquisicao = models.DateTimeField()
    quantidade = models.IntegerField()
    nota_fiscal = models.TextField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    id_distribuidora = models.ForeignKey(
        'Distribuidoras', models.DO_NOTHING, db_column='id_distribuidora', blank=True, null=True)
    id_produto = models.ForeignKey(
        'Produtos', models.DO_NOTHING, db_column='id_produto', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aquisicoes_produtos'


class Clientes(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    cpf = models.CharField(unique=True, max_length=11, verbose_name='CPF')
    telefone = models.CharField(max_length=13)

    class Meta:
        managed = False
        db_table = 'clientes'


class Distribuidoras(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome_fantasia = models.CharField(max_length=50)
    cnpj = models.CharField(unique=True, max_length=14)
    logradouro = models.CharField(max_length=30, blank=True, null=True)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'distribuidoras'


class EstoquesFiliais(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_produto = models.ForeignKey(
        'Produtos', models.DO_NOTHING, db_column='id_produto', blank=True, null=True)
    id_filial = models.ForeignKey(
        'Filiais', models.DO_NOTHING, db_column='id_filial', blank=True, null=True)
    lote = models.CharField(max_length=12)
    data_validade = models.DateTimeField()
    quantidade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'estoques_filiais'


class FarmaceuticoResponsaveis(models.Model):
    id_medicamento = models.OneToOneField(
        'ProdutosMedicamento', models.DO_NOTHING, db_column='id_medicamento', primary_key=True)
    crf = models.CharField(max_length=9)
    uf_registro = models.CharField(max_length=2)
    nome = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'farmaceutico_responsaveis'
        unique_together = (('id_medicamento', 'crf', 'uf_registro'),)


class Filiais(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    logradouro = models.CharField(max_length=30)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'filiais'


class Funcionarios(models.Model):
    matricula = models.CharField(primary_key=True, max_length=7)
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=180)
    telefone = models.CharField(max_length=13)
    funcao = models.CharField(max_length=20)
    observacoes = models.TextField(blank=True, null=True)
    senha = models.CharField(max_length=15)
    id_filial = models.ForeignKey(
        Filiais, models.DO_NOTHING, db_column='id_filial', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'funcionarios'


class HistoricoMovimentacoesEstoques(models.Model):
    id = models.BigAutoField(primary_key=True)
    data_movimentacao = models.DateTimeField()
    quantidade_movimentada = models.IntegerField()
    motivo = models.CharField(max_length=15)
    status = models.CharField(max_length=12)
    observacoes = models.TextField(blank=True, null=True)
    id_estoque = models.ForeignKey(
        EstoquesFiliais, models.DO_NOTHING, db_column='id_estoque', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historico_movimentacoes_estoques'


class HistoricoProdutosRestritos(models.Model):
    id = models.BigAutoField(primary_key=True)
    observacoes = models.TextField()
    url_documento_retido = models.TextField()
    id_item_venda = models.ForeignKey(
        'ItensVendas', models.DO_NOTHING, db_column='id_item_venda', blank=True, null=True)
    matricula_funcionario_responsavel = models.ForeignKey(
        Funcionarios, models.DO_NOTHING, db_column='matricula_funcionario_responsavel', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historico_produtos_restritos'


class ItensVendas(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantidade = models.IntegerField()
    id_venda = models.ForeignKey(
        'VendasProdutos', models.DO_NOTHING, db_column='id_venda', blank=True, null=True)
    id_produto = models.ForeignKey(
        'Produtos', models.DO_NOTHING, db_column='id_produto', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itens_vendas'


class Laboratorios(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(unique=True, max_length=14)
    registro_anvisa = models.CharField(unique=True, max_length=17)
    logradouro = models.CharField(max_length=30)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'laboratorios'


class OrdensEntregas(models.Model):
    id = models.BigAutoField(primary_key=True)
    data_entrega = models.DateTimeField()
    observacoes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=30)
    logradouro = models.CharField(max_length=30)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=30)
    ponto_referencia = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    id_venda = models.ForeignKey(
        'VendasProdutos', models.DO_NOTHING, db_column='id_venda')

    class Meta:
        managed = False
        db_table = 'ordens_entregas'


class Produtos(models.Model):
    id = models.BigAutoField(primary_key=True)
    url_imagem = models.TextField()
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    codigo_barras = models.CharField(unique=True, max_length=13)

    class Meta:
        managed = False
        db_table = 'produtos'


class ProdutosMedicamento(models.Model):
    id_produto = models.OneToOneField(
        Produtos, models.DO_NOTHING, db_column='id_produto', primary_key=True)
    url_bula = models.TextField()
    tipo_medicamento = models.CharField(max_length=20)
    categoria_medicamento = models.CharField(max_length=20)
    classificacao_medicamento = models.CharField(max_length=20)
    retem_receita = models.IntegerField()
    registro_anvisa = models.CharField(unique=True, max_length=17)

    class Meta:
        managed = False
        db_table = 'produtos_medicamento'


class ProdutosNaoMedicamento(models.Model):
    id_produto = models.OneToOneField(
        Produtos, models.DO_NOTHING, db_column='id_produto', primary_key=True)
    categoria = models.CharField(max_length=30)
    unidade_medida = models.CharField(max_length=10)
    quantidade_medida = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'produtos_nao_medicamento'


class Servicos(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_servico = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'servicos'


class ServicosAdquiridosClientes(models.Model):
    id_filial = models.ForeignKey(
        Filiais, models.DO_NOTHING, db_column='id_filial')
    id_cliente = models.ForeignKey(
        Clientes, models.DO_NOTHING, db_column='id_cliente')
    id_servico = models.ForeignKey(
        Servicos, models.DO_NOTHING, db_column='id_servico')
    data_aquisicao = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'servicos_adquiridos_clientes'
        unique_together = (('data_aquisicao', 'id_filial',
                           'id_cliente', 'id_servico'),)


class ServicosFiliais(models.Model):
    id_filial = models.OneToOneField(
        Filiais, models.DO_NOTHING, db_column='id_filial', primary_key=True)
    id_servico = models.ForeignKey(
        Servicos, models.DO_NOTHING, db_column='id_servico')

    class Meta:
        managed = False
        db_table = 'servicos_filiais'
        unique_together = (('id_filial', 'id_servico'),)


class TelefonesDistribuidoras(models.Model):
    id_distribuidora = models.OneToOneField(
        Distribuidoras, models.DO_NOTHING, db_column='id_distribuidora', primary_key=True)
    telefone = models.CharField(max_length=13)

    class Meta:
        managed = False
        db_table = 'telefones_distribuidoras'
        unique_together = (('id_distribuidora', 'telefone'),)


class TelefonesFiliais(models.Model):
    id_filial = models.OneToOneField(
        Filiais, models.DO_NOTHING, db_column='id_filial', primary_key=True)
    telefone = models.CharField(max_length=13)

    class Meta:
        managed = False
        db_table = 'telefones_filiais'
        unique_together = (('id_filial', 'telefone'),)


class TelefonesLaboratorios(models.Model):
    id_laboratorio = models.OneToOneField(
        Laboratorios, models.DO_NOTHING, db_column='id_laboratorio', primary_key=True)
    telefone = models.CharField(max_length=13)

    class Meta:
        managed = False
        db_table = 'telefones_laboratorios'
        unique_together = (('id_laboratorio', 'telefone'),)


class VendasProdutos(models.Model):
    id = models.BigAutoField(primary_key=True)
    data_compra = models.DateTimeField()
    forma_pagamento = models.CharField(max_length=15)
    porcentagem_desconto = models.DecimalField(
        max_digits=5, decimal_places=3, blank=True, null=True)
    id_cliente = models.ForeignKey(
        Clientes, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    matricula_funcionario = models.ForeignKey(
        Funcionarios, models.DO_NOTHING, db_column='matricula_funcionario', blank=True, null=True)
    id_filial = models.ForeignKey(
        Filiais, models.DO_NOTHING, db_column='id_filial', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendas_produtos'
