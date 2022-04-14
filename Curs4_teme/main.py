class Fractie:

    def __init__(self, numitor, numarator):
        self.numitor = numitor
        self.numarator = numarator


    def __str__(self):
        return str(self.numitor)+"/"+str(self.numarator)


    def __add__(self, other):
        if str(other).find("/") == -1:
            other = Fractie(other)
        n = (self.numitor * other.numarator) + (self.numarator * other.numitor)
        d = (self.numarator * other.numarator)
        result = Fractie(n, d)
        adunare = n + d
        return adunare


    def __sub__(self, other):
        if str(other).find("/") == -1:
            other = Fractie(other)
        n = (self.numitor * other.numarator) + (self.numarator * -1 * other.numitor)
        d = (self.numarator * other.numarator)
        result = Fractie(n, d)
        scadere = n + d
        return scadere


    def invers(self):
        self.numitor, self.numarator = self.numarator, self.numitor
        return self.numitor, self.numarator



fractie = (Fractie(6,9))
print(fractie)
print(Fractie(6,9) + Fractie(9,6))
print(Fractie(6,9) - Fractie(9,6))
print(fractie.invers())