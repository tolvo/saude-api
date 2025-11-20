CREATE TABLE CONSULTA(
    data DATE,
    cidadao VARCHAR(11),
    medico VARCHAR(20),
    unidade_saude VARCHAR(10) NOT NULL,
    relatorio VARCHAR(20),
    CONSTRAINT PK_CONSULTA PRIMARY KEY(data, cidadao, medico),
    CONSTRAINT FK_CONSULTA_1 FOREIGN KEY(cidadao)
                REFERENCES CIDADAO(cpf)
                ON DELETE CASCADE,
    CONSTRAINT FK_CONSULTA_2 FOREIGN KEY(medico)
                REFERENCES MEDICO(cpf)
                ON DELETE CASCADE,
    CONSTRAINT FK_CONSULTA_3 FOREIGN KEY (unidade_saude)
                REFERENCES UNIDADE_SAUDE(cnes)
                ON DELETE CASCADE

);

-- Dados de exemplo
INSERT INTO CONSULTA (data, cidadao, medico, unidade_saude, relatorio) VALUES 
('2024-05-10', '12345678901', '11111111111', '2000001', 'Consulta de rotina'),
('2024-05-15', '23456789012', '22222222222', '2000002', 'Exame pediátrico'),
('2024-05-20', '34567890123', '33333333333', '3000001', 'Avaliação ortopédica'),
('2024-06-01', '45678901234', '11111111111', '3000002', 'Pré-natal'),
('2024-06-10', '56789012345', '22222222222', '2000001', 'Consulta geral');

