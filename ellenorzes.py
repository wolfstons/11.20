def ellenorzes(lista):
    vege=True
    nyero_kombinaciok = [
        [0,1,2], 
        [3,4,5], 
        [6,7,8],  
        [0,3,6],
        [1,4,7],  
        [2,5,8], 
        [0,4,8], 
        [2,4,6]   
    ]

    for a, b, c in nyero_kombinaciok:
        if lista[a] == lista[b] == lista[c] and lista[a] != " ":
            if lista[a]=="x":
                print("gratulálok, nyertél!")
                vege=False
                return vege
            if lista[a]=="O":
                print("A gép nyert! sajnálom vesztél.")
                vege=False
                return vege
            else:
                return vege

    return vege

def ellenorzes_tele(lista,vege):
    vege=vege
    if vege==True:
        return False
    else:
        i=0
        helyes=False
        while i<len(lista):
            if lista[i]!="x" or lista[i]!="O":
                helyes=True
            else:
                print("Nincs több szabad hely, döntetlen!")
            i+=1
        return helyes