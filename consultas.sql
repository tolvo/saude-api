-- Consultas SQL para o Prontuário Eletrônico do Cidadão (PEC)

-- Consulta 1: Histórico clínico completo de um cidadão (CPF específico)
-- Descrição: Retorna todas as consultas, exames, receitas, vacinações, cirurgias e internações de um cidadão.
SELECT c.Nome, cons.Data_consulta, cons.Relatorio_medico, e.Tipo_exame, e.Data_realizacao, r.Medicamento, v.Nome AS Vacina, cir.Nome_procedimento, i.Motivo
FROM cidadao c
LEFT JOIN consulta cons ON c.CPF = cons.CPF_cidadao
LEFT JOIN exame e ON cons.CPF_cidadao = e.CPF_cidadao AND cons.CPF_medico = e.CPF_medico AND cons.Data_consulta = e.Data_consulta
LEFT JOIN receita r ON cons.CPF_cidadao = r.CPF_cidadao AND cons.CPF_medico = r.CPF_medico AND cons.Data_consulta = r.Data_consulta
LEFT JOIN vacinacao vac ON c.CPF = vac.CPF_cidadao
LEFT JOIN vacina v ON vac.Lote_vacina = v.Lote AND vac.Cod_vacina = v.Cod_vacina
LEFT JOIN cirurgia cir ON c.CPF = cir.CPF_cidadao
LEFT JOIN internacao i ON c.CPF = i.CPF_cidadao
WHERE c.CPF = '12345678901';

-- Consulta 2: Vacinas em atraso por faixa etária (exemplo: cidadãos com menos de 30 anos sem vacina COVID)
-- Descrição: Cidadãos nascidos após 1994 sem vacinação de COVID.
SELECT c.Nome, c.Data_nasc
FROM cidadao c
WHERE c.Data_nasc > '1994-01-01'
AND NOT EXISTS (
    SELECT 1 FROM vacinacao v WHERE v.CPF_cidadao = c.CPF AND v.Cod_vacina = 'VAC001'
);

-- Consulta 3: Consultas por unidade de saúde em um período (ex: outubro 2023)
-- Descrição: Número de consultas por unidade no mês de outubro 2023.
SELECT u.Nome, COUNT(*) AS Numero_Consultas
FROM unidade_saude u
JOIN consulta cons ON u.CNES = cons.CNES_unidade
WHERE cons.Data_consulta BETWEEN '2023-10-01' AND '2023-10-31'
GROUP BY u.CNES, u.Nome;

-- Consulta 4: Pacientes com prescrição de determinado medicamento (ex: Aspirina)
-- Descrição: Cidadãos que têm receita de Aspirina.
SELECT DISTINCT c.Nome, r.Medicamento
FROM cidadao c
JOIN receita r ON c.CPF = r.CPF_cidadao
WHERE r.Medicamento = 'Aspirina';

-- Consulta 5: Cidadãos que tomaram todas as vacinas disponíveis (Divisão Relacional)
-- Descrição: Cidadãos que têm vacinação para todas as vacinas existentes.
SELECT c.Nome
FROM cidadao c
WHERE NOT EXISTS (
    SELECT v.Lote, v.Cod_vacina
    FROM vacina v
    EXCEPT
    SELECT vac.Lote_vacina, vac.Cod_vacina
    FROM vacinacao vac
    WHERE vac.CPF_cidadao = c.CPF
);