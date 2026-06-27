from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

# Regista as rotas principais
router.register(r'unidades', UnidadeViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'pacientes', PacienteViewSet)

# Regista as rotas das notificações por agravo
router.register(r'notificacoes', NotificacaoViewSet)
router.register(r'notificacoes-aids', NotificacaoAidsViewSet)
router.register(r'notificacoes-botulismo', NotificacaoBotulismoViewSet)
router.register(r'notificacoes-epizootia', NotificacaoEpizootiaViewSet)
router.register(r'notificacoes-esquistossomose', NotificacaoEsquistossomoseViewSet)
router.register(r'notificacoes-febre-amarela', NotificacaoFebreAmarelaViewSet)
router.register(r'notificacoes-dengue-chikungunya', NotificacaoDengueChikungunyaViewSet)
router.register(r'notificacoes-animal-peconhento', NotificacaoAnimalPeconhentoViewSet)
router.register(r'notificacoes-anti-rabico', NotificacaoAntiRabicoViewSet)
router.register(r'notificacoes-colera', NotificacaoColeraViewSet)
router.register(r'notificacoes-chikungunya', NotificacaoChikungunyaViewSet)
router.register(r'notificacoes-coqueluche', NotificacaoCoquelucheViewSet)

urlpatterns = [
    path(r'api/v1/auth/login', LoginView.as_view(), name='login'),

    path('health/', healthcheck, name='healthcheck'),
    path('api/v1/', include(router.urls)),
]

