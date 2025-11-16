FROM postgres:15

# Variáveis padrão
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=admin
ENV POSTGRES_DB=meubanco

COPY ./*.sql /docker-entrypoint-initdb.d/