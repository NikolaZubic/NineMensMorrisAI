from igra import *

"""Heuristika koja vraca neku vrijednost u ovisnosti od toga koliko se nalazi kamencica na ploci, u sustini bitna nam 
je kod toga da odredjuje da li smo dovoljno "blizu" kraju igre."""
def brojKamencicaNaPlociHeuristika(ploca, faza1Bool):
    #evaluacija = 0

    brojOdigranihPotezaIgrac = brojKonkretnihPoteza(ploca, "1")
    brojOdigranihPotezaAI = brojKonkretnihPoteza(ploca, "2")

    moguciPoteziAI = 0

    if not faza1Bool:
        moguciPoteziCrni = len(faza23(ploca))

    if not faza1Bool:
        if brojOdigranihPotezaAI <= 2 or moguciPoteziCrni == 0:
            evaluacija = float('inf')
        elif brojOdigranihPotezaIgrac <= 2:
            evaluacija = float('-inf')
        else:
            evaluacija = 200 * (brojOdigranihPotezaIgrac - brojOdigranihPotezaAI)
    else:
        evaluacija = 100 * (brojOdigranihPotezaIgrac - brojOdigranihPotezaAI)

    return evaluacija



"""Heuristika koja vraca neku vrijednost u ovisnosti od toga koliki je broj potencijalnih MILL-ova na ploci u 
odredjenom trenutku(stanju igre)."""
def potencijalniMillHeuristika(ploca, faza1Bool):
    evaluacija = 0

    brojOdigranihPotezaIgrac = brojKonkretnihPoteza(ploca, "1")
    brojOdigranihPotezaAI = brojKonkretnihPoteza(ploca, "2")

    brojMogucihMillIgrac = brojMogucihMill(ploca, "1")
    brojMogucihMillAI = brojMogucihMill(ploca, "2")

    moguciPoteziAI = 0

    if not faza1Bool:
        moguciPoteziCrni = len(faza23(ploca))

    potencijalniMillIgrac = nizKamencicaKojiFormirajuPotencijalniMill(ploca, "1")
    potencijalniMillAI = nizKamencicaKojiFormirajuPotencijalniMill(ploca, "2")

    if not faza1Bool:
        if brojOdigranihPotezaAI <= 2 or moguciPoteziCrni == 0:
            evaluacija = float('inf')
        elif brojOdigranihPotezaIgrac <= 2:
            evaluacija = float('-inf')
        else:
            if (brojOdigranihPotezaIgrac < 4):
                evaluacija += 100 * brojMogucihMillIgrac
                evaluacija += 200 * potencijalniMillAI
            else:
                evaluacija += 200 * brojMogucihMillIgrac
                evaluacija += 100 * potencijalniMillAI

    else:
        if brojOdigranihPotezaIgrac < 4:
            evaluacija += 100 * brojMogucihMillIgrac
            evaluacija += 200 * potencijalniMillAI
        else:
            evaluacija += 200 * brojMogucihMillIgrac
            evaluacija += 100 * potencijalniMillAI

    return evaluacija



"""Heuristika koja igra u fazi 2,3 bitnu ulogu za racunar jer vraca neku vrijednost u ovisnosti od toga koliko se 
nalazi kamencica na ploci i koji su to potencijalni MILL koji bi mogli da se formiraju (dobri po racunar)."""
def CovekVS_AI_Heuristika(ploca, faza1Bool):
    evaluacija = 0

    brojOdigranihPotezaIgrac = brojKonkretnihPoteza(ploca, "1")
    brojOdigranihPotezaAI = brojKonkretnihPoteza(ploca, "2")

    brojMogucihMillIgrac = brojMogucihMill(ploca, "1")
    brojMogucihMillAI = brojMogucihMill(ploca, "2")

    moguciPoteziIgrac = 0
    moguciPoteziAI = 0

    if not faza1Bool:
        moguciPoteziCrni = len(faza23(ploca))

    potencijalniMillIgrac = nizKamencicaKojiFormirajuPotencijalniMill(ploca, "1")
    potencijalniMillAI = nizKamencicaKojiFormirajuPotencijalniMill(ploca, "2")

    if not faza1Bool:
        if brojOdigranihPotezaAI <= 2 or moguciPoteziCrni == 0:
            evaluacija = float('inf')
        elif brojOdigranihPotezaIgrac <= 2:
            evaluacija = float('-inf')
        else:
            if (brojOdigranihPotezaIgrac < 4):
                evaluacija += 100 * brojMogucihMillIgrac
                evaluacija += 200 * potencijalniMillAI
            else:
                evaluacija += 200 * brojMogucihMillIgrac
                evaluacija += 100 * potencijalniMillAI
            evaluacija -= 25 * moguciPoteziCrni
            evaluacija += 50 * (brojOdigranihPotezaIgrac - brojOdigranihPotezaAI)
    else:
        if brojOdigranihPotezaIgrac < 4:
            evaluacija += 100 * brojMogucihMillIgrac
            evaluacija += 200 * potencijalniMillAI
        else:
            evaluacija += 200 * brojMogucihMillIgrac
            evaluacija += 100 * potencijalniMillAI
        evaluacija -= 25 * moguciPoteziCrni
        evaluacija += 50 * (brojOdigranihPotezaIgrac - brojOdigranihPotezaAI)

    return evaluacija