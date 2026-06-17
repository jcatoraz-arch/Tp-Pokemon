class HashMap:
    def __init__(self):
        self.tabla = {}

    def insertar(self, clave, valor):
        self.tabla[clave] = valor

    def obtener(self, clave):
        return self.tabla.get(clave)

    def valores(self):
        return self.tabla.values()