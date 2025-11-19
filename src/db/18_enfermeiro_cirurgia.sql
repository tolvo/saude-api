CREATE TABLE IF NOT EXISTS ENFERMEIRO_CIRURGIA(
    data_realiza DATE,
    cidadao VARCHAR(11),
    cnes VARCHAR(10),
    enfermeiro VARCHAR(11),
    CONSTRAINT PK_ENFERMEIRO_CIRURGIA PRIMARY KEY(data_realiza, cidadao,cnes,enfermeiro),
    CONSTRAINT FK_ENFERMEIRO_CIRURGIA_1 FOREIGN KEY(cidadao)
                REFERENCES CIDADAO(cpf)
                ON DELETE CASCADE,
    CONSTRAINT FK_ENFERMEIRO_CIRURGIA_2 FOREIGN KEY(cnes)
                REFERENCES HOSPITAL(cnes)
                ON DELETE CASCADE,

    CONSTRAINT FK_ENFERMEIRO_CIRURGIA_3 FOREIGN KEY(enfermeiro)
                REFERENCES enfermeiro(cpf)
                ON DELETE CASCADE


);