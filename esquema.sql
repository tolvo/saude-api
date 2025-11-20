-- Esquema SQL para o Prontuário Eletrônico do Cidadão (PEC)

-- Tabela Cidadão
CREATE TABLE IF NOT EXISTS cidadao (
    CPF VARCHAR(20) PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Data_nasc DATE NOT NULL,
    Sexo VARCHAR(10) CHECK (Sexo IN ('Masculino', 'Feminino', 'Outro')),
    Endereco VARCHAR(200),
    Telefone VARCHAR(20),
    Tipo_sanguineo VARCHAR(5) CHECK (Tipo_sanguineo IN ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'))
);

-- Tabela Alergia Cidadão (atributo multivalorado)
CREATE TABLE IF NOT EXISTS alergia_cidadao (
    CPF VARCHAR(20),
    Alergia VARCHAR(100),
    PRIMARY KEY (CPF, Alergia),
    FOREIGN KEY (CPF) REFERENCES cidadao(CPF) ON DELETE CASCADE
);

-- Tabela Unidade de Saúde
CREATE TABLE IF NOT EXISTS unidade_saude (
    CNES VARCHAR(20) PRIMARY KEY,
    Tipo VARCHAR(50) CHECK (Tipo IN ('Unidade Básica de Saúde', 'Hospital')),
    Nome VARCHAR(100) NOT NULL,
    Endereco VARCHAR(200),
    Horario_func VARCHAR(100)
);

-- Tabela Hospital (especialização)
CREATE TABLE IF NOT EXISTS hospital (
    CNES VARCHAR(20) PRIMARY KEY,
    Capacidade INTEGER,
    FOREIGN KEY (CNES) REFERENCES unidade_saude(CNES) ON DELETE CASCADE
);

-- Tabela Unidade Básica (especialização)
CREATE TABLE IF NOT EXISTS unidade_basica (
    CNES VARCHAR(20) PRIMARY KEY,
    FOREIGN KEY (CNES) REFERENCES unidade_saude(CNES) ON DELETE CASCADE
);

-- Tabela Profissional
CREATE TABLE IF NOT EXISTS profissional (
    CPF VARCHAR(20) PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Tipo VARCHAR(20) CHECK (Tipo IN ('Médico', 'Enfermeiro'))
);

-- Tabela Médico (especialização)
CREATE TABLE IF NOT EXISTS medico (
    CPF VARCHAR(20) PRIMARY KEY,
    CRM VARCHAR(20) NOT NULL,
    Especialidade VARCHAR(100),
    FOREIGN KEY (CPF) REFERENCES profissional(CPF) ON DELETE CASCADE
);

-- Tabela Enfermeiro (especialização)
CREATE TABLE IF NOT EXISTS enfermeiro (
    CPF VARCHAR(20) PRIMARY KEY,
    COREN VARCHAR(20) NOT NULL,
    FOREIGN KEY (CPF) REFERENCES profissional(CPF) ON DELETE CASCADE
);

-- Tabela Consulta (agregação)
CREATE TABLE IF NOT EXISTS consulta (
    CPF_cidadao VARCHAR(20),
    CPF_medico VARCHAR(20),
    Data_consulta DATE,
    CNES_unidade VARCHAR(20),
    Relatorio_medico TEXT,
    PRIMARY KEY (CPF_cidadao, CPF_medico, Data_consulta),
    FOREIGN KEY (CPF_cidadao) REFERENCES cidadao(CPF),
    FOREIGN KEY (CPF_medico) REFERENCES medico(CPF),
    FOREIGN KEY (CNES_unidade) REFERENCES unidade_saude(CNES)
);

-- Tabela Receita (entidade fraca)
CREATE TABLE IF NOT EXISTS receita (
    CPF_cidadao VARCHAR(20),
    CPF_medico VARCHAR(20),
    Data_consulta DATE,
    Medicamento VARCHAR(100),
    Dosagem VARCHAR(100),
    Duracao VARCHAR(50),
    PRIMARY KEY (CPF_cidadao, CPF_medico, Data_consulta, Medicamento),
    FOREIGN KEY (CPF_cidadao, CPF_medico, Data_consulta) REFERENCES consulta(CPF_cidadao, CPF_medico, Data_consulta) ON DELETE CASCADE
);

-- Tabela Exame (entidade fraca)
CREATE TABLE IF NOT EXISTS exame (
    CPF_cidadao VARCHAR(20),
    CPF_medico VARCHAR(20),
    Data_consulta DATE,
    Tipo_exame VARCHAR(100),
    Data_realizacao DATE,
    Local VARCHAR(100),
    Link_resultado VARCHAR(200),
    PRIMARY KEY (CPF_cidadao, CPF_medico, Data_consulta, Tipo_exame),
    FOREIGN KEY (CPF_cidadao, CPF_medico, Data_consulta) REFERENCES consulta(CPF_cidadao, CPF_medico, Data_consulta) ON DELETE CASCADE
);

-- Tabela Vacina
CREATE TABLE IF NOT EXISTS vacina (
    Lote VARCHAR(50),
    Cod_vacina VARCHAR(50),
    Nome VARCHAR(100) NOT NULL,
    Fabricante VARCHAR(100),
    Validade DATE,
    PRIMARY KEY (Lote, Cod_vacina)
);

-- Tabela Vacinação (relacionamento ternário)
CREATE TABLE IF NOT EXISTS vacinacao (
    CPF_cidadao VARCHAR(20),
    Lote_vacina VARCHAR(50),
    Cod_vacina VARCHAR(50),
    Dose INTEGER,
    Data_aplicacao DATE,
    CNES_unidade VARCHAR(20),
    CPF_enfermeiro VARCHAR(20),
    PRIMARY KEY (CPF_cidadao, Lote_vacina, Cod_vacina),
    FOREIGN KEY (CPF_cidadao) REFERENCES cidadao(CPF),
    FOREIGN KEY (Lote_vacina, Cod_vacina) REFERENCES vacina(Lote, Cod_vacina),
    FOREIGN KEY (CNES_unidade) REFERENCES unidade_basica(CNES),
    FOREIGN KEY (CPF_enfermeiro) REFERENCES enfermeiro(CPF)
);

-- Tabela Cirurgia
CREATE TABLE IF NOT EXISTS cirurgia (
    CPF_cidadao VARCHAR(20),
    CNES_hospital VARCHAR(20),
    Data_realizacao TIMESTAMP,
    Nome_procedimento VARCHAR(200),
    Duracao INTERVAL,
    Observacoes TEXT,
    Cuidados TEXT,
    PRIMARY KEY (CPF_cidadao, CNES_hospital, Data_realizacao),
    FOREIGN KEY (CPF_cidadao) REFERENCES cidadao(CPF),
    FOREIGN KEY (CNES_hospital) REFERENCES hospital(CNES)
);

-- Tabela Auxilia (N:N Cirurgia - Enfermeiro)
CREATE TABLE IF NOT EXISTS auxilia (
    CPF_enfermeiro VARCHAR(20),
    CPF_cidadao VARCHAR(20),
    CNES_hospital VARCHAR(20),
    Data_realizacao TIMESTAMP,
    PRIMARY KEY (CPF_enfermeiro, CPF_cidadao, CNES_hospital, Data_realizacao),
    FOREIGN KEY (CPF_enfermeiro) REFERENCES enfermeiro(CPF),
    FOREIGN KEY (CPF_cidadao, CNES_hospital, Data_realizacao) REFERENCES cirurgia(CPF_cidadao, CNES_hospital, Data_realizacao) ON DELETE CASCADE
);

-- Tabela Opera (N:N Cirurgia - Médico)
CREATE TABLE IF NOT EXISTS opera (
    CPF_medico VARCHAR(20),
    CPF_cidadao VARCHAR(20),
    CNES_hospital VARCHAR(20),
    Data_realizacao TIMESTAMP,
    PRIMARY KEY (CPF_medico, CPF_cidadao, CNES_hospital, Data_realizacao),
    FOREIGN KEY (CPF_medico) REFERENCES medico(CPF),
    FOREIGN KEY (CPF_cidadao, CNES_hospital, Data_realizacao) REFERENCES cirurgia(CPF_cidadao, CNES_hospital, Data_realizacao) ON DELETE CASCADE
);

-- Tabela Internação
CREATE TABLE IF NOT EXISTS internacao (
    CPF_cidadao VARCHAR(20),
    CNES_hospital VARCHAR(20),
    Data_entrada DATE,
    Data_alta DATE,
    Motivo VARCHAR(200),
    Ala VARCHAR(50),
    PRIMARY KEY (CPF_cidadao, CNES_hospital, Data_entrada),
    FOREIGN KEY (CPF_cidadao) REFERENCES cidadao(CPF),
    FOREIGN KEY (CNES_hospital) REFERENCES hospital(CNES),
    CHECK (Data_alta >= Data_entrada)
);

-- Tabela Atende (N:N Internação - Profissional)
CREATE TABLE IF NOT EXISTS atende (
    CPF_profissional VARCHAR(20),
    CPF_cidadao VARCHAR(20),
    CNES_hospital VARCHAR(20),
    Data_entrada DATE,
    PRIMARY KEY (CPF_profissional, CPF_cidadao, CNES_hospital, Data_entrada),
    FOREIGN KEY (CPF_profissional) REFERENCES profissional(CPF),
    FOREIGN KEY (CPF_cidadao, CNES_hospital, Data_entrada) REFERENCES internacao(CPF_cidadao, CNES_hospital, Data_entrada) ON DELETE CASCADE
);

-- Tabela Acompanhamento (agregação)
CREATE TABLE IF NOT EXISTS acompanhamento (
    CPF_profissional VARCHAR(20),
    CPF_cidadao VARCHAR(20),
    CNES_hospital VARCHAR(20),
    Data_entrada DATE,
    Data_hora_acompanhamento TIMESTAMP,
    Procedimentos TEXT,
    Condicao TEXT,
    PRIMARY KEY (CPF_profissional, CPF_cidadao, CNES_hospital, Data_entrada, Data_hora_acompanhamento),
    FOREIGN KEY (CPF_profissional, CPF_cidadao, CNES_hospital, Data_entrada) REFERENCES atende(CPF_profissional, CPF_cidadao, CNES_hospital, Data_entrada) ON DELETE CASCADE,
    CHECK (Data_hora_acompanhamento >= Data_entrada::timestamp AND (Data_alta IS NULL OR Data_hora_acompanhamento <= Data_alta::timestamp))
);

-- Tabela Atua (N:N Unidade - Profissional)
CREATE TABLE IF NOT EXISTS atua (
    CPF_profissional VARCHAR(20),
    CNES_unidade VARCHAR(20),
    PRIMARY KEY (CPF_profissional, CNES_unidade),
    FOREIGN KEY (CPF_profissional) REFERENCES profissional(CPF),
    FOREIGN KEY (CNES_unidade) REFERENCES unidade_saude(CNES)
);