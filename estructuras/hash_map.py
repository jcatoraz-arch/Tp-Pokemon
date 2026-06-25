class HashMap:
    def __init__(self, tamaño=10):
        self.tamaño = tamaño
        self.buckets = [[] for _ in range(tamaño)]

    def funcion_hash(self, clave):
        return clave % self.tamaño

    def insertar(self, clave, valor):
        indice = self.funcion_hash(clave)
        bucket = self.buckets[indice]

        for i in range(len(bucket)):
            if bucket[i][0] == clave:
                bucket[i] = (clave, valor)
                return

        bucket.append((clave, valor))

    def obtener(self, clave):
        indice = self.funcion_hash(clave)
        bucket = self.buckets[indice]

        for clave_guardada, valor in bucket:
            if clave_guardada == clave:
                return valor

        return None

    def valores(self):
        lista_valores = []

        for bucket in self.buckets:
            for clave, valor in bucket:
                lista_valores.append(valor)

        return lista_valores