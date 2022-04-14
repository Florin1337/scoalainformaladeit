class Fractie:

    def __init__(self, numitor, numarator):
        self.numitor = numitor
        self.numarator = numarator

    def __str__(self):
        return str(self.numitor)+"/"+str(self.numarator)

    def __add__(self):
        pass

    def invers(self):
        pass

fractie = Fractie(12, 21)
print(fractie)