import random
import pandas as pd


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
    df.loc[df['Numero_Cuenta'] == cuenta.numero_cuenta, 'Saldo'] = cuenta.saldo


def iniciar_sesion(df):
    clave = int(input("Ingrese su numero de cuenta: "))


    for key, persona in personas_diccionario.items():
        if clave == persona.numero_cuenta:
            print("Sesion iniciada como: ")
            print(str(persona))
            return persona
        print("Cuenta no encontrada")


def registro(df):
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    numero_cuenta = str(random.randint(10**11, (10**12)-1))
    print(f"Numero de cuenta: {numero_cuenta}")
    nuevo_cliente = Cliente(nombre, apellido, numero_cuenta, 0)
    # Agregar la nueva persona al DataFrame
    nueva_fila = pd.DataFrame({'Nombre': [nuevo_cliente.nombre], 
                               'Apellido': [nuevo_cliente.apellido], 
                               'Numero_Cuenta': [nuevo_cliente.numero_cuenta],
                               'Saldo': [nuevo_cliente.saldo]})
    df = pd.concat([df, nueva_fila], ignore_index=True)
    # Guardar el DataFrame actualizado en el mismo archivo CSV
    df.to_csv("C:\\Users\\psbad\\OneDrive\\Documentos\\Visual Studio Code\\Proyecto Python\\Pandas\\Pruebas\\Clientes.csv", index=False)
    print("Nueva persona agregada y datos actualizados en prueba.csv")


opc = 0
while opc != 3:
    print("Menu")
    print("""
        1. Iniciar Sesion.
        2. Registrar.
        3. Salir
        4. Opciones de .csv
        """)
    opc = int(input("Opcion: "))
    if opc == 1:
        cliente = iniciar_sesion(df)
        menu(cliente)

    elif opc == 2:
        registro(df)
    
    elif opc == 4:
        print("Menu.")
        print("1.Crear .csv")
        print("2.Leer .csv")
        opc_csv = int(input("Opcion: "))
        if opc_csv == 1:
            # Crear un DataFrame con la información de las personas
            data = {'Nombre': [],
                    'Apellido': [],
                    'Numero_Cuenta': [],
                    'Saldo': []}
            df = pd.DataFrame(data)
            df.to_csv("C:\\Users\\psbad\\OneDrive\\Documentos\\Visual Studio Code\\Proyecto Python\\Pandas\\Pruebas\\Clientes.csv", index= False)
        
        elif opc_csv == 2:
            df=pd.read_csv("C:\\Users\\psbad\\OneDrive\\Documentos\\Visual Studio Code\\Proyecto Python\\Pandas\\Pruebas\\Clientes.csv")

            personas_diccionario = {}
            for index, row in df.iterrows():
                persona = Cliente(row['Nombre'], row['Apellido'], row['Numero_Cuenta'], row['Saldo'])
                personas_diccionario[index] = persona

            print(df)
            print("-" * 60 + '\n')

    print("Gracias por operar con nosotros")

df.to_csv("C:\\Users\\psbad\\OneDrive\\Documentos\\Visual Studio Code\\Proyecto Python\\Pandas\\Pruebas\\Clientes.csv", index=False)
