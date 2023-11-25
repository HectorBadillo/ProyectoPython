from Ejecutivo import CrearCuenta

class Cliente(CrearCuenta):
    def __init__(self, nombre: str, apellido: str, fecha: str, correo: str, telefono: str, contrasenia: str, numero_cuenta, saldo:float, apartado:float):
        super().__init__(nombre, apellido, fecha, correo, telefono, contrasenia, numero_cuenta)
        self.saldo = saldo
        self.apartado = apartado

'''    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        if not isinstance(nuevo_saldo, float):
            raise ValueError("El valor ingresado no es un número")
        self._saldo = nuevo_saldo
    @property
    def contrasenia(self):
        return self._contrasenia

    @contrasenia.setter
    def contrasenia(self, nueva_contrasenia):
        if not isinstance(nueva_contrasenia, str):
            raise ValueError("El valor ingresado no es un número")
        self._contrasenia = nueva_contrasenia

    @property
    def numero_cuenta(self):
        return self._numero_cuenta

    @numero_cuenta.setter
    def numero_cuenta(self, nuevo_numero_cuenta):
        if not isinstance(nuevo_numero_cuenta, float):
            raise ValueError("El valor ingresado no es un número")
        self._Numero_cuenta = nuevo_numero_cuenta

'''



