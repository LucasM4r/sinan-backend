from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema, OpenApiExample
from .models import *
from .serializers import *

@api_view(['GET'])
def healthcheck(request):
    """
    Rota simples para verificar se a API está online.
    """
    return Response({"status": "ok", "mensagem": "A API está a funcionar perfeitamente!"})

# Views de Autenticação
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        """
        Endpoint para autenticação de usuários.
        Retorna tokens JWT (access e refresh) se as credenciais forem válidas.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = serializer.validated_data.get('access')

        return Response(
            {
                'access_token': token,
            },
            status=status.HTTP_200_OK
        )

# ViewSets  Principais

class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerilizer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


# ViewSets para as Notificações Gerais e Específicas

class NotificacaoViewSet(viewsets.ModelViewSet):
    queryset = Notificacao.objects.all()
    serializer_class = NotificacaoSerializer

class NotificacaoAidsViewSet(viewsets.ModelViewSet):
    queryset = NotificacaoAids.objects.all()
    serializer_class = NotificacaoAidsSerializer

class NotificacaoBotulismoViewSet(viewsets.ModelViewSet):
    queryset = NotificacaoBotulismo.objects.all()
    serializer_class = NotificacaoBotulismoSerializer

class NotificacaoEpizootiaViewSet(viewsets.ModelViewSet):
    queryset = NotificacaoEpizootia.objects.all()
    serializer_class = NotificacaoEpizootiaSerializer

class NotificacaoEsquistossomoseViewSet(viewsets.ModelViewSet):
    queryset = NotificacaoEsquistossomose.objects.all()
    serializer_class = NotificacaoEsquistossomoseSerializer

class NotificacaoFebreAmarelaViewSet(viewsets.ModelViewSet):
    queryset = NotificacaoFebreAmarela.objects.all()
    serializer_class = NotificacaoFebreAmarelaSerializer

class NotificacaoDengueChikungunyaViewSet(viewsets.ModelViewSet):
    queryset = NotificacaoDengueChikungunya.objects.all()
    serializer_class = NotificacaoDengueChikungunyaSerializer

class NotificacaoAnimalPeconhentoViewSet(viewsets.ModelViewSet):
    queryset = NotificacaoAnimalPeconhento.objects.all()
    serializer_class = NotificacaoAnimalPeconhentoSerializer

class NotificacaoAntiRabicoViewSet(viewsets.ModelViewSet):
    queryset = NotificacaoAntiRabico.objects.all()
    serializer_class = NotificacaoAntiRabicoSerializer

class NotificacaoColeraViewSet(viewsets.ModelViewSet):
    queryset = NotificacaoColera.objects.all()
    serializer_class = NotificacaoColeraSerializer

class NotificacaoChikungunyaViewSet(viewsets.ModelViewSet):
    queryset = NotificacaoChikungunya.objects.all()
    serializer_class = NotificacaoChikungunyaSerializer

class NotificacaoCoquelucheViewSet(viewsets.ModelViewSet):
    queryset = NotificacaoCoqueluche.objects.all()
    serializer_class = NotificacaoCoquelucheSerializer