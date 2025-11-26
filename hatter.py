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
    lista=lista
    szabadhelyek=[]
    i=0
    while i<len(lista):
        if lista[i]==" ":
            szabadhelyek.append(i)
        i+=1
    if len(szabadhelyek)==0:
        print("vége a játéknak")
        return lista
    gepvalasztas=random.randrange(len(szabadhelyek))
    lista[szabadhelyek[gepvalasztas]]="O"
    szabadhelyek=[]
    i=0
    return lista

    


#van-e még szabad hely? 
#számold meg, hoyg hány üres hely van a listában?


