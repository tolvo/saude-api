CREATE TABLE RECEITA(
    medicamento varchar(30),
    data DATE,
    cidadao VARCHAR(11),
    medico VARCHAR(11),
    duracao VARCHAR(30),
    dosagem VARCHAR(30),
    CONSTRAINT PK_RECEITA PRIMARY KEY(medicamento, data, cidadao, medico),
    CONSTRAINT FK_RECEITA FOREIGN KEY(data, cidadao, medico)
                REFERENCES CONSULTA(data, cidadao, medico)
                ON DELETE CASCADE
);

-- Dados de exemplo
INSERT INTO RECEITA (medicamento, data, cidadao, medico, duracao, dosagem) VALUES 
('Atenolol', '2024-05-10', '12345678901', '11111111111', '30 dias', '50mg 1x ao dia'),
('Amoxicilina', '2024-05-15', '23456789012', '22222222222', '7 dias', '500mg 8/8h'),
('Ibuprofeno', '2024-05-20', '34567890123', '33333333333', '10 dias', '600mg 8/8h'),
('Ácido Fólico', '2024-06-01', '45678901234', '11111111111', '90 dias', '5mg 1x ao dia'),
('Dipirona', '2024-06-10', '56789012345', '22222222222', '5 dias', '500mg se dor');