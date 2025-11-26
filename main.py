import kiiras
import hatter
import ellenorzes
lista=[" "," "," ",
       " "," "," ",
       " "," "," "]
vege=ellenorzes.ellenorzes(lista)
tele_e=ellenorzes.ellenorzes_tele(lista,vege)
kiiras.kiir(lista)
while tele_e==True or vege==True:
       hatter.bekeres(lista)
       kiiras.kiir(lista)
       hatter.geplepes(lista)
       kiiras.kiir(lista)
       vege=ellenorzes.ellenorzes(lista)
       ellenorzes.ellenorzes(lista)
       ellenorzes.ellenorzes_tele(lista,vege)
