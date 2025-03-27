from .models import Decisao, Resultado
from decimal import Decimal

# 💰 Parâmetros simulados (mock)
CUSTO_MATERIA_PRIMA = Decimal('5.00')
CUSTO_FIXO = Decimal('1000.00')
SALARIO_POR_FUNCIONARIO = Decimal('1200.00')
TREINAMENTO_POR_FUNC = Decimal('300.00')
TAXA_EMPRESTIMO = Decimal('0.05')  # 5% ao mês
PRECO_PADRAO = Decimal('20.00')
DEMANDA_PADRAO = Decimal('100')  # mock

def processar_rodada(decisao: Decisao) -> Resultado:
    preco = Decimal(decisao.preco or PRECO_PADRAO)
    demanda = DEMANDA_PADRAO

    receita = preco * demanda

    custo_mp = Decimal(decisao.prazo) * CUSTO_MATERIA_PRIMA
    folha = Decimal(decisao.funcionarios) * SALARIO_POR_FUNCIONARIO
    treinamento = TREINAMENTO_POR_FUNC * Decimal(decisao.funcionarios) if decisao.treinamento else Decimal(0)
    maquinas = Decimal(decisao.compra_maquinas) * Decimal('0')  # 🛠️ ajustar se quiser custo por máquina
    emprestimo_juros = Decimal(decisao.emprestimo) * TAXA_EMPRESTIMO
    antecipacao = Decimal(decisao.antecipacao or 0)

    custos_totais = (
        custo_mp + folha + treinamento + maquinas + CUSTO_FIXO + antecipacao
    )

    lucro = receita - custos_totais - emprestimo_juros
    patrimonio = lucro  # 🛠️ ajuste se quiser somar patrimônio acumulado

    resultado = Resultado.objects.create(
        empresa=decisao.empresa,
        rodada=decisao.rodada,
        receita=receita,
        custo=custos_totais,
        despesa=emprestimo_juros,
        lucro=lucro,
        patrimonio=patrimonio
    )

    return resultado