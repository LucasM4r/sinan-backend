# backend-sinan

Backend Django configurado para usar **PostgreSQL**.

## Configuracao rapida

1. Instale as dependencias:
   - `pip install -r requirements.txt`
2. Copie `.env.example` para `.env` e ajuste as credenciais do PostgreSQL.
3. Rode as migracoes:
   - `python manage.py migrate`
4. Inicie a aplicacao:
   - `python manage.py runserver`
