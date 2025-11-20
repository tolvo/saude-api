CREATE TABLE IF NOT EXISTS MEDICO(
    cpf VARCHAR(11),
    crm INTEGER,
    especialidade VARCHAR(20),
    CONSTRAINT PK_MEDICO PRIMARY KEY (cpf),
    CONSTRAINT FK_MEDICO FOREIGN KEY (cpf)
                REFERENCES PROFISSIONAL(cpf)
                ON DELETE CASCADE,
    UNIQUE(crm)

);

-- Dados de exemplo
INSERT INTO MEDICO (cpf, crm, especialidade) VALUES 
('11111111111', 123456, 'Cardiologia'),
('22222222222', 234567, 'Pediatria'),
('33333333333', 345678, 'Ortopedia');
