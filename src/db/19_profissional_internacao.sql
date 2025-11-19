CREATE TABLE IF NOT EXISTS PROFISSIONAL_INTERNACAO(
    data_internacao DATE,
    cidadao VARCHAR(11),
    cnes VARCHAR(10),
    data_visita DATE,
    horario VARCHAR(10),
    visita VARCHAR(15),
    profissional VARCHAR(11),
    procedimento_realizado VARCHAR(50),
    situacao_paciente VARCHAR(50),
    CONSTRAINT PK_PROFISSIONAL_INTERNACAO PRIMARY KEY(data_internacao, cidadao, cnes, data_visita, profissional),
    CONSTRAINT FK_PROFISSIONAL_INTERNACAO_1 FOREIGN KEY(data_internacao, cidadao, cnes)
                REFERENCES INTERNACAO(data_entrada, cidadao, cnes)
                ON DELETE CASCADE,
    CONSTRAINT FK_PROFISSIONAL_INTERNACAO_2 FOREIGN KEY(profissional)
                REFERENCES PROFISSIONAL(cpf)
                ON DELETE CASCADE


);
