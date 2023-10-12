class MiIterador:
    def __init__(self, limite):
        self.limite = limite

    def __iter__(self):
        return self

    def __next__(self):
        if self.limite <= 0:
            raise StopIteration
        self.limite -= 1
        return self.limite

# Usar la clase iteradora en un bucle for
mi_iterador = MiIterador(5)
for elemento in mi_iterador:
    print(elemento)
