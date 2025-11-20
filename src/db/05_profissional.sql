CREATE TABLE IF NOT EXISTS PROFISSIONAL(
    cpf VARCHAR(11),
    nome VARCHAR(30),
    tipo VARCHAR(10),
    CONSTRAINT PK_PROFISSIONAL PRIMARY KEY(cpf),
    CONSTRAINT TIPO_PROFISSIONAL CHECK (lower(tipo) IN ('enfermeiro', 'medico'))

);

-- Dados de exemplo
INSERT INTO PROFISSIONAL (cpf, nome, tipo) VALUES 
('11111111111', 'Dr. Roberto Ferreira', 'medico'),
('22222222222', 'Dra. Juliana Mendes', 'medico'),
('33333333333', 'Dr. Fernando Costa', 'medico'),
('44444444444', 'Enf. Carla Rodrigues', 'enfermeiro'),
('55555555555', 'Enf. Paulo Henrique', 'enfermeiro');
