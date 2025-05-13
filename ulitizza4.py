import pymysql

# queries = [ "DELETE FROM regione", f"Insert INTO regione (nome) VALUES ({input('Inserisci il nome della regione: ')})"]

conn = pymysql.connect(
    host='localhost', port=3306,
    user='root', password='root',db = "province")



def esegui_query(idx):
    
    match (idx.upper()):
        case "DELETE":
            cur.execute("DELETE FROM regioni limit 50")
            print(f"Query eseguita!")
        case "INSERT":
            cur.execute(f"INSERT INTO regioni (nome) VALUES ('{input('Inserisci il nome della regione: ')}')")
            print(f"Query eseguita!")
        case _:
            print("Indice non valido")



cur = conn.cursor()


idx = input("Scegli tra le seguenti query: 'Delete' oppure 'Insert'")
while idx != "q":
    cur = conn.cursor()
    esegui_query(idx)
    idx = input("Scegli tra le seguenti query: 'Delete' oppure 'Insert'")
    
# idx = int(input(f"Inserisci l'indice della query da eseguire (0-{len(queries)-1}: "))
# print (f"Eseguo la query {idx}: {queries[idx]}... oppure q per uscire")

# n_righe = cur.execute(queries[idx])
# conn.commit()
# print(f"Query eseguita, {n_righe} righe modificate")
