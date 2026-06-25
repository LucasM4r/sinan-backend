
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def healthcheck(request):
    """
    Rota simples para verificar se a API está online.
    """
    return Response({"status": "ok", "mensagem": "A API está a funcionar perfeitamente!"})

# ViewSets para processar as requisições