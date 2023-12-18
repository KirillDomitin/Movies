#!/bin/bash
# Создаем схему "content"
set -e
export PGPASSWORD=$POSTGRES_PASSWORD;
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    GRANT ALL PRIVILEGES ON DATABASE movies_database TO kirill;
  \connect movies_database kirill
  BEGIN;
    CREATE SCHEMA IF NOT EXISTS "content";
  COMMIT;
EOSQL