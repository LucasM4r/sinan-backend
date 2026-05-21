from django.db import models


# --- CADASTRO MESTRE (Fonte da Verdade) ---

class Unidade(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha_hash = models.CharField(max_length=255)
    funcao = models.CharField(max_length=100)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)


class Paciente(models.Model):
    # Dados imutáveis e de referência
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    cidade_nascimento = models.CharField(max_length=100)
    cartao_sus = models.CharField(max_length=20)
    raca_cor = models.CharField(max_length=50)

    # Dados mutáveis (pode ser atualizado no cadastro principal)
    nome = models.CharField(max_length=255)
    sexo = models.CharField(max_length=50)
    escolaridade = models.CharField(max_length=100)
    endereco_atual = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.cpf})"

class Notificacao(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)  # ex: "rascunho", "publicado"
    slug_tipo_notificacao = models.CharField(max_length=100)
    data_notificacao = models.DateField()
    data_ocorrencia = models.DateField()
    observacoes = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)


class NotificacaoBase(models.Model):
    """
    Esta classe guarda os dados capturados NO MOMENTO da notificação.
    Mesmo os imutáveis são copiados aqui para 'congelar' a fotografia.
    """
    notificacao = models.OneToOneField(Notificacao, primary_key=True, on_delete=models.CASCADE)

    # Snapshot dos Dados Imutáveis (para registro histórico)
    cpf_snapshot = models.CharField(max_length=14)
    data_nascimento_snapshot = models.DateField()
    cidade_nascimento_snapshot = models.CharField(max_length=100)
    cartao_sus_snapshot = models.CharField(max_length=20)
    raca_cor_snapshot = models.CharField(max_length=50)

    # Snapshot dos Dados Mutáveis (capturados no momento do registro)
    nome_snapshot = models.CharField(max_length=255)
    sexo_snapshot = models.CharField(max_length=50)
    escolaridade_snapshot = models.CharField(max_length=100)
    endereco_snapshot = models.TextField()

    class Meta:
        abstract = True

class NotificacaoAids(NotificacaoBase):
    transmissao_vertical = models.CharField(max_length=100)
    exposicao_sexual = models.CharField(max_length=100)
    uso_drogas_injetaveis = models.CharField(max_length=100)
    resultado_exame_triagem = models.CharField(max_length=100)
    desfecho_saude = models.CharField(max_length=100)
    tratamento_realizado = models.TextField()

class NotificacaoBotulismo(NotificacaoBase):
    dt_primeiro_atendimento = models.DateField()
    st_ocorreu_hospitalizacao = models.CharField(max_length=50)
    st_sintoma_febre = models.CharField(max_length=50)
    st_sintoma_visao_turva = models.CharField(max_length=50)
    st_exame_ptose = models.CharField(max_length=50)
    fonte_transmissao_alimentar = models.CharField(max_length=100)
    st_tratamento_soro_antibotulinico = models.CharField(max_length=50)
    tp_classificacao_final = models.CharField(max_length=100)

class NotificacaoEpizootia(NotificacaoBase):
    dt_inicio_epizootia = models.DateField()
    ds_fonte_informacao = models.CharField(max_length=255)
    uf_ocorrencia = models.CharField(max_length=2)
    tp_zona = models.CharField(max_length=50)
    tp_animal = models.CharField(max_length=50)
    nu_animais_mortos = models.IntegerField()
    tp_suspeita_1 = models.CharField(max_length=100)
    st_resultado_laboratorio = models.CharField(max_length=100)

class NotificacaoEsquistossomose(NotificacaoBase):
    dt_coproscopia = models.DateField()
    st_analise_quantitativa = models.CharField(max_length=100)
    st_tratamento_realizado = models.CharField(max_length=100)
    tp_forma_clinica = models.CharField(max_length=100)
    tp_evolucao_caso = models.CharField(max_length=100)

class NotificacaoFebreAmarela(NotificacaoBase):
    st_vacinado_febre_amarela = models.CharField(max_length=50)
    st_sindrome_hemorragica = models.CharField(max_length=50)
    st_disfuncao_renal = models.CharField(max_length=50)
    ds_tgo_ast = models.CharField(max_length=100)
    st_classificacao_final = models.CharField(max_length=100)

class NotificacaoDengueChikungunya(NotificacaoBase):
    st_febre = models.CharField(max_length=50)
    st_artralgia_intensa = models.CharField(max_length=50)
    st_resultado_chik_s1 = models.CharField(max_length=50)
    st_resultado_ns1 = models.CharField(max_length=50)
    tp_classificacao = models.CharField(max_length=100)
    st_choque = models.CharField(max_length=50)

class NotificacaoAnimalPeconhento(NotificacaoBase):
    tipo_acidente = models.CharField(max_length=100)
    local_acidente = models.CharField(max_length=100)
    antiveneno_administrado = models.CharField(max_length=50)
    ampolas_antiveneno = models.IntegerField()
    classificacao_caso = models.CharField(max_length=100)

class NotificacaoAntiRabico(NotificacaoBase):
    st_tipo_exposicao = models.CharField(max_length=100)
    st_tipo_animal = models.CharField(max_length=100)
    st_observacao_animal = models.CharField(max_length=100)
    st_profilaxia_pos_exposicao = models.CharField(max_length=100)

class NotificacaoColera(NotificacaoBase):
    st_nivel_desidratacao = models.CharField(max_length=100)
    st_hospitalizacao = models.CharField(max_length=50)
    st_resultado_cultura_fezes = models.CharField(max_length=100)
    st_fonte_agua = models.CharField(max_length=100)

class NotificacaoChikungunya(NotificacaoBase):
    st_febre = models.CharField(max_length=50)
    st_dor_articular = models.CharField(max_length=50)
    st_exantema_cutaneo = models.CharField(max_length=50)
    st_resultado_exame_lab = models.CharField(max_length=100)
    st_hospitalizacao = models.CharField(max_length=50)

class NotificacaoCoqueluche(NotificacaoBase):
    st_duracao_tosse_semanas = models.IntegerField()
    st_status_vacinacao = models.CharField(max_length=100)
    st_som_guincho = models.CharField(max_length=50)
    st_apneia = models.CharField(max_length=50)
    st_confirmacao_lab = models.CharField(max_length=100)