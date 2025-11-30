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

-- Dados de exemplo
INSERT INTO EXAME (tipo, data, cidadao, medico, data_realiza, local, link) VALUES 
('Eletrocardiograma', '2024-05-10', '12345678901', '11111111111', '2024-05-12', 'Lab Centro', 'http://exames.com/123'),
('Hemograma', '2024-05-15', '23456789012', '22222222222', '2024-05-16', 'Lab São Paulo', 'http://exames.com/234'),
('Raio-X', '2024-05-20', '34567890123', '33333333333', '2024-05-21', 'Hospital São Paulo', 'http://exames.com/345'),
('Ultrassom', '2024-06-01', '45678901234', '11111111111', '2024-06-02', 'Clínica Mãe Bebê', 'http://exames.com/456');