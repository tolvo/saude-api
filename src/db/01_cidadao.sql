CREATE TABLE IF NOT EXISTS CIDADAO (
    cpf VARCHAR(11),
    nome VARCHAR(100) NOT NULL,
    data_nasc DATE NOT NULL,
    sexo VARCHAR(5) NOT NULL,
    endereco VARCHAR(100),
    telefone VARCHAR(15),
    tipo_sanguineo VARCHAR(5),
    CONSTRAINT PK_CIDADAO PRIMARY KEY(cpf)
);


-- Dados de exemplo
INSERT INTO CIDADAO (cpf, nome, data_nasc, sexo, endereco, telefone, tipo_sanguineo) VALUES 
('12345678901', 'João Silva Santos', '1985-03-15', 'M', 'Rua das Flores, 123, São Paulo/SP', '11987654321', 'A+'),
('23456789012', 'Maria Oliveira Costa', '1990-07-22', 'F', 'Av. Paulista, 1000, São Paulo/SP', '11976543210', 'O-'),
('34567890123', 'Pedro Souza Lima', '1978-11-30', 'M', 'Rua Augusta, 456, São Paulo/SP', '11965432109', 'B+'),
('45678901234', 'Ana Paula Santos', '1995-01-08', 'F', 'Rua Consolação, 789, São Paulo/SP', '11954321098', 'AB+'),
('56789012345', 'Carlos Eduardo Alves', '1982-09-12', 'M', 'Av. Rebouças, 321, São Paulo/SP', '11943210987', 'O+');