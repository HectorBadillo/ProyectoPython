from Clases import *
import pandas as pd
from pathlib import Path

ruta_ejecutivos = Path(Path.home(), "registro_ejecutivos.csv")
ruta_clientes = Path(Path.home(), "registro_clientes.csv")

class Banco:

    @staticmethod
    def generar_csv_clientes():
        # Crear un DataFrame con la información de los clientes
        data = {'Nombre': [],
                'Apellido': [],
                'Fecha': [],
                'Correo': [],
                'Telefono': [],
                'Contrasenia': [],
                'Numero_Cuenta': [],
                'Saldo': []}
        df = pd.DataFrame(data)
        df.to_csv(ruta_clientes, index = False)
        print(type(df))
        return df

    def registrar_cliente(self, usuario:Cliente, df:pd):
            new_row =pd.DataFrame ({'Nombre': [usuario.nombre],
            'Apellido': [usuario.apellido],
            'Fecha': [usuario.fecha],
            'Correo': [usuario.correo],
            'Telefono': [usuario.telefono],
            'Contrasenia': [usuario.contrasenia],
            'Numero_Cuenta': [usuario.numero_cuenta],
            'Saldo': [usuario.saldo]})
            df = pd.concat([df, new_row], ignore_index = True)
            df.to_csv(ruta_clientes, index = False)
            return df 

    def lectura_clientes(self):
        """Leera y guardara todos los datos del archivo .csv

        Returns:
            dict{Numero_cuenta: objeto cliente}
        """
        df = pd.read_csv(ruta_clientes)
        personas_diccionario = {}
        for index, row in df.iterrows():
            usuario = Cliente(row['Nombre'], 
                                row['Apellido'], 
                                row['Fecha'], 
                                row['Correo'],
                                row['Telefono'],
                                row['Contrasenia'],
                                row['Numero_Cuenta'],
                                row['Saldo'])
            personas_diccionario[int(row['Numero_Cuenta'])] = usuario
        print(df)
        print("-" * 60 + '\n')
        return df,personas_diccionario
    
    def guardar_mov_cliente(self, usuario: Cliente, df: pd):
        df.loc[df['Numero_Cuenta'] == usuario.numero_cuenta, 'Nombre'] = usuario.nombre
        df.loc[df['Numero_Cuenta'] == usuario.numero_cuenta, 'Apellido'] =usuario.apellido
        df.loc[df['Numero_Cuenta'] == usuario.numero_cuenta, 'Correo'] =usuario.correo
        df.loc[df['Numero_Cuenta'] == usuario.numero_cuenta, 'Telefono'] =usuario.telefono
        df.loc[df['Numero_Cuenta'] == usuario.numero_cuenta, 'Contrasenia'] =usuario.contrasenia
        df.loc[df['Numero_Cuenta'] == usuario.numero_cuenta, 'Saldo'] =usuario.saldo 
        return df

    
    @staticmethod
    def generar_csv_ejecutivos():
        # Crear un DataFrame con la información de los ejecutivos
        data = {'Nombre': [],
                'Apellido': [],
                'Fecha': [],
                'Correo': [],
                'Telefono': [],
                'Contrasenia': [],
                'Numero_Cuenta': [],
                'Puesto': [],
                'Sucursal': []}
        df = pd.DataFrame(data)
        df.to_csv(ruta_ejecutivos, index = False)
        print(type(df))
        return df
    
    def registrar_ejecutivo(self, usuario:Ejecutivo, df:pd):
            new_row =pd.DataFrame ({'Nombre': [usuario.nombre],
            'Apellido': [usuario.apellido],
            'Fecha': [usuario.fecha],
            'Correo': [usuario.correo],
            'Telefono': [usuario.telefono],
            'Contrasenia': [usuario.contrasenia],
            'Numero_Cuenta': [usuario.numero_cuenta],
            'Puesto': [usuario.puesto],
            'Sucursal': [usuario.sucursal]})
            df = pd.concat([df, new_row], ignore_index = True)
            df.to_csv(ruta_ejecutivos, index = False)
            return df
    
    def lectura_ejecutivos(self):
        """Leera y guardara todos los datos del archivo .csv

        Returns:
            dict{Numero_cuenta: objeto ejecutivo}
        """
        df = pd.read_csv(ruta_ejecutivos)
        personas_diccionario = {}
        for index, row in df.iterrows():
            usuario = Ejecutivo(row['Nombre'], 
                                row['Apellido'], 
                                row['Fecha'], 
                                row['Correo'],
                                row['Telefono'],
                                row['Contrasenia'],
                                row['Numero_Cuenta'],
                                row['Puesto'],
                                row['Sucursal'])
            personas_diccionario[int(row['Numero_Cuenta'])] = usuario
        print(df)
        print("-" * 60 + '\n')
        return df,personas_diccionario
    
    def guardar_mov_ejecutivos(self, usuario: Ejecutivo, df: pd):
        df.loc[df['Numero_Cuenta'] == usuario.numero_cuenta, 'Nombre'] = usuario.nombre
        df.loc[df['Numero_Cuenta'] == usuario.numero_cuenta, 'Apellido'] =usuario.apellido
        df.loc[df['Numero_Cuenta'] == usuario.numero_cuenta, 'Correo'] =usuario.correo
        df.loc[df['Numero_Cuenta'] == usuario.numero_cuenta, 'Telefono'] =usuario.telefono
        df.loc[df['Numero_Cuenta'] == usuario.numero_cuenta, 'Contrasenia'] =usuario.contrasenia
        df.loc[df['Numero_Cuenta'] == usuario.numero_cuenta, 'Puesto'] =usuario.puesto
        df.loc[df['Numero_Cuenta'] == usuario.numero_cuenta, 'Sucursal'] =usuario.sucursal 
        return df

banamex = Banco()

'''cliente1 = Cliente("Juan", "Perez", "1990-05-15", "juan@example.com", "555-1234", "clave123", 1001, 1500.0)
cliente2 = Cliente("Maria", "Gomez", "1985-08-22", "maria@example.com", "555-5678", "contraseña456", 1002, 2000.0)
cliente3 = Cliente("Carlos", "Lopez", "1978-11-10", "carlos@example.com", "555-9876", "secreto789", 1003, 3000.0)
cliente4 = Cliente("Laura", "Garcia", "1995-03-28", "laura@example.com", "555-4321", "clave123", 1004, 2500.0)
cliente5 = Cliente("Pedro", "Rodriguez", "1982-07-03", "pedro@example.com", "555-8765", "contraseña789", 1005, 1800.0)

lista = [cliente2,cliente3,cliente4,cliente5]
for cliente in lista:
    df = banamex.registrar_cliente(cliente,df)'''

df, diccionario_personas = banamex.lectura_clientes()
cliente = diccionario_personas[1001]

cliente.nombre = 'Hector'
cliente.apellido = 'Badillo'
df = banamex.guardar_mov_cliente(cliente,df)

df.to_csv(ruta_clientes, index=False)