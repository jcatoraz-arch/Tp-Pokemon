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