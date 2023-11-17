class Pajaro:

    alas = True                         #Atributo de clase

    def __init__(self, color, especie):
        self.atributo_color = color     #Atributos de instancia
        self.atributo_especie = especie

mi_pajaro = Pajaro("Negro", "Agaporni")


print(mi_pajaro.atributo_color)
print(mi_pajaro.atributo_especie)
print(Pajaro.alas)
print(mi_pajaro.alas)