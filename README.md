# backend-sinan

Backend inicial do SINAN desenvolvido com Django 6 e PostgreSQL, com configuração baseada em variáveis de ambiente.

## Desenvolvimento

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abra `http://127.0.0.1:8000`.

## Banco de dados PostgreSQL

Por padrão, a aplicação usa PostgreSQL via `config/settings.py`.

Configure o arquivo `.env` na raiz do projeto:

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

## Rotas iniciais

- `/health/`
- `/admin/`

## Estrutura do projeto

- `config/`: configuração do projeto Django
- `app/`: aplicação principal com modelos, views e rotas
- `templates/`: templates da aplicação
- `static/`: arquivos estáticos

## Scripts

```powershell
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py test
```

## Observações

- O arquivo `.env` é carregado automaticamente com `python-dotenv`.
- O endpoint `GET /health/` retorna o status da aplicação.
- Em desenvolvimento, `MEDIA_ROOT` e `STATIC_ROOT` estão configurados no projeto.

