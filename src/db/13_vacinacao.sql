CREATE TABLE VACINACAO(
    dose INTEGER,
    cidadao VARCHAR(11),
    vacina_cod INTEGER,
    vacina_lote INTEGER,
    ubs VARCHAR(10),
    data DATE NOT NULL,
    enfermeiro VARCHAR(11) NOT NULL,
    CONSTRAINT PK_VACINACAO PRIMARY KEY (dose, cidadao, vacina_cod, vacina_lote),
    CONSTRAINT FK_VACINACAO_1 FOREIGN KEY (cidadao)
                REFERENCES CIDADAO(cpf)
                ON DELETE CASCADE,
    CONSTRAINT FK_VACINACAO_2 FOREIGN KEY (vacina_cod, vacina_lote)
                REFERENCES VACINA(cod, lote)
                ON DELETE CASCADE,
    CONSTRAINT FK_VACINACAO_3 FOREIGN KEY (ubs)
                REFERENCES UNIDADE_BASICA_SAUDE(cnes)
                ON DELETE CASCADE,
    CONSTRAINT FK_VACINACAO_4 FOREIGN KEY (enfermeiro)
                REFERENCES ENFERMEIRO(cpf)
                ON DELETE CASCADE


);

-- Dados de exemplo
INSERT INTO VACINACAO (dose, cidadao, vacina_cod, vacina_lote, ubs, data, enfermeiro) VALUES 
(1, '12345678901', 1, 1001, '2000001', '2024-03-15', '44444444444'),
(2, '12345678901', 1, 1002, '2000001', '2024-06-15', '44444444444'),
(1, '23456789012', 2, 2001, '2000002', '2024-04-10', '55555555555'),
(1, '34567890123', 3, 3001, '2000001', '2024-05-20', '44444444444'),
(1, '45678901234', 4, 4001, '2000002', '2024-06-05', '55555555555');

