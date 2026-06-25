'''
Módulo de Serialização (API Integration)
    * Realiza a transformação dos modelos Django em formato JSON.
    * Facilita a comunicação entre o banco de dados e o front-end.
    * Define serializadores para todas as entidades e tipos de notificação.
    * Serializer serao usados no views depois
    * Atributos:
    :param fields: Especifica os campos a serem incluídos na serialização (neste caso, todos os campos).
    :type fields: list ou str

    :param model: Define o modelo a ser serializado.
    :type model: Django Model
'''

from rest_framework import serializers
from .models import *

class UnidadeSerializer(serializers.ModelSerializer): # Serializa modelo de Unidades
    class Meta:
        model = Unidade
        fields = '__all__'
class UsuarioSerilizer(serializers.ModelSerializer): # Serializa modelo de Usuários (typo mantido)
    class Meta:
        model = Usuario
        fields = '__all__'
class PacienteSerializer(serializers.ModelSerializer): # Serializa modelo de Pacientes
    class Meta:
        model = Paciente
        fields = '__all__'


class NotificacaoSerializer(serializers.ModelSerializer): # Serializa notificações gerais
    class Meta:
        model = Notificacao
        fields = '__all__'
class NotificacaoBaseSerializer(serializers.ModelSerializer): # Serializa base de notificações
    class Meta:
        model = NotificacaoBase
        fields = '__all__'
class NotificacaoAidsSerializer(serializers.ModelSerializer): # Serializa notificações de Aids
    class Meta:
        model = NotificacaoAids
        fields = '__all__'
class NotificacaoBotulismoSerializer(serializers.ModelSerializer): # Serializa notificações de Botulismo
    class Meta:
        model = NotificacaoBotulismo
        fields = '__all__'
class NotificacaoEpizootiaSerializer(serializers.ModelSerializer): # Serializa notificações de Epizootia
    class Meta:
        model = NotificacaoEpizootia
        fields = '__all__'
class NotificacaoEsquistossomoseSerializer(serializers.ModelSerializer): # Serializa notificações de Esquistossomose
    class Meta:
        model = NotificacaoEsquistossomose
        fields = '__all__'
class NotificacaoFebreAmarelaSerializer(serializers.ModelSerializer): # Serializa notificações de Febre Amarela
    class Meta:
        model = NotificacaoFebreAmarela
        fields = '__all__'
class NotificacaoDengueChikungunyaSerializer(serializers.ModelSerializer): # Serializa notificações de Dengue/Chikungunya
    class Meta:
        model = NotificacaoDengueChikungunya
        fields = '__all__'
class NotificacaoAnimalPeconhentoSerializer(serializers.ModelSerializer): # Serializa notificações de Animais Peçonhentos
    class Meta:
        model = NotificacaoAnimalPeconhento
        fields = '__all__' #
class NotificacaoAntiRabicoSerializer(serializers.ModelSerializer): # Serializa notificações Antirrábicas
    class Meta:
        model = NotificacaoAntiRabico
        fields = '__all__'
class NotificacaoColeraSerializer(serializers.ModelSerializer): # Serializa notificações de Cólera
    class Meta:
        model = NotificacaoColera
        fields = '__all__'
class NotificacaoChikungunyaSerializer(serializers.ModelSerializer): # Serializa notificações de Chikungunya
    class Meta:
        model = NotificacaoChikungunya
        fields = '__all__'
class NotificacaoCoquelucheSerializer(serializers.ModelSerializer): # Serializa notificações de Coqueluche
    class Meta:
        model = NotificacaoCoqueluche
        fields = '__all__'