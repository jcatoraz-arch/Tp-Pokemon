class Stack:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        if len(self.items) >= 5:
            self.items.pop(0)
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def esta_vacia(self):
        return len(self.items) == 0