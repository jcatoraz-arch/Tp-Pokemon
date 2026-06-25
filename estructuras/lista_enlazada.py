from estructuras.nodo import Nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def mostrar(self):
        actual = self.cabeza

        if actual is None:
            print("La PC esta vacia")
            return

        while actual:
            print(actual.dato)
            actual = actual.siguiente

    def eliminar_inicio(self):
        if self.cabeza is None:
            return None

        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente

        return dato

    def a_lista(self):
        lista = []
        actual = self.cabeza

        while actual:
            lista.append(actual.dato)
            actual = actual.siguiente

        return lista

    def desde_lista(self, lista):
        self.cabeza = None

        for pokemon in reversed(lista):
            self.agregar_inicio(pokemon)