# Preparação de deploy do Rumix

Esta configuração mantém o desenvolvimento local com SQLite quando as variáveis
POSTGRES_DB e POSTGRES_USER não estão definidas. O Docker Compose fornece essas
variáveis e usa PostgreSQL.

## Antes de subir para produção

1. Faça backup de db.sqlite3 e da pasta media/ em local seguro.
2. Nunca compartilhe nem versione .env, backups do banco ou credenciais.
3. Copie .env.example para .env e gere uma SECRET_KEY exclusiva:
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
4. Defina SECRET_KEY, POSTGRES_PASSWORD, ALLOWED_HOSTS e
   CSRF_TRUSTED_ORIGINS com os valores reais do domínio.
5. Confirme que o provedor mantém volumes persistentes para PostgreSQL e media.
6. Teste a migração em uma cópia do banco antes de apontar o domínio público.

## Teste local com Docker

Com Docker instalado e o .env preenchido:

    docker compose config
    docker compose up --build

O entrypoint existente executa migrate e collectstatic ao iniciar o container web.

## Migração de dados SQLite para PostgreSQL

Não rode a migração diretamente no único banco com dados. Preserve uma cópia
intocada do SQLite e faça o teste em uma instância PostgreSQL separada.

Uma estratégia Django possível é:

1. No ambiente local, com o SQLite original e migrations aplicadas:
   python manage.py dumpdata --natural-foreign --natural-primary --exclude contenttypes --exclude auth.permission -o rumix-data.json
2. No ambiente de teste PostgreSQL, aplique as migrations:
   python manage.py migrate
3. Carregue os dados exportados:
   python manage.py loaddata rumix-data.json
4. Valide login, usuários, relações, cadastros, imagens e fluxos principais.

A exportação acima é um roteiro inicial, não uma garantia de migração completa:
modelos com dependências especiais, arquivos enviados e dados de apps de terceiros
podem exigir tratamento adicional. Não apague nem substitua o SQLite até concluir
a validação e manter backups restauráveis.

## Observações

- O armazenamento de media/ precisa ser persistente; o volume do Compose é local
  ao host e não substitui um serviço de arquivos persistentes em plataformas gerenciadas.
- O Nginx deste projeto atende HTTP na porta 80. Em hospedagens com HTTPS terminado
  em proxy externo, configure corretamente os hosts e origens confiáveis.
- Revise a checklist de deploy do Django antes da publicação final.
