class Animal:

    def __init__(self, edad, color) -> None:
        self.edad = edad
        self.color = color
        

    def nacer(self):
        print("Este animal ha nacido")


class Pajaro(Animal):
    pass



piolin = Pajaro(2,"Amarillo")
piolin.nacer()
print(piolin.color)