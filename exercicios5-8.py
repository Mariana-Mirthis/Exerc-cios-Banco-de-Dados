import sqlite3

exercicios5 = sqlite3.connect('banco')
cursor = exercicios5.cursor()





exercicios5.commit()
exercicios5.close