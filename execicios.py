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


exercicios.commit()
exercicios.close