# backend/simulador/serializers.py

from rest_framework import serializers
from .models import Empresa, Rodada, Decisao, Resultado, ParametroGlobal

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class RodadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rodada
        fields = '__all__'

class DecisaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decisao
        fields = '__all__'

class ResultadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultado
        fields = '__all__'

class ParametroGlobalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParametroGlobal
        fields = '__all__'

# ✅ Ranking usado pela tela /professor
class RankingSerializer(serializers.ModelSerializer):
    empresa = serializers.StringRelatedField()

    class Meta:
        model = Resultado
        fields = ['empresa', 'lucro', 'patrimonio']