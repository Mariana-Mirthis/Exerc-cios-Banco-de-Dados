import sqlite3

exercicios = sqlite3.connect('banco')
cursor = exercicios.cursor()

# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (1, "Neymar Silva", 20, "Engenharia");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (2, "Messi Oliveira", 21, "Medicina");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (3, "Cristiano Souza", 22, "Direito");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (4, "Ronaldo Santos", 23, "Administração");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (5, "Daniel Mendes", 24, "Ciências da Computação");')

# 3. Consultas Básicas

# a) Selecionar todos os registros da tabela "alunos".
dados = cursor.execute('SELECT * FROM alunos')

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética
dados = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome ASC')

# d) Contar o número total de alunos na tabela
dados = cursor.execute('SELECT COUNT(*) AS total_alunos FROM alunos')

for alunos in dados:
    print(alunos)



exercicios.commit()
exercicios.close