# backend/simulador/scripts/simulador_teste.py

import os
import django
import random
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from simulador.models import Empresa, Rodada, Decisao
from simulador.utils import processar_rodada

# ⚠️ Limpar dados antigos
Empresa.objects.all().delete()
Rodada.objects.all().delete()
Decisao.objects.all().delete()

# 🏢 Criar empresas
nomes = ["Alpha Ltda", "Beta S/A", "Gamma Indústria"]
empresas = [Empresa.objects.create(nome=nome) for nome in nomes]

# 🔄 Criar rodada ativa
rodada = Rodada.objects.create(numero=1, ativa=True)

# 📩 Criar decisões simuladas
for empresa in empresas:
    decisao = Decisao.objects.create(
        empresa=empresa,
        rodada=rodada,
        preco=Decimal(random.randint(80, 120)),
        propaganda=random.randint(1, 3),
        prazo=random.randint(15, 45),
        juros=Decimal(random.uniform(1, 5)),
        funcionarios=random.randint(5, 20),
        treinamento=random.choice([True, False]),
        compra_maquinas=random.randint(0, 3),
        emprestimo=Decimal(random.randint(1000, 5000)),
        antecipacao=Decimal(random.randint(500, 3000))
    )

# ⚙️ Rodar simulação
resultado = processar_rodada(None)
print(resultado)