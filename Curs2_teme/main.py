lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

def asc_desc():
    lista_asc = sorted(lista)
    lista_desc = sorted(lista, reverse=True)

    return print(lista_asc), print(lista_desc)

def par_impar():
    lista_asc = sorted(lista)
    lista_par = lista_asc
    lista_impar = lista_asc
    print(lista_par[::2])
    print(lista_impar[1::2])

def multiplu():
    for nr in lista:
        if (nr % 3 == 0):
            print(nr, end=" ")

print(lista)
print(asc_desc())
print(par_impar())
print(multiplu())