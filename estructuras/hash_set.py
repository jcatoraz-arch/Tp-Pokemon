class HashSet:
    def __init__(self, tamaño=10):
        self.tamaño = tamaño
        self.buckets = [[] for _ in range(tamaño)]

    def funcion_hash(self, elemento):
        return hash(elemento) % self.tamaño

    def agregar(self, elemento):
        indice = self.funcion_hash(elemento)
        if elemento not in self.buckets[indice]:
            self.buckets[indice].append(elemento)

    def contiene(self, elemento):
        indice = self.funcion_hash(elemento)
        return elemento in self.buckets[indice]

    def valores(self):
        elementos = []
        for bucket in self.buckets:
            for elemento in bucket:
                elementos.append(elemento)
        return elementos