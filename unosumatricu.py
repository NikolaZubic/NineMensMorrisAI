import copy

#Funkcija koja prebrojava broj kamencica koje je postavio neki igrac
def brojKonkretnihPoteza(ploca, vrednost):
    return ploca.count(vrednost)

def InverznaPloca(ploca):
    inverzna = []
    for kamencic in ploca:
        if kamencic == "1": #oznacava potez igraca
            inverzna.append("2")
        elif kamencic == "2":
            inverzna.append("1")
        else:
            inverzna.append("X")
    return inverzna

def generisanjeListeInverznihPloca(lista_pozicija):
    listaInv = []
    for pozicija in lista_pozicija:
        listaInv.append(InverznaPloca(pozicija))
    return listaInv