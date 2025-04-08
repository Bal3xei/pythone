prices=[]
isPet=[]
counter=0


def discount(prices, isPet, nItems):
    x=0
    stringa = ""

    if nItems >5:  
        while x< nItems:
            if isPet[x]==True:
                stringa+=(f"{prices[x]} Y\n")
            else:
                stringa+=(f"{prices[x]-(prices[x]*0.2)} N\n")
                somma += prices[x]
            x+=1
            
        return stringa
    else:
        while x< nItems:
            if isPet[x]==True:
                stringa+=(f"{prices[x]} Y\n")
            else:
                stringa+=(f"{prices[x]} N\n")
            x+=1
    stringa += f"Lo sconto è di  {somma*0.20}"
    return stringa
    




    

riga= input("Passami il prezzo e Y/N")
while riga!= "-1":
    prices.append(float(riga[:-2]))
    if riga[-1]=="Y":
        isPet.append(True) 
    else: isPet.append(False)
    counter+=1
    riga= input("Passami il prezzo e Y/N") 

print(discount(prices, isPet, counter))

