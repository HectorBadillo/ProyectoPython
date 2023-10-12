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

class MiIterador:
    def __init__(self, limite):
        self.limite = limite
        self.valor = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.valor < self.limite:
            resultado = self.valor
            self.valor += 1
            return resultado
        else:
            raise StopIteration

# Usar la clase iteradora en un bucle for
mi_iterador = MiIterador(5)
for elemento in mi_iterador:
    print(elemento)
