class Persona:
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0) -> None:
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self) -> str:
        return f"Cliente: {self.nombre} {self.apellido}\nBalance de cuenta {self.numero_cuenta}: ${self.balance}"
    
    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print("Deposito aceptado")

    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro exitoso")
        else:
            print("Saldo insuficiente")

def crear_cliente():
    nombre_cl = input("Nombre: ")
    apellido_cl = input("Apellido: ")
    numero_cuenta = input("Numero de cuenta: ")
    cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta)
    return cliente

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opc = 0
    while opc != 'S':
        print("Elige: Depositar(D), Retirar(R), Salir(S)")
        opc = input()

        if opc == "D":
            monto_deposito = int(input("Deposito: "))
            mi_cliente.depositar(monto_deposito)
        elif opc == "R":
            monto_retiro = int(input("Retiro: "))
            mi_cliente.retirar(monto_retiro)
        print(mi_cliente)
    print("Gracias por operar")

inicio()
