CREATE TABLE VACINACAO(
    dose INTEGER,
    cidadao VARCHAR(11),
    vacina_cod INTEGER,
    vacina_lote INTEGER,
    ubs VARCHAR(10),
    data DATE NOT NULL,
    enfermeiro VARCHAR(11) NOT NULL,
    CONSTRAINT PK_VACINACAO PRIMARY KEY (dose, cidadao, vacina_cod, vacina_lote),
    CONSTRAINT FK_VACINACAO_1 FOREIGN KEY (cidadao)
                REFERENCES CIDADAO(cpf)
                ON DELETE CASCADE,
    CONSTRAINT FK_VACINACAO_2 FOREIGN KEY (vacina_cod, vacina_lote)
                REFERENCES VACINA(cod, lote)
                ON DELETE CASCADE,
    CONSTRAINT FK_VACINACAO_3 FOREIGN KEY (ubs)
                REFERENCES UNIDADE_BASICA_SAUDE(cnes)
                ON DELETE CASCADE,
    CONSTRAINT FK_VACINACAO_4 FOREIGN KEY (enfermeiro)
                REFERENCES ENFERMEIRO(cpf)
                ON DELETE CASCADE


);


