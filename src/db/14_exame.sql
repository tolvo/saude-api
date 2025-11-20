CREATE TABLE EXAME(
    tipo varchar(30),
    data DATE,
    cidadao VARCHAR(11),
    medico VARCHAR(11),
    data_realiza DATE,
    local VARCHAR(30),
    link VARCHAR(150),
    CONSTRAINT PK_EXAME PRIMARY KEY(tipo, data, cidadao, medico),
    CONSTRAINT FK_EXAME FOREIGN KEY(data, cidadao, medico)
                REFERENCES CONSULTA(data, cidadao, medico)
                ON DELETE CASCADE
);