CREATE TABLE IF NOT EXISTS PROFISSIONAL_INTERNACAO(
    data_internacao DATE,
    cidadao VARCHAR(11),
    cnes VARCHAR(10),
    data_visita DATE,
    horario VARCHAR(10),
    visita VARCHAR(15),
    profissional VARCHAR(11),
    procedimento_realizado VARCHAR(50),
    situacao_paciente VARCHAR(50),
    CONSTRAINT PK_PROFISSIONAL_INTERNACAO PRIMARY KEY(data_internacao, cidadao, cnes, data_visita, profissional),
    CONSTRAINT FK_PROFISSIONAL_INTERNACAO_1 FOREIGN KEY(data_internacao, cidadao, cnes)
                REFERENCES INTERNACAO(data_entrada, cidadao, cnes)
                ON DELETE CASCADE,
    CONSTRAINT FK_PROFISSIONAL_INTERNACAO_2 FOREIGN KEY(profissional)
                REFERENCES PROFISSIONAL(cpf)
                ON DELETE CASCADE


);

-- Dados de exemplo
INSERT INTO PROFISSIONAL_INTERNACAO (data_internacao, cidadao, cnes, data_visita, horario, visita, profissional, procedimento_realizado, situacao_paciente) VALUES 
('2024-01-15', '12345678901', '3000001', '2024-01-16', '10:00', 'Rotina', '11111111111', 'Avaliação cardiológica', 'Estável'),
('2024-01-15', '12345678901', '3000001', '2024-01-17', '14:00', 'Rotina', '44444444444', 'Troca de curativos', 'Recuperando'),
('2024-02-10', '23456789012', '3000002', '2024-02-11', '09:00', 'Emergência', '22222222222', 'Medicação endovenosa', 'Grave'),
('2024-03-05', '34567890123', '3000001', '2024-03-06', '11:00', 'Rotina', '33333333333', 'Avaliação pós-operatória', 'Estável');
