from tokenize import TokenError
import uuid

from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view
from rest_framework.views import APIView
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
                'access': token,
                'refresh': serializer.validated_data.get('refresh')
            },
            status=status.HTTP_200_OK
        )

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        """
        Endpoint para logout de usuários.
        Invalida o token de refresh fornecido.
        """
        try:
            refresh_token = request.data.get("refresh")
            
            if not refresh_token:
                return Response(
                    {
                        "type": "validation_error",
                        "detail": "O campo 'refresh' é obrigatório.",
                        "code": "missing_field"
                    }, 
                    status=status.HTTP_400_BAD_REQUEST
                )

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except TokenError as e:
            return Response(
                {
                    "type": "token_error",
                    "detail": f"Erro ao invalidar o token: {str(e)}",
                    "code": "token_error"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {
                    "type": "server_error",
                    "detail": f"Erro interno ao processar o logout: {str(e)}",
                    "request_id": str(uuid.uuid4())
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
# ViewSets  Principais
class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

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