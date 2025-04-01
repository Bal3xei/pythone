carattere=input("inserisci carattere")
ampiezza_base=int(input("inserisci numero ampiezza"))
            

# carattere="A"
# ampiezza_base = 3
# i=1
# while righe == ampiezza_base:
#     righe+=1

i = 1
while i <= ampiezza_base:
  testo = " "*((ampiezza_base-i)//2) + carattere * (i+1)
  i += 1
  print(testo)


  