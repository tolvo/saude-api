CREATE TABLE IF NOT EXISTS cidadao (
    CPF VARCHAR(20) PRIMARY KEY,
    Nome VARCHAR(100),
    Data_nasc VARCHAR(100),
    Sexo VARCHAR(5),
    Endereco VARCHAR(100),
    Telefone INTEGER,
    Tipo_sanguineo VARCHAR(5)
);


INSERT INTO cidadao (CPF, Nome, Data_nasc, Sexo, Endereco, Telefone, Tipo_sanguineo) VALUES ('123', 'Teste', '01/01/2003', 'M', 'Rua teste, 1112, Teste/TESTE', 1111111111,'A+');