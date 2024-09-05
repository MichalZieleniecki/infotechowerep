class Film:
    def __init__(self):
        self._tytul = ""
        self._liczbaWypozyczen = 0

    def setTytul(self, t):
        self._tytul = t

    def getTytul(self):
        return self._tytul

    def getLiczbaEypozyczen(self):
        return self._liczbaWypozyczen
    def inkrementacja(self):
        self._liczbaWypozyczen += 1


film1 = Film()

film1.setTytul("Rambo. Pierwsza krew.")
print(film1.getTytul(), film1.getLiczbaEypozyczen())
film1.inkrementacja()
print(film1.getTytul(), film1.getLiczbaEypozyczen())