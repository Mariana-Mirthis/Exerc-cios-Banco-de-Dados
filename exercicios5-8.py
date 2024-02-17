import sqlite3

exercicios5 = sqlite3.connect('banco')
cursor = exercicios5.cursor()

# 5. Criar uma Tabela e Inserir Dados
cursor.execute('CREATE TABLE clientes (id_clientes INT PRIMARY KEY,  nome VARCHAR(100), idade INT, saldo FLOAT);')
cursor.execute('INSERT INTO clientes (nome, idade, saldo) VALUES("Wagner Silva", 25, 500.00),("Sandra Santos", 35, 1200.50),("Gustavo Oliveira", 40, 800.25),("Gabriel Souza", 20, 350.75),("Jessica Costa", 32, 1500.00);')



exercicios5.commit()
exercicios5.close