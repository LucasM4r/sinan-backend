
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404

# ViewSets para processar as requisições