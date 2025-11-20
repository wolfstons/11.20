import kiiras
import hatter
import ellenorzes
lista=[" "," "," ",
       " "," "," ",
       " "," "," "]
while hatter.ellenorzes(lista):
    kiiras.kiir(lista)
    hatter.bekeres(lista)
    hatter.geplepes(lista)
    kiiras.kiir(lista)
    hatter.ellenorzes(lista)