lista = [10,20,30]
temp = 0
while True:
    temp = (input("Inserisci un numero"))
    if temp!="q":
        lista.append(int(temp))
    else:
       break


for i in lista:
    
    somma=sum(lista)
print(f"Il numero più alto è ",(somma/len(lista)))

