# backend/simulador/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EmpresaViewSet,
    DecisaoViewSet,
    ParametroGlobalViewSet,  # NOVO
    RodadaAtivaAPIView,
    DecisaoCreateView,
    resultado_empresa,
    ranking_empresas
)

router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'decisoes', DecisaoViewSet)
router.register(r'parametros', ParametroGlobalViewSet)  # NOVO

urlpatterns = [
    path('', include(router.urls)),  # /api/empresas, /api/decisoes...
    path('rodadas/ativas/', RodadaAtivaAPIView.as_view()),
    path('decisao/create/', DecisaoCreateView.as_view()),
    path('resultados/<int:empresa_id>/', resultado_empresa),
    path('ranking/', ranking_empresas),
]