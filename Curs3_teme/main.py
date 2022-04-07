from f_recursive.modul import adunare, adunareimpara, adunarepara

def calculsuma():
    lista = ["pisica", 1, -3, 2.5, 5, 1337, -69, "ff15", "python", "sarpe", 26, 40]
    lista_numere = []
    for x in lista:
        if isinstance(x,int) and not isinstance(x,bool):
            lista_numere.append(x)
    suma = sum(lista_numere)
    print(f"Suma parametrilor care reprezintă numere întregi sau reale este: {suma}")

def citit_tastatura():
    while True:
        try:
            valoare = int(input("Introdu ceva: "))
        except ValueError:
            print(0)
            break
        else:
            print(valoare)
            break

def suma_modul():
    n = int(input("Va rugam introduceti valoarea lui \"n\": "))

    print("Adunare para: " + str(adunarepara(n)))
    print("Adunare impara: " + str(adunareimpara(n)))
    print("Suma numerelor: " + str(adunare(n)))

#calculsuma()
#citit_tastatura()
#suma_modul()

