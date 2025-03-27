from .models import Empresa, Rodada, Decisao, Resultado
from decimal import Decimal

# 💰 Parâmetros simulados
CUSTO_MATERIA_PRIMA = Decimal('5.00')
CUSTO_FIXO = Decimal('1000.00')
SALARIO_POR_FUNCIONARIO = Decimal('1200.00')
TREINAMENTO_POR_FUNC = Decimal('300.00')
TAXA_EMPRESTIMO = Decimal('0.05')  # 5% ao mês
PRECO_PADRAO = Decimal('20.00')  # fallback

def processar_rodada():
    try:
        rodada = Rodada.objects.get(ativa=True)
    except Rodada.DoesNotExist:
        return '❌ Nenhuma rodada ativa encontrada.'

    empresas = Empresa.objects.all()

    for empresa in empresas:
        try:
            decisao = Decisao.objects.get(empresa=empresa, rodada=rodada)
        except Decisao.DoesNotExist:
            continue

        # 👇🏽 Use os nomes atualizados dos campos do modelo Decisao
        preco = decisao.preco or PRECO_PADRAO
        demanda = 100

        receita = preco * demanda
        custo_mp = decisao.prazo * CUSTO_MATERIA_PRIMA
        folha = decisao.funcionarios * SALARIO_POR_FUNCIONARIO
        treinamento = (TREINAMENTO_POR_FUNC * decisao.funcionarios) if decisao.treinamento else 0
        maquinas = decisao.compra_maquinas
        emprestimo_juros = decisao.emprestimo * TAXA_EMPRESTIMO
        antecipacao = decisao.antecipacao or 0

        custos_totais = (
            custo_mp + folha + Decimal(treinamento) + Decimal(maquinas) +
            CUSTO_FIXO + Decimal(antecipacao)
        )
        lucro = receita - custos_totais - Decimal(emprestimo_juros)
        patrimonio = lucro + Decimal(empresa.capital_inicial or 0)

        Resultado.objects.create(
            empresa=empresa,
            rodada=rodada,
            receita=receita,
            custo=custos_totais,
            despesa=Decimal(emprestimo_juros),
            lucro=lucro,
            patrimonio=patrimonio
        )

    return '✅ Processamento concluído com sucesso!'