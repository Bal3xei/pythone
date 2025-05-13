import pymysql

queries = [ "DELETE FROM regione", "Insert INTO regione (nome) VALUES ('Marche')", "Insert Into Regione (nome) VALUES ('Emilia Romagna')"]

conn = pymysql.connect(
    host='localhost', port=3306,
    user='root', password='root',db = "province")

cur = conn.cursor()

idx = int(input(f"Inserisci l'indice della query da eseguire (0-{len(queries)-1}: "))
print (f"Eseguo la query {idx}: {queries[idx]}...")

n_righe = cur.execute(queries[idx])
conn.commit()
print(f"Query eseguita, {n_righe} righe modificate")
