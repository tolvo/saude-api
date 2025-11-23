# Prontuário Eletrônico do Cidadão (PEC)

Sistema de banco de dados para gestão de dados urbanos em cidades inteligentes, focado na saúde.

## Estrutura do Projeto

- `esquema.sql`: Script para criação das tabelas do banco de dados.
- `dados.sql`: Script para inserção de dados iniciais.
- `consultas.sql`: Consultas SQL complexas implementadas.
- `src/back/`: Back-end em Flask (Python) com API REST.
- `src/front/`: Front-end simples em Flask com HTML.
- `src/db/`: Configuração do PostgreSQL via Docker.

## Como Executar

1. Construir e executar os containers:

   ```bash
   docker-compose up --build
   ```

2. O back-end estará em http://localhost:5000
3. O front-end estará em http://localhost:8080

## Funcionalidades

### Busca de Cidadão 🔍 DESTAQUE

- **Busca Completa por CPF**: Retorna TODAS as informações do cidadão
  - Dados básicos (nome, CPF, data de nascimento, sexo, tipo sanguíneo, etc.)
  - Alergias registradas
  - Histórico de consultas médicas
  - Exames realizados
  - Receitas prescritas
  - Vacinações recebidas
  - Cirurgias realizadas
  - Internações (em andamento e concluídas)
- Interface visual intuitiva com cards organizados
- Informações formatadas e fáceis de ler

### Cadastro (CRUD)

- Cidadão e Alergias
- Profissional de Saúde (Médico/Enfermeiro)
- Unidade de Saúde (Hospital/Unidade Básica)
- Consulta, Exames e Receitas
- Internação e Cirurgia
- Vacinação e Vacinas
- Formulários inteligentes com validação (datas, selects, placeholders)

### Consultas Complexas

- **Histórico Clínico Completo** de um Cidadão (com consultas, exames, receitas, vacinações, cirurgias e internações)
- **Vacinas em Atraso** por faixa etária
- **Consultas por Unidade de Saúde** em um período específico
- **Pacientes com Prescrição** de determinado medicamento
- **Cidadãos com Todas as Vacinas** (Divisão Relacional)

## Tecnologias

- PostgreSQL
- Python Flask
- Docker

## Segurança

- Uso de prepared statements para evitar SQL Injection.
- Transações para consistência de dados.
