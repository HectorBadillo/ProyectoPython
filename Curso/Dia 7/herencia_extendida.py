class Animal:

    def __init__(self, edad, color) -> None:
        self.edad = edad
        self.color = color
        

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):
    #Atributos nuevos
    def __init__(self, edad, color, altura_vuelo) -> None:
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo


    #Metodo modificado
    def hablar(self):
        print("pio")

    #Metodo nuevo
    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")



piolin = Pajaro(3,"Amarillo",60)
#Metodo heredado
piolin.nacer()

#Metodo modificado
piolin.hablar()

#Metodo nuevo
piolin.volar(50)


