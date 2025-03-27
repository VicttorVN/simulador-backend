# backend/simulador/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EmpresaViewSet,
    DecisaoViewSet,
    ParametroGlobalViewSet,
    RodadaViewSet,
    RodadaAtivaAPIView,
    DecisaoCreateView,
    resultado_empresa,
    ranking_empresas,
    resultado_por_empresa_rodada,
)

router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'decisoes', DecisaoViewSet)
router.register(r'parametros', ParametroGlobalViewSet)
router.register(r'rodadas', RodadaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/rodadas/ativas/', RodadaAtivaAPIView.as_view()),
    path('api/decisao/create/', DecisaoCreateView.as_view()),
    path('api/resultados/<int:empresa_id>/', resultado_empresa),
    path('api/ranking/', ranking_empresas),
    path('api/resultados/<int:empresa_id>/<int:rodada_id>/', resultado_por_empresa_rodada),  # ✅ novo
]