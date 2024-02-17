import sqlite3

exercicios = sqlite3.connect('banco')
cursor = exercicios.cursor()

# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')



exercicios.commit()
exercicios.close