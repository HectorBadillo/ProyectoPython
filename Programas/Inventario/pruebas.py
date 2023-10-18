class Producto:
    """La clase definira todos los
    atributos que tenga un producto
    """
    def __init__(
        self,
        nombre: str,
        marca: str,
        sku: str,
        categoria: str,
        precio: float,
        status: str,
    ) -> None:
        self._nombre = nombre
        self._marca = marca
        self._sku = sku
        self._categoria = categoria
        self._precio = precio
        self._status = status

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        self._nombre = valor

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, valor: str):
        self._marca = valor

    @property
    def sku(self):
        return self._sku

    @sku.setter
    def sku(self, valor: str):
        self._sku = valor

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str):
        self._categoria = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor: float):
        self._precio = valor

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, valor: str):
        self._status = valor


class AdministradorProductos:
    def __init__(
        self, dict_productos_disponibles: dict, dict_productos_no_disponibles: dict
    ) -> None:
        self._dict_productos_disponibles = dict_productos_disponibles
        self._dict_productos_no_disponibles = dict_productos_no_disponibles

    def flujo_inventario(self, opcion: int):
        """Decisiones

        Args:
            opcion (int): Segun la opcion que se
            introduzca se agregara o se eliminara
            un producto o se generara un informe
            de productos
        """
        if opcion == 1:
            # Agregar producto
            nombre = str(input("Nombre: "))
            marca = str(input("Marca: "))
            categoria = str(input("Categoria: "))
            precio = float(input("Precio: "))
            sku = str(input("SKU: "))
            status = str(input("Estado: "))

            producto_obj = Producto(nombre, marca, sku, categoria, precio, status)

            if self._validacion_existencia(sku) is False:
                self._dict_productos_disponibles[sku] = producto_obj
            else:
                print("El producto ya existe.")

        elif opcion == 2:
            # Eliminar producto
            eliminar_sku = input("Ingrese el sku del producto que desea eliminar: ")
            if self._validacion_existencia(eliminar_sku) is True:
                pass
            else:
                print("El producto no existe.")

        else:
            pass

    def _validacion_existencia(self, sku: str):
        """Se evalua si el producto esta o no
        en la lista de productos

        Args:
            sku (str): Es la clave con la que se
            buscaran los productos en el diccionario

        Returns:
            Retorna True si el produccto si existe
            caso contrario retorna False
        """
        if sku in self._dict_productos_disponibles:
            return True
        return False


# Menu
opc = 0
dict_prod_disp = {}
dict_prod_no_disp = {}
administracion_obj = AdministradorProductos(
    dict_prod_disp, dict_prod_no_disp
)

while opc != 4:
    print("\tMENU")
    print("1.Agregar producto\n")
    print("2.Eliminar producto\n")
    print("3.Generar informe\n")
    print("4.Salir\n")
    opc = int(input("Opcion: "))
    if opc in range(1, 4):
        administracion_obj.flujo_inventario(opc)
    elif opc == 4:
        print("Hasta pronto")
    else:
        print("Opcion incorrecta")
