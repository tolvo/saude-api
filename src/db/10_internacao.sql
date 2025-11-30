CREATE TABLE IF NOT EXISTS INTERNACAO(
    data_entrada DATE,
    cidadao VARCHAR(11),
    cnes VARCHAR(11),
    data_alta DATE,
    motivo VARCHAR(100),
    ala_hospitalar VARCHAR(20),
    CONSTRAINT PK_INTERNACAO PRIMARY KEY (data_entrada, cidadao, cnes),
    CONSTRAINT FK_INTERNACAO_1 FOREIGN KEY (cidadao)
                REFERENCES CIDADAO(cpf)
                ON DELETE CASCADE,
    CONSTRAINT FK_INTERNACAO_2 FOREIGN KEY (cnes)
                REFERENCES HOSPITAL(cnes)
                ON DELETE CASCADE
);

-- Dados de exemplo
INSERT INTO INTERNACAO (data_entrada, cidadao, cnes, data_alta, motivo, ala_hospitalar) VALUES 
('2024-01-15', '12345678901', '3000001', '2024-01-20', 'Cirurgia cardíaca', 'UTI'),
('2024-02-10', '23456789012', '3000002', '2024-02-15', 'Pneumonia', 'Clínica'),
('2024-03-05', '34567890123', '3000001', '2024-03-12', 'Fratura de fêmur', 'Ortopedia'),
('2024-04-20', '45678901234', '3000003', NULL, 'Parto normal', 'Maternidade');

