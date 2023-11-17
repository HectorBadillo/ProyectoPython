class Pajaro:

    alas = True
    #Metodos de instancia

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("Pio, mi color es {}".format(self.color))

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()

    def pintar_negro(self):
        self.color = "Negro"
        print(f"Ahora el pajaro es {self.color}")

    #Metodo de clase
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False    #No piede acceder a atributos de instancia    
        print(Pajaro.alas)  #pero si de clase

    #Metodos estaticos
    @staticmethod
    def mirar():        #No modifican ni instancia ni clase
        print("El pajaro mira")

    
#Metodos de instancia
piolin = Pajaro("Amarillo", "Canario")
piolin.volar(50)
piolin.pintar_negro()
piolin.alas = False
print(piolin.alas)
print("-" * 30 + "\n")

#Metodos de clase
Pajaro.poner_huevos(3)      
print("-" * 30 + "\n")

#Metodos estaticos
Pajaro.mirar()