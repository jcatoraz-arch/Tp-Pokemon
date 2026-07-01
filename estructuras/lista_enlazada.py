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

    def transferir_por_id(self, id):
        if self.cabeza is None:
            return None
        if self.cabeza.dato.id == id:
            dato = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            return dato
        anterior = self.cabeza
        actual = self.cabeza.siguiente
        while actual is not None:
            if actual.dato.id == id:
                dato = actual.dato
                anterior.siguiente = actual.siguiente
                return dato
            anterior = actual
            actual = actual.siguiente
        return None