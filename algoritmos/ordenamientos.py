def bubble_sort_nombre(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - 1 - i):
            if lista[j].nombre > lista[j + 1].nombre:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def insertion_sort_tipo(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j].tipo > actual.tipo:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

def quick_sort_poder(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    mayores = []
    iguales = []
    menores = []
    for pokemon in lista:
        if pokemon.poder_combate > pivote.poder_combate:
            mayores.append(pokemon)
        elif pokemon.poder_combate < pivote.poder_combate:
            menores.append(pokemon)
        else:
            iguales.append(pokemon)
    return quick_sort_poder(mayores) + iguales + quick_sort_poder(menores)