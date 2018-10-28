from igra import *
from unosumatricu import *

odrezano = 0
dostignuta_dubina = 0


class evaluator():
    def __init__(self):
        self.evaluator = 0
        self.ploca = []

"""Alfa je najbolja do sada istrazena opcija pocev od datog cvora pa iduci na gore do korena za maximizer-a tj. 
za igraca (nas). Beta je najbolje istrazena opcija pocev od datog cvora pa iduci na gore do korena za minimizer-a
tj. za racunar (AI). Pretpostavimo da je koren maximizer tj. prvi potez igramo mi. Neka je v inicijalna vrijednost 
za dati cvor. Kod nas tj. maximizer-a ona je -inf (minus beskonacno), za AI je +inf (plus beskonacno).
Ako je v > beta ili v < alfa onda odsijecamo taj dio stabla."""

#Dobijamo trenutno stanje igre (matricu/plocu), sa odredjenom dubinom.
def alfaBetaRezanje(ploca, dubina, igrac, alfa, beta, faza1Bool, heuristika):
    ishod = evaluator()

    global dostignuta_dubina
    dostignuta_dubina += 1

    if dubina != 0:
        trenutno_stanje = evaluator()

        #Ako je u pitanju igrac onda odredjujemo moguce poteze za datu fazu.
        if igrac:

            if faza1Bool:
                moguci_potezi = faza1(ploca)
            else:
                moguci_potezi = faza23(ploca)

        #Ukoliko je u pitanju racunar onda generisemo listu inverznih ploca i shodno njima moguce poteze
        else:
            if faza1Bool:
                moguci_potezi = generisanjeListeInverznihPloca(faza1(InverznaPloca(ploca)))
            else:
                moguci_potezi = generisanjeListeInverznihPloca(faza23(InverznaPloca(ploca)))

        """Kada smo izgenerisali listu mogucih poteza koji se sad nalaze u leaf-ovima, trebamo se kretati od korena
        kako bi odredili koji je to potez najbolji po racunar.
        """
        for potez in moguci_potezi:

            if igrac:

                trenutno_stanje = alfaBetaRezanje(potez, dubina - 1, False, alfa, beta, faza1Bool, heuristika)

                if trenutno_stanje.evaluator > alfa:
                    alfa = trenutno_stanje.evaluator
                    ishod.ploca = potez
            else:

                trenutno_stanje = alfaBetaRezanje(potez, dubina - 1, True, alfa, beta, faza1Bool, heuristika)

                if trenutno_stanje.evaluator < beta:
                    beta = trenutno_stanje.evaluator
                    ishod.ploca = potez

            if alfa >= beta:
                global odrezano
                odrezano += 1
                break

        if igrac:
            ishod.evaluator = alfa
        else:
            ishod.evaluator = beta

    else:
        if igrac:
            ishod.evaluator = heuristika(ploca, faza1Bool)
        else:
            ishod.evaluator = heuristika(InverznaPloca(ploca), faza1Bool)

    return ishod

def minimax(ploca, dubina, igrac, alfa, beta, faza1Bool, heuristika):
    ishod = evaluator()

    global dostignuta_dubina
    dostignuta_dubina += 1

    if dubina != 0:
        trenutno_stanje = evaluator()

        if igrac:
            if faza1Bool:
                moguci_potezi = faza1(ploca)
            else:
                moguci_potezi = faza23(ploca)

        else:
            if faza1Bool:
                moguci_potezi = generisanjeListeInverznihPloca(faza1(InverznaPloca(ploca)))
            else:
                moguci_potezi = generisanjeListeInverznihPloca(faza23(InverznaPloca(ploca)))

        for potez in moguci_potezi:

            if igrac:
                trenutno_stanje = minimax(potez, dubina - 1, False, alfa, beta, faza1Bool, heuristika)

                if trenutno_stanje.evaluator > alfa:
                    alfa = trenutno_stanje.evaluator
                    ishod.ploca = potez
            else:
                trenutno_stanje = minimax(potez, dubina - 1, True, alfa, beta, faza1Bool, heuristika)

                if trenutno_stanje.evaluator < beta:
                    beta = trenutno_stanje.evaluator
                    ishod.ploca = potez

        if igrac:
            ishod.evaluator = alfa
        else:
            ishod.evaluator = beta

    else:
        if igrac:
            ishod.evaluator = heuristika(ploca, faza1Bool)
        else:
            ishod.evaluator = heuristika(ploca, faza1Bool)

    return ishod

def brojRezova():
    global odrezano
    x = odrezano
    odrezano = 0
    return x

def brojSpratova():
    global dostignuta_dubina
    x = dostignuta_dubina
    dostignuta_dubina = 0
    return x