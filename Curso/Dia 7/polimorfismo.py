class Vaca:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + "dice muuuu")
    
class Oveja:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + "dice beee")

vaca1 = Vaca("Aurora")
oveja1 = Oveja("Nube")

vaca1.hablar()
oveja1.hablar()
print("-" * 40 + "\n")

animales = [vaca1, oveja1]
for animal in animales:
    animal.hablar()
print("-" * 40 + "\n")

def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
animal_habla(oveja1)