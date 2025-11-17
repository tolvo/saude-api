CREATE TABLE RECEITA(
    medicamento varchar(30),
    data DATE,
    cidadao VARCHAR(11),
    medico VARCHAR(11),
    duracao VARCHAR(30),
    dosagem VARCHAR(30),
    CONSTRAINT PK_RECEITA PRIMARY KEY(medicamento, data, cidadao, medico),
    CONSTRAINT FK_RECEITA FOREIGN KEY(data, cidadao, medico)
                REFERENCES CONSULTA(data, cidadao, medico)
                ON DELETE CASCADE
);