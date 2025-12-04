CREATE TABLE IF NOT EXISTS UNIDADE_SAUDE(
    cnes VARCHAR(10),
    nome VARCHAR(50) NOT NULL,
    endereco VARCHAR(100),
    tipo VARCHAR(15),
    horario_funcionamento VARCHAR(20),
    CONSTRAINT PK_UNIDADE_SAUDE PRIMARY KEY (cnes)

);

-- Dados de exemplo
INSERT INTO UNIDADE_SAUDE (cnes, nome, endereco, tipo, horario_funcionamento) VALUES 
('2000001', 'UBS Vila Mariana', 'Rua Domingos de Morais, 2000, São Paulo/SP', 'UBS', '08:00-17:00'),
('2000002', 'UBS Jardim Paulista', 'Av. Brigadeiro Luís Antônio, 3000, São Paulo/SP', 'UBS', '07:00-19:00'),
('3000001', 'Hospital São Paulo', 'Rua Napoleão de Barros, 715, São Paulo/SP', 'Hospital', '24h'),
('3000002', 'Hospital das Clínicas', 'Av. Dr. Enéas de Carvalho Aguiar, 255, São Paulo/SP', 'Hospital', '24h'),
('3000003', 'Hospital Santa Cruz', 'Rua Santa Cruz, 398, São Paulo/SP', 'Hospital', '24h');

