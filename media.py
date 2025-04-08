media = 0
numero_inserito=0
contatore = 0
while media != "exit":
    numero_inserito = (input("inserisci un numero"))
    media = media + numero_inserito
    contatore+=1

print(f"La media dei numeri inseriti è {media}")    
                    