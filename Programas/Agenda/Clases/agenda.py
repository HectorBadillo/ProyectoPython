from contacto import *


class Agenda:
    def __init__(self) -> None:
        self.lista_contactos = []

    def agregar_contacto(self, 
                         contacto) -> None:
        self.lista_contactos.append(contacto)

    def eliminar_contacto(self,eliminar_contacto):
        for contacto in self.lista_contactos:
            if (eliminar_contacto.no_telefono == contacto.no_telefono):
                self.lista_contactos.remove(contacto)    

    def mostrar_contactos(self):
        for contacto in self.lista_contactos:
            contacto.mostrar_contacto()
            print("\n")


contacto1 = Contacto("Hector","chelito@mail","3401")
contacto2 = Contacto("Wendy","Flores@gmail","2757")
contacto3 = Contacto("Ivan","capri@gmail","4488")
contacto4 =  Contacto("Hector","chelito@mail","3401")
agenda1 = Agenda()

agenda1.agregar_contacto(contacto1)
agenda1.agregar_contacto(contacto2)
agenda1.agregar_contacto(contacto3)
agenda1.agregar_contacto(contacto4)
agenda1.mostrar_contactos()

print("Eliminando el contacto 1\n")

agenda1.eliminar_contacto(contacto1)
agenda1.mostrar_contactos()

print("Eliminando el contacto 2\n")

agenda1.eliminar_contacto(contacto2)
agenda1.mostrar_contactos()

print("Eliminando el contacto 3\n")

agenda1.eliminar_contacto(contacto3)
agenda1.mostrar_contactos()
