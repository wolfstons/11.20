import random
def bekeres(lista):
    joadat= True
    while joadat:
        oszlopok = {"a": 0, "b": 1, "c": 2}

        sor = input("Adja meg a sort (1,2,3): ")


        while sor not in ("1", "2", "3"):
            print("Hibás sor! Csak 1,2,3 lehet.")
            sor = input("Adja meg a sort (1,2,3): ")


        s = int(sor) - 1

        oszlop = input("Adja meg az oszlopot (a,b,c): ")

    
        while oszlop not in oszlopok:
            print("Hibás oszlop! Csak a,b,c lehet.")
            oszlop = input("Adja meg az oszlopot (a,b,c): ")

        o = oszlopok[oszlop]

        if lista[s*3 + o] != " ":
            print("Ez a mező már foglalt! Próbáld újra.")
        else:
            joadat = False
    
    lista[s*3 + o] = "x"

    return lista
    

def geplepes(lista):
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

def ellenorzes(lista):
    if lista[0] and lista[1] and lista[2] or lista[3] and lista[4] and lista[5] or lista[6] and lista[7] and lista[8] or lista[0] and lista[4] and lista[7] or lista[2] and lista[4] and lista[6] or lista[0] and lista[3] and lista[6] or lista[1] and lista[4] and lista[7] or lista[2] and lista[5] and lista[8] == "X" or "O":
        print("véget ért'")
        return True
