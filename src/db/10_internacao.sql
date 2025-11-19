CREATE TABLE IF NOT EXISTS INTERNACAO(
    data_entrada DATE,
    cidadao VARCHAR(11),
    cnes VARCHAR(10),
    data_alta DATE,
    motivo VARCHAR(100),
    ala_hospitalar VARCHAR(10),
    CONSTRAINT PK_INTERNACAO PRIMARY KEY (data_entrada, cidadao, cnes),
    CONSTRAINT FK_INTERNACAO_1 FOREIGN KEY (cidadao)
                REFERENCES CIDADAO(cpf)
                ON DELETE CASCADE,
    CONSTRAINT FK_INTERNACAO_2 FOREIGN KEY (cnes)
                REFERENCES HOSPITAL(cnes)
                ON DELETE CASCADE
);


