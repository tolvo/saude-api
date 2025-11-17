CREATE TABLE IF NOT EXISTS CIDADAO (
    cpf VARCHAR(20),
    nome VARCHAR(100),
    data_nasc DATE,
    sexo VARCHAR(5),
    endereco VARCHAR(100),
    telefone INTEGER,
    tipo_sanguineo VARCHAR(5),
    CONSTRAINT PK_CIDADAO PRIMARY KEY(cpf)
);


INSERT INTO CIDADAO (cpf, nome, data_nasc, sexo, endereco, telefone, tipo_sanguineo) VALUES ('1', 'Teste', '01/01/2003', 'M', 'Rua teste, 1112, Teste/TESTE', 1111111111,'A+');
INSERT INTO CIDADAO (cpf, nome, data_nasc, sexo, endereco, telefone, tipo_sanguineo) VALUES ('2', 'Teste2', '01/01/2004', 'M', 'Rua teste2, 1112, Teste/TESTE', 1111111111,'A+');