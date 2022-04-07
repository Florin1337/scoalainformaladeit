def adunarepara(m):
    m = m + 1
    suma = 0
    for i in range(m):
        if i % 2 == 0:
            suma = suma + i

    return suma

def adunareimpara(m):
    m = m + 1
    suma = 0
    for i in range(m):
        if i % 2 != 0:
            suma = suma + i

    return suma

def adunare(m):
    suma = 0
    for i in range(m + 1):
        suma = suma + i

    return suma
