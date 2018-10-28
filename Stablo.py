class cvorStabla(object):
    def __init__(self, element = None, roditelj = None):
        self.element = element
        self.roditelj = roditelj
        self.djeca = []

    def jeLiKoren(self):
        return self.roditelj == None

    def jeLiList(self): #Cvor je list/leaf ukoliko nema dece
        return len(self.djeca) == 0

    def imaLiDijete(self):
        return len(self.djeca) > 0

    def preorder(self):
        print (self.element)
        for dijete in self.djeca:
            dijete.preorder()

    def postorder(self):
        for dijete in self.djeca:
            dijete.postorder()
        print (self.element)

    def Roditelj(self):
        return self.roditelj.element

    def Djeca(self):
        lista_djeca = []
        for svaki_element in self.djeca:
            lista_djeca.append(svaki_element.element)
        return lista_djeca

class Stablo(object):
    def __init__(self, koren = None):
        self.koren = koren

    def dubina(self, cvor): #Moze se koristiti za odredjeni cvor; dubina zadnjeg cvora hijerarhijski je dubina stabla
        if cvor.jeLiKoren():
            return 0
        else:
            return 1 + self.dubina(cvor.roditelj)

    def preorder(self):
        self.koren.preorder()

    def postorder(self):
        self.koren.postorder()

    def breadth_first(self):
        brojElemenata = 0
        Q = Red() #Napravi novi prazan red Q
        Q.enqueue(self.koren) #Dodaj korenski cvor u red
        while not Q.is_empty(): #Dok red nije prazan
            cvor = Q.dequeue()
            print (cvor.element)

            for dijete in cvor.djeca:
                Q.enqueue(dijete)
                brojElemenata += 1
        return brojElemenata

    def __len__(self):
        brojElemenata = 0
        Q = Red()  # Napravi novi prazan red Q
        Q.enqueue(self.koren)  # Dodaj korenski cvor u red
        while not Q.is_empty():  # Dok red nije prazan
            cvor = Q.dequeue()

            for dijete in cvor.djeca:
                Q.enqueue(dijete)
                brojElemenata += 1
        return brojElemenata + 1

    def is_empty(self):
        return self.breadth_first() == 0

class prazanRed(Exception):
    pass

class Red(object):
    inicijalniKapacitet = 20

    def __init__(self):
        self.elementi = [None] * self.inicijalniKapacitet
        self.velicina = 0
        self.prviEl = 0 #indeks prvog elementa u redu

    def __len__(self):
        return self.velicina

    def is_empty(self):
        return self.velicina == 0

    def prvi(self):
        if self.is_empty():
            raise prazanRed('red je prazan.')
        return self.elementi[self.prviEl]

    def povecajKapacitet(self, kapacitet):
        stari = self.elementi
        self.elementi = [None] * kapacitet
        premotanaKonf = self.prviEl
        for svaki in range(self.velicina):
            self.elementi[svaki] = stari[premotanaKonf]
            premotanaKonf = (1 + premotanaKonf) % len(stari)
        self.prviEl = 0

    def enqueue(self, element):
        if self.velicina == len(self.elementi):
            self.povecajKapacitet(2 * len(self.elementi))
        pomocni = (self.prviEl + self.velicina) % len(self.elementi)
        self.elementi[pomocni] = element
        self.velicina += 1

    def dequeue(self):
        if self.is_empty():
            raise prazanRed('red je prazan.')
        ans = self.elementi[self.prviEl]
        self.elementi[self.prviEl] = None
        self.prviEl = (self.prviEl + 1) % len(self.elementi)
        self.velicina -= 1
        return ans