import sqlite3

exercicios5 = sqlite3.connect('banco')
cursor = exercicios5.cursor()

# 5. Criar uma Tabela e Inserir Dados
cursor.execute('CREATE TABLE clientes (id_clientes INT PRIMARY KEY,  nome VARCHAR(100), idade INT, saldo FLOAT);')
cursor.execute('INSERT INTO clientes (nome, idade, saldo) VALUES("Wagner Silva", 25, 500.00),("Sandra Santos", 35, 1200.50),("Gustavo Oliveira", 40, 800.25),("Gabriel Souza", 20, 350.75),("Jessica Costa", 32, 1500.00);')

# 6. Consultas e Funções Agregadas

# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')

# b) Calcule o saldo médio dos clientes.
dados = cursor.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes')

# c) Encontrar o cliente com o saldo máximo:
dados = cursor.execute('SELECT nome, saldo FROM clientes ORDER BY saldo DESC LIMIT 1')

# d) Contar quantos clientes têm saldo acima de 1000:
dados = cursor.execute('SELECT COUNT(*) AS total_clientes FROM clientes WHERE saldo > 1000')

# 7. Atualização e Remoção com Condições

# a) Atualizar o saldo de um cliente específico:
dados = cursor.execute('UPDATE clientes SET saldo = 1500 WHERE nome = "Wagner Silva"')

# b) Remover um cliente pelo seu ID:
dados = cursor.execute('DELETE FROM clientes WHERE nome = "Sandra Oliveira"')

# 8. Junção de Tabelas

cursor.execute("""CREATE TABLE compras (id_compras INT PRIMARY KEY, id_cliente INT, produto VARCHAR(200), valor REAL, FOREIGN KEY (id_cliente) REFERENCES clientes (id_clientes));""")

# a) - Inserindo Compras:

cursor.execute("""INSERT INTO compras (id_cliente, produto, valor) VALUES (1, 'Livro', 50.00), (2, 'Camisa', 100.00), (3, 'Celular', 1500.00), (4, 'Jogo', 80.00), (5, 'Eletrônico', 200.00);""")

# b) - Exibindo Nome do Cliente, Produto e Valor:
dados = cursor.execute("""
SELECT clientes.nome, compras.produto, compras.valor
FROM compras
INNER JOIN clientes ON clientes.id_clientes = compras.id_cliente;
""")


for compras in dados:
    print(compras)

exercicios5.commit()
exercicios5.close