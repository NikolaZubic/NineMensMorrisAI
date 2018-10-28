from unosumatricu import *
import copy

""" Ukoliko pozicija1 i pozicija2 na ploci pripadaju igracu vrati True. Igrac je string reprezentacija 
toga ko igra igru ("1" - igrac tj. mi, "2' - racunar(AI) ). Ploca je matrica tekuce igre. """
def isMill(igrac, ploca, pozicija1, pozicija2):
    if ((ploca[pozicija1] == igrac) and (ploca[pozicija2] == igrac)):
        return True
    return False

""" Funkcija vraca True ukoliko bilo koji igrac(ili mi ili racunar(AI)) ima MILL na nekoj poziciji. Pozicija se 
odnosi na poziciju za koju vrsimo provjeru, a ploca na matricu tekuce igre."""
def imaLiIkoMill(pozicija, ploca):

    igrac = ploca[pozicija]

    #Ukoliko je pozicija zauzeta, ima smisla provjeravati je li odigran MILL
    if (igrac != "X"):
        return postojiLiMillZaKonkretnuMatricu(pozicija, ploca, igrac)
    return False

""" Cilj sledece funkcije jeste da nam vrati za datu poziciju u matrici (trenutnom stanju igre) susjedne pozicije. 
Npr: za 08 da vrati 09,11.

X(00)----------------------X(01)----------------------X(02)
|                           |                           |
|       X(08)--------------X(09)--------------X(10)     |
|       |                   |                    |      |
|       |                   |                    |      |
|       |        X(16)-----X(17)-----X(18)       |      |
|       |         |                   |          |      |
|       |         |                   |          |      |
X(03)---X(11)----X(19)               X(20)----X(12)---X(04)
|       |         |                   |          |      |
|       |         |                   |          |      |
|       |        X(21)-----X(22)-----X(23)       |      |
|       |                   |                    |      |
|       |                   |                    |      |
|       X(13)--------------X(14)--------------X(15)     |
|                           |                           |
|                           |                           |
X(05)----------------------X(06)----------------------X(07)
"""
def susjednePozicijeNaPloci(pozicija):
    susjedna = [[1, 3], [0, 2, 9], [1, 4], [0, 5, 11], [2, 7, 12], [3, 6], [5, 7, 14], [4, 6], [9, 11], \
                [1, 8, 10, 17], [9, 12], [3, 8, 13, 19], [4, 10, 15, 20], [11, 14], [6, 13, 15, 22], [12, 14], \
                [17, 19], [9, 16, 18], [17, 20], [11, 16, 21], [12, 18, 23], [19, 22], [21, 23, 14], [20, 22]]
    return susjedna[pozicija]

#Vraca True ako postoji MILL na poziciji za igraca na datoj matrici.
def postojiLiMillZaKonkretnuMatricu(pozicija, ploca, igrac):
    mill = [
        (isMill(igrac, ploca, 1, 2) or isMill(igrac, ploca, 3, 5)),
        (isMill(igrac, ploca, 0, 2) or isMill(igrac, ploca, 9, 17)),
        (isMill(igrac, ploca, 0, 1) or isMill(igrac, ploca, 4, 7)),
        (isMill(igrac, ploca, 0, 5) or isMill(igrac, ploca, 11, 19)),
        (isMill(igrac, ploca, 2, 7) or isMill(igrac, ploca, 12, 20)),
        (isMill(igrac, ploca, 0, 3) or isMill(igrac, ploca, 6, 7)),
        (isMill(igrac, ploca, 5, 7) or isMill(igrac, ploca, 14, 22)),
        (isMill(igrac, ploca, 2, 4) or isMill(igrac, ploca, 5, 6)),
        (isMill(igrac, ploca, 9, 10) or isMill(igrac, ploca, 11, 13)),
        (isMill(igrac, ploca, 8, 10) or isMill(igrac, ploca, 1, 17)),
        (isMill(igrac, ploca, 8, 9) or isMill(igrac, ploca, 12, 15)),
        (isMill(igrac, ploca, 3, 19) or isMill(igrac, ploca, 8, 13)),
        (isMill(igrac, ploca, 20, 4) or isMill(igrac, ploca, 10, 15)),
        (isMill(igrac, ploca, 8, 11) or isMill(igrac, ploca, 14, 15)),
        (isMill(igrac, ploca, 13, 15) or isMill(igrac, ploca, 6, 22)),
        (isMill(igrac, ploca, 13, 14) or isMill(igrac, ploca, 10, 12)),
        (isMill(igrac, ploca, 17, 18) or isMill(igrac, ploca, 19, 21)),
        (isMill(igrac, ploca, 1, 9) or isMill(igrac, ploca, 16, 18)),
        (isMill(igrac, ploca, 16, 17) or isMill(igrac, ploca, 20, 23)),
        (isMill(igrac, ploca, 16, 21) or isMill(igrac, ploca, 3, 11)),
        (isMill(igrac, ploca, 12, 4) or isMill(igrac, ploca, 18, 23)),
        (isMill(igrac, ploca, 16, 19) or isMill(igrac, ploca, 22, 23)),
        (isMill(igrac, ploca, 6, 14) or isMill(igrac, ploca, 21, 23)),
        (isMill(igrac, ploca, 18, 20) or isMill(igrac, ploca, 21, 22)),
    ]
    return mill[pozicija]


