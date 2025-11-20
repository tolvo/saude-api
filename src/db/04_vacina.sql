CREATE TABLE IF NOT EXISTS VACINA (
    cod INTEGER,
    lote INTEGER,
    nome_popular VARCHAR(29),
    fabricante VARCHAR(30),
    validade DATE,
    CONSTRAINT PK_VACINA PRIMARY KEY (cod, lote)

);

-- Dados de exemplo
INSERT INTO VACINA (cod, lote, nome_popular, fabricante, validade) VALUES 
(1, 1001, 'COVID-19', 'Pfizer', '2025-12-31'),
(1, 1002, 'COVID-19', 'Pfizer', '2026-01-31'),
(2, 2001, 'Influenza', 'Butantan', '2025-06-30'),
(3, 3001, 'Hepatite B', 'GSK', '2026-03-15'),
(4, 4001, 'Febre Amarela', 'Bio-Manguinhos', '2027-08-20');
