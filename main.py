import random
import kiiras
lista=[" "," "," ",
       " "," "," ",
       " "," "," "]

def geplepes():
    i=0
    while i<len(lista):
        pozicio=0
        gepszam1=random.randint(0,2)
        gepszam2=random.randint(0,2)
        if gepszam2>0:
            pozicio=gepszam1
            lista[pozicio]="O"
            return lista
        if gepszam2==1:
            pozicio=gepszam1+3
            lista[pozicio]="O"
            return lista
        else:
            pozicio=gepszam1+6
            lista[pozicio]="O"
            return lista
        i+=1


geplepes()
kiiras.kiir(lista)