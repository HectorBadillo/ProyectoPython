import random

class Usuario:
    def __init__(self, nombre:str, apellido:str, fecha:str, correo:str ,telefono:str):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha = fecha
        self.correo = correo
        self.telefono = telefono

class CrearCuenta(Usuario):
    
    def __init__(self, nombre: str, apellido: str, fecha: str, correo: str, telefono: str, contrasenia: str , numero_cuenta: int ):
        super().__init__(nombre, apellido, fecha, correo, telefono)
        self.contrasenia = contrasenia or self.generar_contrasenia()
        self.numero_cuenta = numero_cuenta or self.asignar_numero_cuenta()

    def generar_contrasenia(self):
        contrasenia = ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=8))
        print("Tu contraseña es:", contrasenia)
        return contrasenia

    def asignar_numero_cuenta(self):
        # Generar un número de cuenta y asegurarse de que no exista ya en el sistema
        nuevo_numero_cuenta = random.randint(100000, 999999)
        print(f"Número de cuenta asignado: {nuevo_numero_cuenta}")
        return nuevo_numero_cuenta


class Ejecutivo(CrearCuenta):
    def __init__(self, nombre: str, apellido: str, fecha: str, correo: str, telefono: str, contrasenia: str , numero_cuenta: int , puesto:str, sucursal:str):
        super().__init__(nombre, apellido, fecha, correo, telefono, contrasenia, numero_cuenta)
        self.puesto = puesto
        self.sucursal = sucursal

class Cliente(CrearCuenta):
    def __init__(self, nombre: str, apellido: str, fecha: str, correo: str, telefono: str, contrasenia: str, numero_cuenta: int, saldo: float):
        super().__init__(nombre, apellido, fecha, correo, telefono, contrasenia, numero_cuenta)
        self.saldo = saldo


ejecutivo1 = Ejecutivo("Nombre", "Apellido", "Fecha", "Correo", "Telefono", "Contrasenia", 123456, "Gerente", "Sucursal A")

