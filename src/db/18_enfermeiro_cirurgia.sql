CREATE TABLE IF NOT EXISTS MEDICO_CIRURGIA(
    data_realiza DATE,
    cidadao VARCHAR(11),
    cnes VARCHAR(10),
    enfermeiro VARCHAR(11),
    CONSTRAINT PK_MEDICO_CIRURGIA PRIMARY KEY(data_realiza, cidadao,cnes,enfermeiro),
    CONSTRAINT FK_MEDICO_CIRURGIA_1 FOREIGN KEY(cidadao)
                REFERENCES CIDADAO(cpf)
                ON DELETE CASCADE,
    CONSTRAINT FK_MEDICO_CIRURGIA_2 FOREIGN KEY(cnes)
                REFERENCES HOSPITAL(cnes)
                ON DELETE CASCADE,

    CONSTRAINT FK_MEDICO_CIRURGIA_3 FOREIGN KEY(enfermeiro)
                REFERENCES enfermeiro(cpf)
                ON DELETE CASCADE


);