CREATE DATABASE inventario;

USE inventario;

CREATE TABLE produtos (
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10, 2),
    quantidade INT
);

SELECT * FROM produtos;

