aliquotaA= 0.23
aliquotaB = 0.35
aliquotaC = 0.43
scaglione1= 28000
scaglione2= 50000

while True:
    reddito = float(input("Insersici il reddito"))

    if reddito<=scaglione1:
        tassazione=reddito*aliquotaA
    else:    
        if reddito > scaglione1 and reddito <= scaglione2:
            tassazione=(scaglione1*aliquotaA)+((reddito-scaglione1)*aliquotaB)
        else: 
            tassazione=(scaglione1*aliquotaA)+((scaglione2-scaglione1)*aliquotaB)+((reddito-scaglione2)*aliquotaC)
    
    print(f"La tassazione da pagare per un reddito di {reddito} è di {tassazione}, percependo un netto annuo di {reddito-tassazione}")
            
