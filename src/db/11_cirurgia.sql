CREATE TABLE IF NOT EXISTS CIRURGIA(
    data_realizacao DATE,
    cidadao VARCHAR(11),
    cnes VARCHAR(10),
    duracao TIME,
    observacao VARCHAR(300),
    cuidados_posteriores VARCHAR(100),
    nome_procedimento VARCHAR(100),
    CONSTRAINT PK_CIRURGIA PRIMARY KEY (data_realizacao, cidadao, cnes),
    CONSTRAINT FK_CIRURGIA_1 FOREIGN KEY (cidadao)
                REFERENCES CIDADAO(cpf)
                ON DELETE CASCADE,
    CONSTRAINT FK_CIRURGIA_2 FOREIGN KEY (cnes)
                REFERENCES HOSPITAL(cnes)
                ON DELETE CASCADE

);

-- Dados de exemplo
INSERT INTO CIRURGIA (data_realizacao, cidadao, cnes, duracao, observacao, cuidados_posteriores, nome_procedimento) VALUES 
('2024-01-15', '12345678901', '3000001', '03:30:00', 'Cirurgia realizada com sucesso', 'Repouso de 30 dias', 'Angioplastia'),
('2024-03-05', '34567890123', '3000001', '02:15:00', 'Fixação interna da fratura', 'Fisioterapia após 15 dias', 'Redução de fratura'),
('2024-04-20', '45678901234', '3000003', '01:00:00', 'Parto cesárea sem complicações', 'Repouso de 40 dias', 'Cesariana');

