from django.db import models

class Rodada(models.Model):
    numero = models.PositiveIntegerField()
    ativa = models.BooleanField(default=False)
    data_abertura = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rodada {self.numero}"

class Empresa(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Decisao(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    rodada = models.ForeignKey(Rodada, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    propaganda = models.IntegerField()
    prazo = models.IntegerField()
    juros = models.DecimalField(max_digits=5, decimal_places=2)
    funcionarios = models.IntegerField()
    treinamento = models.BooleanField(default=False)
    compra_maquinas = models.IntegerField()
    emprestimo = models.DecimalField(max_digits=10, decimal_places=2)
    antecipacao = models.DecimalField(max_digits=10, decimal_places=2)
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Decisão - {self.empresa} - Rodada {self.rodada.numero}"

class Resultado(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    rodada = models.ForeignKey(Rodada, on_delete=models.CASCADE)
    receita = models.DecimalField(max_digits=10, decimal_places=2)
    despesa = models.DecimalField(max_digits=10, decimal_places=2)
    lucro = models.DecimalField(max_digits=10, decimal_places=2)
    patrimonio = models.DecimalField(max_digits=10, decimal_places=2)
    custo = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Resultado - {self.empresa} - Rodada {self.rodada.numero}"

class ParametroGlobal(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome}: {self.valor}"