import os
import sqlite3

# deleta o arquivo
os.remove("escola.db") if os.path.exists("escola.db") else None

# conecta ao arquivo, se não tiver, cria.
con = sqlite3.connect('escola.db')

cur = con.cursor()

# cria a tabela

sql_create = 'create table gordos ' \
             '(id integer primary key, ' \
             'Nome varchar(20), ' \
             'peso integer, ' \
             'IMC integer)'

cur.execute(sql_create)

# insere os dados


sql_insert = 'insert into gordos values (?, ? , ? , ?)'

recset = [(1, "Guilherme", 87, 17),
          (2, "Vinicius", 84, 26),
          (3, "Rafael", 78, 19)]

for rec in recset:
    cur.execute(sql_insert, rec)

# grava a transação


con.commit()

# seleciona os registros

sql_select = 'select * from gordos'

cur.execute(sql_select)
dados = cur.fetchall()

for linha in dados:
    pass

recset = [(4, "Barbara", 60, 33)]

for rec in recset:
    cur.execute(sql_insert, rec)

con.commit()

cur.execute('select * from gordos')

recset = cur.fetchall()

for rec in recset:
    print('gordos Id: %d, Nome: %s, Peso: %d, IMC: %d \n' % rec)


con.close()