def ukloniKamencic(kopija_ploce, lista_ploca):
    for kamencic in range(len(kopija_ploce)):
        if (kopija_ploce[kamencic] == "2"):
            if not imaLiIkoMill(kamencic, kopija_ploce):
                nova_ploca = copy.deepcopy(kopija_ploce)
                nova_ploca[kamencic] = "X"
                lista_ploca.append(nova_ploca)
    return lista_ploca

def brojMogucihMill(ploca, igrac):
    brojac = 0

    for kamencic in range(len(ploca)):
        if (ploca[kamencic] == "X"):
            if postojiLiMillZaKonkretnuMatricu(kamencic, ploca, igrac):
                brojac += 1
    return brojac


"""Faza 1: postavljanje figura
Igra pocinje sa praznom tablom. Igraci naizmjenicno postavljaju svojih 9 figura na slobodna polja na tabli. 
Ukoliko igrac formira niz od 3 figure, ima pravo da ukloni jednu protivnicku figuru. Ona protivnicka figura koja se 
uklanja ne smije biti dio protivnickog niza od 3 figure, osim u slucaju da su sve protivnicke figure u nizu od 3."""
def faza1(ploca):
    lista_ploca = []

    for kamencic in range(len(ploca)):
        if (ploca[kamencic] == "X"):
            kopija_ploce = copy.deepcopy(ploca)
            kopija_ploce[kamencic] = "1"

            if (imaLiIkoMill(kamencic, kopija_ploce)):
                lista_ploca = ukloniKamencic(kopija_ploce, lista_ploca)
            else:
                lista_ploca.append(kopija_ploce)
    return lista_ploca


"""Faza 2: kretanje
Igraci naizmjenicno igraju po jedan potez. Potez predstavlja pomjeranje svoje figure na susjedno slobodno mjesto. 
Cilj kretanja je da se formira niz od 3 svoje figure kada je moguce ukloniti jednu protivnicku figuru. Kada jedan 
od igraca ostane sa 3 figure na tabli, prelazi se na fazu 3."""
def faza2(ploca):
    lista_ploca = []

    for kamencic in range(len(ploca)):
        if (ploca[kamencic] == "1"):
            susjedne_pozicije = susjednePozicijeNaPloci(kamencic)

            for pozicija in susjedne_pozicije:
                if (ploca[pozicija] == "X"):
                    kopija_ploce = copy.deepcopy(ploca)
                    kopija_ploce[kamencic] = "X"
                    kopija_ploce[pozicija] = "1"

                    if imaLiIkoMill(pozicija, kopija_ploce):
                        lista_ploca = ukloniKamencic(kopija_ploce, lista_ploca)
                    else:
                        lista_ploca.append(kopija_ploce)
    return lista_ploca


