# Prontuário Eletrônico do Cidadão (PEC)

Sistema de banco de dados para gestão de dados urbanos em cidades inteligentes, focado na saúde.

## Estrutura do Projeto

- `src/back/`: Código-fonte do back-end em Python Flask.
- `src/front/`: Código-fonte do front-end em Python Flask.
- `src/db/`: Scripts SQL para criação e povoamento do banco de dados PostgreSQL.
- `docker-compose.yml`: Configuração do Docker para orquestração dos containers.

### Esquema do Banco de Dados

O esquema do banco de dados está dividido em arquvos SQL localizados em `src/db/`, tais como:

- `01_cidadao.sql`: Tabela de cidadãos.
- `02_alergias.sql`: Tabela de alergias.
- `03_unidade_saude.sql`: Tabela de unidades de saúde.

### Dados Iniciais

Cada arquivo contém a definição da tabela e os dados iniciais para povoamento.

### Consultas SQL

As consultas SQL estão localizadas em `src/back/queries/`, organizadas por funcionalidade, como:

- `cidadao_queries.py`:
  - obter dados básicos do cidadão
  - obter alergias
  - obter consultas
  - obter exames realizados
  - obter receitas prescritas
  - obter vacinações
  - obter cirurgias realizadas
  - obter internações
- `consultas_queries.py`:
  - histórico clínico completo
  - vacinas em atraso
  - consultas por unidade de saúde
  - pacientes com prescrição
  - cidadãos com todas as vacinas

## Como Executar

1. Construir e executar os containers:

   ```bash
   docker-compose up --build
   ```

2. O back-end estará em http://localhost:5000
3. O front-end estará em http://localhost:8080

## Tecnologias

- PostgreSQL
- Python Flask
- Docker

## Segurança

- Uso de prepared statements para evitar SQL Injection.
- Transações para consistência de dados.
