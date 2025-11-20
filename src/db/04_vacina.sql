CREATE TABLE IF NOT EXISTS VACINA (
    cod INTEGER,
    lote INTEGER,
    nome_popular VARCHAR(29),
    fabricante VARCHAR(30),
    validade DATE,
    CONSTRAINT PK_VACINA PRIMARY KEY (cod, lote)

);

