CREATE TABLE IF NOT EXISTS ALERGIA(
    cpf VARCHAR(20),
    alergia VARCHAR(50),
    CONSTRAINT PK_ALERGIA PRIMARY KEY (cpf, alergia),
    CONSTRAINT FK_ALERGIA FOREIGN KEY (cpf) 
                REFERENCES CIDADAO
                ON DELETE CASCADE
);

-- Dados de exemplo
INSERT INTO ALERGIA (cpf, alergia) VALUES 
('12345678901', 'Penicilina'),
('12345678901', 'Dipirona'),
('23456789012', 'Lactose'),
('34567890123', 'Poeira'),
('45678901234', 'Ácaro');