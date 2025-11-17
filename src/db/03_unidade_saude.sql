CREATE TABLE IF NOT EXISTS UNIDADE_SAUDE(
    cnes VARCHAR(10),
    nome VARCHAR(50),
    endereco VARCHAR(100),
    tipo VARCHAR(15),
    horario_funcionamento VARCHAR(10),
    CONSTRAINT PK_UNIDADE_SAUDE PRIMARY KEY (cnes)

);