"""Faza 3: preskakanje
Figure se mogu pomjeriti na bilo koju slobodnu poziciju na tabli, ukljucujuci i preskakanje."""
def faza3(ploca):
    lista_ploca = []

    for kamencic in range(len(ploca)):
        if (ploca[kamencic] == "1"):

            for novo_mjesto in range(len(ploca)):
                if (ploca[novo_mjesto] == "X"):
                    kopija_ploce = copy.deepcopy(ploca)

                    kopija_ploce[kamencic] = "X"
                    kopija_ploce[novo_mjesto] = "1"

                    if (imaLiIkoMill(novo_mjesto, kopija_ploce)):
                        lista_ploca = ukloniKamencic(kopija_ploce, lista_ploca)
                    else:
                        lista_ploca.append(kopija_ploce)
    return lista_ploca


#U slucaju da jedan od igraca ostane sa 3 figure na tabli prelazi se na fazu 3.
def faza23(ploca):
    if (brojKonkretnihPoteza(ploca, "1") == 3):
        return faza3(ploca)
    else:
        return faza2(ploca)

"""Mi procijenjujemo svaki list-cvor koristeci funkciju heruisticke evaluacije, pribavljanjem dobijenih vrijednosti.
Potezi gdje pobjedjuju maksimiziranje igraca su dodjeljeni sa pozitivnom beskonacnoscu, dok su potezi koji dovode 
do pobjede na minimiziranje igraca se dodjeljuje sa negativnom beskonacnoscu."""
def heruistickaEvaluacijaFaza23(ploca):

    brojBelih = brojKonkretnihPoteza(ploca, "1")
    brojCrnih = brojKonkretnihPoteza(ploca, "2")
    mills = brojMogucihMill(ploca, "1")

    evaluacija = 0

    lista_ploca = faza23(ploca)
    brojCrnihPoteza = len(lista_ploca) #Broj poteza koje je odigrao protivnik, nakon svakog naseg poteza

    if brojCrnih <= 2 or brojCrnih == 0:
        return float('inf')
    elif brojBelih <= 2:
        return float('-inf')
    else:
        return 0

def potencijalniMill(pozicija, ploca, igrac):

    susjedne_pozicije = susjednePozicijeNaPloci(pozicija)

    for pozicija in susjedne_pozicije:
        if (ploca[pozicija] == igrac) and (not postojiLiMillZaKonkretnuMatricu(pozicija, ploca, igrac)):
            return True
    return False

"""npr: neka igrac 1 ima zauzete neke pozicije, i igrac 2.
Igrac 1: 00, 09, 10, 12
Igrac 2: 21,22,14,15
Vrsimo provjeru za npr: igraca 2.
Za svaki kamencic u matrici, odnosno svako polje provjeravamo da li se poklapa sa trenutnim igracem, tj. 2
Ukoliko se poklopi (u slucaju pozicija 21, 22, 14, 15) generisemo susjedne pozicije na ploci.
Za svaku poziciju u listi susjednih generisanih pozicija ukoliko se ona poklopi sa prvim igracem, i ukoliko
je ta pozicija zauzeta od strane igraca 2, onda ce on tu teziti da stavi 2 kako bi formirao potencijalni mill.
Ako je u pitanju igrac2 i ako je na poziciji 1 i postoji potencijalni mill za njega, onda takodje uvecavamo broj
potencijalnih dobitaka mill-a."""
def nizKamencicaKojiFormirajuPotencijalniMill(ploca, igrac):
    brojac = 0

    for kamencic in range(len(ploca)):
        if (ploca[kamencic] == igrac):
            susjedne_pozicije = susjednePozicijeNaPloci(kamencic)
            for pozicija in susjedne_pozicije:
                if (igrac == "1"):
                    if (ploca[pozicija] == "2"):
                        ploca[kamencic] = "2"
                        if imaLiIkoMill(kamencic, ploca):
                            brojac += 1
                        ploca[kamencic] = igrac
                else:
                    if (ploca[pozicija] == "1" and potencijalniMill(pozicija, ploca, "1")):
                        brojac += 1

    return brojac