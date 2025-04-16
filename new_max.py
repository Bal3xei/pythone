
# file_path=input("Inserisci nome file")
file_path= "new_max.txt"

with open(file_path, 'r') as file:
    numeri = (file.readlines())
    for numero in numeri:
        numero = float(numero.replace("\n",""))

def media(numeri):
    cont = 0
    somma=0
    
    for numero in numeri:
        somma+= float(numero)
        cont+=1
        media = somma/cont
    return media

def massimo (numeri):
    massimo = max(numeri)
    pos = []
    for i,valore in enumerate(numeri):
        if valore== massimo:
            pos.append(i+1)

    return f"Il numero massimo è {massimo}, che si trova nella riga {pos}"


print(media(numeri),massimo(numeri))

