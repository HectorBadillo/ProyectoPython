import random
class Persona:
    def __init__(self, nombre: str, apellido: str) -> None:
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre: str, apellido: str, numero_cuenta : str, saldo : str) -> None:
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def __str__(self) -> str:
        return f"""
        Usuario:            {self.nombre} {self.apellido}
        Numero de cuenta:   {self.numero_cuenta}
        Saldo:              ${self.saldo}
        """
    
    def depositar(self, deposito: int):
        self.saldo += int(deposito)
    
    def retirar(self, retiro: int):
        if retiro > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= int(retiro)

clientes =[]

def inicio():
    opc = 0
    while(opc != 3):
        print("\nMENU")
        print("""
            1.Iniciar sesion.
            2.Registrarse.
            3.Salir
            """)
        opc = int(input("Opcion: "))
        if opc == 1:
            cuenta = iniciar_sesion()
            print(cuenta)
            menu(cuenta)
        elif opc == 2:
            registro()

def menu(cuenta: Cliente):
    opc = 0
    while(opc != 3):
        print("Menu")
        print("""
            1.Depositar.
            2.Retirar.
            3.Cerrar sesion.
                """)
        opc = int(input("Opcion: "))
        if opc == 1:
            deposito = int(input("Deposito: "))
            cuenta.depositar(deposito)
            print(cuenta)
        elif opc == 2:
            retiro = int(input("Retiro: "))
            cuenta.retirar(retiro)
            print(cuenta)

def registro():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    numero_cuenta = str(random.randint(10**11, (10**12)-1))
    print(f"Numero de cuenta: {numero_cuenta}")
    nuevo_cliente = Cliente(nombre, apellido, numero_cuenta, 0)
    clientes.append(nuevo_cliente)

def iniciar_sesion():
    numero_cuenta = input("Numero de Cuenta: ")
    for cuenta in clientes:
        if numero_cuenta == cuenta.numero_cuenta:
            return cuenta

inicio()