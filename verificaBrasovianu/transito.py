
import datetime


class Transito:
    def __init__ (self, targa, data, ora, velocita):
        self.targa = targa
        self.data = data
        self.ora = ora
        self.velocita = velocita
    
    def getTarga(self,targa):
        return self.targa
    
    def getData(self,data):
        return self.data
    
    def getOra(self,ora):
        return self.ora
    
    def getVelocita(self,velocita):
        return self.velocita
    

    def is_multa(self):
        limite = 50
        if self.velocita > (limite*1.03): # 3% di tolleranza rispetto al limite
            return True
        else:
            return False

    def contaTransiti(self):
        return self.targa.count(self.targa)


with open(r"verifica\transiti_urbani.txt") as infile:
    lines = infile.readlines()[1:]  # Salta la prima riga 
    transiti = []
    

    for line in lines:
        targa, dataUnita, velocita = line.strip().split(";")
        data, ora = datetime.datetime.strptime(dataUnita, "%Y-%m-%d %H:%M:%S").date(), datetime.datetime.strptime(dataUnita, "%Y-%m-%d %H:%M:%S").time()  # Converte la stringa in un oggetto datetime
        velocita = float(velocita) 
        transito = Transito(targa, data, ora, velocita)  # Crea un oggetto Transito
        transiti.append(transito)  # Aggiunge l'oggetto alla lista
        #print(transito.targa,transito.data, transito.ora, transito.velocita, transito.is_multa() )  # Stampa i dati del transito per verifica
    
    #tagaFrequente= transiti.contaTransit() # Conta il numero di transiti per ogni targa 
   

ListaMulte = []
ListaTarghe = []
for transito in transiti:   #conta numero multe totali
    if transito.is_multa():
        ListaMulte.append(transito.targa)  # Aggiunge la targa alla lista delle multe
    



print("Numero totale di transiti per targa:", max(set(ListaTarghe), key=ListaTarghe.count)) # Dovrebbe stampare la targa con il numero massimo di transiti

print("Numero totale di multe:", len(ListaMulte))  # Stampa il numero totale di multe

print("Targa con più multe:", max(set(ListaMulte), key=ListaMulte.count))  # Stampa la targa con il numero massimo di multe
