class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("Ja Ja")
    
    def hablar(self):
        print("Que tal?")



class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.hablar()       #Primero Padre por orden
mi_nieto.reir()
print(Nieto.__mro__)    #Orden con la que busca