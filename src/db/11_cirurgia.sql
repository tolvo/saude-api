CREATE TABLE IF NOT EXISTS CIRURGIA(
    data_realizacao DATE,
    cidadao VARCHAR(11),
    cnes VARCHAR(10),
    duracao TIME,
    observacao VARCHAR(300),
    cuidados_posteriores VARCHAR(100),
    nome_procedimento VARCHAR(50),
    CONSTRAINT PK_CIRURGIA PRIMARY KEY (data_realizacao, cidadao, cnes),
    CONSTRAINT FK_CIRURGIA_1 FOREIGN KEY (cidadao)
                REFERENCES CIDADAO(cpf)
                ON DELETE CASCADE,
    CONSTRAINT FK_CIRURGIA_2 FOREIGN KEY (cnes)
                REFERENCES HOSPITAL(cnes)
                ON DELETE CASCADE

);


