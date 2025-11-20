-- Dados iniciais para o Prontuário Eletrônico do Cidadão (PEC)

-- Cidadão
INSERT INTO cidadao (CPF, Nome, Data_nasc, Sexo, Endereco, Telefone, Tipo_sanguineo) VALUES
('12345678901', 'João Silva', '1990-05-15', 'Masculino', 'Rua A, 123', '11987654321', 'A+'),
('98765432109', 'Maria Oliveira', '1985-10-20', 'Feminino', 'Rua B, 456', '11912345678', 'O-');

-- Alergia Cidadão
INSERT INTO alergia_cidadao (CPF, Alergia) VALUES
('12345678901', 'Penicilina'),
('98765432109', 'Amendoim'),
('98765432109', 'Poeira');

-- Unidade de Saúde
INSERT INTO unidade_saude (CNES, Tipo, Nome, Endereco, Horario_func) VALUES
('CNES001', 'Hospital', 'Hospital Central', 'Av. Saúde, 1000', '24h'),
('CNES002', 'Unidade Básica de Saúde', 'UBS Centro', 'Rua Centro, 200', '08h-18h');

-- Hospital
INSERT INTO hospital (CNES, Capacidade) VALUES
('CNES001', 200);

-- Unidade Básica
INSERT INTO unidade_basica (CNES) VALUES
('CNES002');

-- Profissional
INSERT INTO profissional (CPF, Nome, Tipo) VALUES
('11111111111', 'Dr. Carlos', 'Médico'),
('22222222222', 'Enf. Ana', 'Enfermeiro');

-- Médico
INSERT INTO medico (CPF, CRM, Especialidade) VALUES
('11111111111', 'CRM12345', 'Cardiologia');

-- Enfermeiro
INSERT INTO enfermeiro (CPF, COREN) VALUES
('22222222222', 'COREN67890');

-- Atua
INSERT INTO atua (CPF_profissional, CNES_unidade) VALUES
('11111111111', 'CNES001'),
('22222222222', 'CNES002');

-- Consulta
INSERT INTO consulta (CPF_cidadao, CPF_medico, Data_consulta, CNES_unidade, Relatorio_medico) VALUES
('12345678901', '11111111111', '2023-10-01', 'CNES001', 'Paciente com dor no peito, prescrito exames.'),
('98765432109', '11111111111', '2023-10-05', 'CNES001', 'Consulta de rotina.');

-- Receita
INSERT INTO receita (CPF_cidadao, CPF_medico, Data_consulta, Medicamento, Dosagem, Duracao) VALUES
('12345678901', '11111111111', '2023-10-01', 'Aspirina', '100mg', '7 dias'),
('98765432109', '11111111111', '2023-10-05', 'Vitamina C', '500mg', '30 dias');

-- Exame
INSERT INTO exame (CPF_cidadao, CPF_medico, Data_consulta, Tipo_exame, Data_realizacao, Local, Link_resultado) VALUES
('12345678901', '11111111111', '2023-10-01', 'Eletrocardiograma', '2023-10-02', 'Hospital Central', 'http://exames.com/123'),
('98765432109', '11111111111', '2023-10-05', 'Hemograma', '2023-10-06', 'Lab Central', 'http://exames.com/456');

-- Vacina
INSERT INTO vacina (Lote, Cod_vacina, Nome, Fabricante, Validade) VALUES
('LOTE001', 'VAC001', 'COVID-19', 'Pfizer', '2024-12-31'),
('LOTE002', 'VAC002', 'Gripe', 'Sanofi', '2024-06-30');

-- Vacinação
INSERT INTO vacinacao (CPF_cidadao, Lote_vacina, Cod_vacina, Dose, Data_aplicacao, CNES_unidade, CPF_enfermeiro) VALUES
('12345678901', 'LOTE001', 'VAC001', 1, '2023-09-01', 'CNES002', '22222222222'),
('98765432109', 'LOTE002', 'VAC002', 1, '2023-09-10', 'CNES002', '22222222222');

-- Cirurgia
INSERT INTO cirurgia (CPF_cidadao, CNES_hospital, Data_realizacao, Nome_procedimento, Duracao, Observacoes, Cuidados) VALUES
('12345678901', 'CNES001', '2023-11-01 10:00:00', 'Cirurgia Cardíaca', '2 hours', 'Procedimento bem-sucedido', 'Repouso absoluto por 1 mês');

-- Auxilia
INSERT INTO auxilia (CPF_enfermeiro, CPF_cidadao, CNES_hospital, Data_realizacao) VALUES
('22222222222', '12345678901', 'CNES001', '2023-11-01 10:00:00');

-- Opera
INSERT INTO opera (CPF_medico, CPF_cidadao, CNES_hospital, Data_realizacao) VALUES
('11111111111', '12345678901', 'CNES001', '2023-11-01 10:00:00');

-- Internação
INSERT INTO internacao (CPF_cidadao, CNES_hospital, Data_entrada, Data_alta, Motivo, Ala) VALUES
('98765432109', 'CNES001', '2023-10-15', '2023-10-20', 'Pneumonia', 'Ala 3');

-- Atende
INSERT INTO atende (CPF_profissional, CPF_cidadao, CNES_hospital, Data_entrada) VALUES
('11111111111', '98765432109', 'CNES001', '2023-10-15'),
('22222222222', '98765432109', 'CNES001', '2023-10-15');

-- Acompanhamento
INSERT INTO acompanhamento (CPF_profissional, CPF_cidadao, CNES_hospital, Data_entrada, Data_hora_acompanhamento, Procedimentos, Condicao) VALUES
('11111111111', '98765432109', 'CNES001', '2023-10-15', '2023-10-15 08:00:00', 'Administração de antibióticos', 'Estável'),
('22222222222', '98765432109', 'CNES001', '2023-10-15', '2023-10-16 08:00:00', 'Troca de curativos', 'Melhorando');