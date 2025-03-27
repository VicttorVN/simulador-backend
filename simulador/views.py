# backend/simulador/views.py

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Max

from .models import Rodada, Empresa, Decisao, Resultado, ParametroGlobal
from .serializers import (
    RodadaSerializer,
    EmpresaSerializer,
    DecisaoSerializer,
    ResultadoSerializer,
    RankingSerializer,
    ParametroGlobalSerializer
)
from .utils import processar_rodada


class RodadaViewSet(viewsets.ModelViewSet):
    queryset = Rodada.objects.all().order_by('-numero')
    serializer_class = RodadaSerializer


class RodadaAtivaAPIView(APIView):
    def get(self, request):
        rodadas_ativas = Rodada.objects.filter(ativa=True)
        serializer = RodadaSerializer(rodadas_ativas, many=True)
        return Response(serializer.data)


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


class DecisaoViewSet(viewsets.ModelViewSet):
    queryset = Decisao.objects.all().order_by('-data_envio')
    serializer_class = DecisaoSerializer


class ResultadoViewSet(viewsets.ModelViewSet):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer


class ParametroGlobalViewSet(viewsets.ModelViewSet):
    queryset = ParametroGlobal.objects.all()
    serializer_class = ParametroGlobalSerializer


class DecisaoCreateView(APIView):
    def post(self, request):
        serializer = DecisaoSerializer(data=request.data)
        if serializer.is_valid():
            decisao = serializer.save()
            resultado = processar_rodada(decisao)
            return Response({'decisao': serializer.data, 'resultado_id': resultado.id})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def resultado_empresa(request, empresa_id):
    resultados = Resultado.objects.filter(empresa_id=empresa_id).order_by('-rodada__numero')
    if not resultados.exists():
        return Response([], status=status.HTTP_200_OK)
    serializer = ResultadoSerializer(resultados, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ranking_empresas(request):
    ultima_rodada = Resultado.objects.aggregate(ultima=Max('rodada__numero'))['ultima']
    if ultima_rodada is not None:
        resultados = Resultado.objects.filter(
            rodada__numero=ultima_rodada
        ).order_by('-patrimonio')
        serializer = RankingSerializer(resultados, many=True)
        return Response(serializer.data)
    return Response([])


@api_view(['GET'])
def resultado_por_empresa_rodada(request, empresa_id, rodada_id):
    try:
        resultado = Resultado.objects.get(empresa_id=empresa_id, rodada_id=rodada_id)
        serializer = ResultadoSerializer(resultado)
        return Response(serializer.data)
    except Resultado.DoesNotExist:
        return Response({'detail': 'Resultado não encontrado'}, status=404)