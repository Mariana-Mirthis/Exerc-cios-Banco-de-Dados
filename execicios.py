import sqlite3

exercicios = sqlite3.connect('banco')
cursor = exercicios.cursor()



exercicios.commit()
exercicios.close