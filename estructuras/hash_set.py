class HashSet:
    def __init__(self):
        self.conjunto = set()

    def agregar(self, elemento):
        self.conjunto.add(elemento)

    def contiene(self, elemento):
        return elemento in self.conjunto

    def valores(self):
        return self.conjunto