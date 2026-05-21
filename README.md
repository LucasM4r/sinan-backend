# BACKEND SINAN

## Sobre o projeto

O Sistema de Informação de Agravos de Notificação (SINAN) é uma plataforma essencial para a vigilância epidemiológica no Brasil, permitindo o registro e o monitoramento sistemático de doenças e agravos de notificação compulsória.

Este projeto entrega um backend robusto e escalável em **Django 6**, focado em garantir a integridade histórica dos dados de saúde pública.

### Características principais

- **Integridade Histórica:** Captura dos dados do paciente (CPF, endereço, escolaridade, etc.) no momento do registro da notificação através de classes de `NotificacaoBase`, garantindo um "snapshot" histórico imutável.
- **Segurança de Dados:** Protege a notificação epidemiológica original mesmo quando o cadastro mestre do paciente é atualizado posteriormente, preservando a fotografia dos dados conforme estavam no momento do atendimento.
- **API REST:** Desenvolvido como uma API RESTful para integração com frontend em TypeScript, com comunicação via JSON e endpoints bem definidos.

### Tecnologias 

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![postgresql](https://img.shields.io/badge/postgresql-4169E1?style=for-the-badge&logo=postgresql&logoColor=white) 
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Json](https://img.shields.io/badge/json-000000?style=for-the-badge&logo=json&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Estrutura do Projeto

```
backend-sinan/
├── config/              # Configurações do projeto Django
│   ├── settings.py      # Configurações principais (BD, apps instalados, middleware)
│   ├── urls.py          # Rotas principais
│   ├── asgi.py          # Configuração ASGI
│   └── wsgi.py          # Configuração WSGI
├── app/                 # Aplicação principal
│   ├── models.py        # Modelos de dados (Unidade, Usuario, Paciente, Notificacao, etc.)
│   ├── views.py         # Views (endpoints)
│   ├── urls.py          # Rotas da aplicação
│   ├── admin.py         # Configurações do Django Admin
│   └── migrations/      # Histórico de migrações do banco
├── templates/           # Templates HTML
├── static/              # Arquivos estáticos (CSS, JS, imagens)
├── manage.py            # Script de gerenciamento Django
└── requirements.txt     # Dependências do projeto
```

## Como começar

### Pré-requisitos

Antes de iniciar, certifique-se de ter instalado em sua máquina:
* **Python 3.12+**
* **PostgreSQL** (com um banco de dados criado conforme as credenciais abaixo)

### Configuração do Ambiente

1. **Clone o repositório:**
   ```powershell
   git clone https://github.com/SINAN-UFSM/sinan-backend
   cd backend-sinan
   
2. **Crie um ambiente virual**
    ```powershell
    python -m venv venv
    .\venv\Scripts\activate
    ```
3. **Instale as dependências:**
   ```powershell
   pip install -r requirements.txt
   ```
### Configuração do Banco de Dados

O projeto utiliza variáveis de ambiente para configuração sensível. Crie um arquivo `.env` na raiz do projeto seguindo o modelo abaixo:

```env
DJANGO_SECRET_KEY=sua_chave_secreta
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
DJANGO_LANGUAGE_CODE=pt-br
DJANGO_TIME_ZONE=America/Sao_Paulo

POSTGRES_DB=backend_sinan
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432
```

### Como se conectar ao PostgreSQL

1. Certifique-se de que o serviço PostgreSQL esteja em execução na máquina local.
2. Crie o banco informado em `POSTGRES_DB` e confirme que o usuário possui permissão de acesso.
3. Verifique se `POSTGRES_HOST` e `POSTGRES_PORT` correspondem ao ambiente em que o banco está rodando.
4. Teste a conexão com as credenciais definidas no `.env` antes de iniciar o backend.
5. Após validar o acesso, execute as migrações e inicie a aplicação.

Conexão local padrão:

- host: `localhost`
- porta: `5432`
- banco: `sinan_web`
- usuário: `admin_sinanweb`
- senha: `2026sinan`
````sql
CREATE USER admin_sinanweb WITH PASSWORD '2026sinan';
CREATE DATABASE sinan_web OWNER admin_sinanweb;
GRANT ALL PRIVILEGES ON DATABASE sinan_web TO admin_sinanweb;
````
### Executando
1. **Aplique as migrações:**
   ```powershell
   python manage.py migrate
   ```
2. **Inicie o servidor de desenvolvimento:**
    ```powershell
    python manage.py runserver
    ```
  Acesse http://127.0.0.1:8000 para verificar se a aplicação está rodando.

## Rotas Principais
- Em desenvolvimento

## Scripts Úteis

```powershell
# Criar usuário administrador
python manage.py createsuperuser

# Criar novas migrações de modelos
python manage.py makemigrations

# Aplicar migrações ao banco
python manage.py migrate

# Iniciar servidor de desenvolvimento
python manage.py runserver

# Executar testes
python manage.py test

# Acessar shell Django interativo
python manage.py shell
```

## Observações Importantes

- O arquivo `.env` é carregado automaticamente via `python-dotenv` no `config/settings.py`
- O banco de dados PostgreSQL deve estar em execução antes de rodar o servidor
- Em desenvolvimento, `DEBUG=True` permite visualizar erros detalhados e recarrega automático
- Os dados do paciente são capturados como "snapshot" no momento da notificação para manter integridade histórica
- `MEDIA_ROOT` e `STATIC_ROOT` estão configurados para armazenamento local em desenvolvimento

## Modelos de Dados

O projeto implementa uma arquitetura que preserva dados históricos:

- **Unidade** - Unidades de saúde
- **Usuario** - Usuários do sistema
- **Paciente** - Cadastro mestre de pacientes
- **Notificacao** - Notificações gerais (status, datas, observações)
- **NotificacaoBase** - Classe abstrata que captura snapshot dos dados do paciente
- **NotificacaoAids**, **NotificacaoBotulismo**, **NotificacaoEpizootia**, etc. - Notificações específicas por tipo de agravo

## Contribuição

Para contribuir com melhorias, protocole um Pull Request descrevendo bem as alterações propostas.


