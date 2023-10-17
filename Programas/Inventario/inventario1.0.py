class Producto:
    def __init__(self, nombre:str, marca:str, sku:str, categoria:str, precio:float, status:str) -> None:
        self._nombre = nombre
        self._marca = marca
        self._sku = sku
        self._categoria = categoria
        self._precio = precio
        self._status = status
    
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self,valor:str):
        self._status = valor

class AdministradorProductos:
    def __init__(self, dict_productos_disponibles:dict, dict_productos_no_disponibles:dict) -> None:
        self._dict_productos_disponibles = dict_productos_disponibles
        self._dict_productos_no_disponibles = dict_productos_no_disponibles
    
    def flujo_inventario(self, opcion:int):
        if opcion == 1:
            nombre = str(input('Nombre: '))
            marca = str(input('Marca: '))
            categoria = str(input('Categoria: '))
            precio = float(input('Precio: '))
            sku = str(input('SKU: '))
            status = str(input('Estado: '))

            producto_obj = Producto(nombre, marca, sku, categoria, precio,status)
            print(producto_obj.__dict__)
            
        elif opcion == 2:
            pass
        else:
            pass

#Menu
opc = 0
dict_productos_disponibles = {}
dict_productos_no_disponibles = {}
administracion_obj = AdministradorProductos(dict_productos_disponibles, dict_productos_no_disponibles)

while(opc != 4):
    print('\tMENU') 
    print('1.Agregar producto\n')
    print('2.Eliminar producto\n')
    print('3.Generar informe\n')
    print('4.Salir\n')
    opc = int(input('Opcion: '))
   
    match opc:
        case 1:
            print("Agregar Producto")
            administracion_obj.flujo_inventario(opc)
        case 2:
            print("Elimiar Producto")
        case 3:
            print("Generar informe")
        case 4:
            print("Hasta pronto")
        case _:
            print("Opcion no encontrada")
