from estructuras.nodo import Nodo

class Queue:
    def __init__(self):
        self.frente = None
        self.final = None

    def esta_vacia(self):
        return self.frente is None

    def encolar(self, dato):
        nuevo = Nodo(dato)

        if self.esta_vacia():
            self.frente = nuevo
            self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo

    def desencolar(self):
        if self.esta_vacia():
            return None

        dato = self.frente.dato
        self.frente = self.frente.siguiente

        if self.frente is None:
            self.final = None

        return dato