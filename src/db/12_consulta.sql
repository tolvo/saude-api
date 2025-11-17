CREATE TABLE CONSULTA(
    data DATE,
    cidadao VARCHAR(11),
    medico VARCHAR(20),
    unidade_saude VARCHAR(10) NOT NULL,
    relatorio VARCHAR(20),
    CONSTRAINT PK_CONSULTA PRIMARY KEY(data, cidadao, medico),
    CONSTRAINT FK_CONSULTA_1 FOREIGN KEY(cidadao)
                REFERENCES CIDADAO(cpf)
                ON DELETE CASCADE,
    CONSTRAINT FK_CONSULTA_2 FOREIGN KEY(medico)
                REFERENCES MEDICO(cpf)
                ON DELETE CASCADE,
    CONSTRAINT FK_CONSULTA_3 FOREIGN KEY (unidade_saude)
                REFERENCES UNIDADE_SAUDE(cnes)
                ON DELETE CASCADE

);


