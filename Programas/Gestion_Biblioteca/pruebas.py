


class Libro:
    def __init__(self, titulo: str, autor: str, status: bool) -> None:
        self._titulo = titulo
        self._autor = autor
        self._status = status

    def mostrar_libro(self):
        print(f'Título: {self.titulo}, Autor: {self.autor}, Status: {"Disponible" if self.status else "Prestado"}')


    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self, nuevo_titulo:str):
        self._titulo = nuevo_titulo


    @property
    def autor(self):
        return self._autor
    @autor.setter
    def autor(self, nuevo_autor:str):
        self._autor = nuevo_autor

 
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, nuevo_status:bool):
        self._status = nuevo_status



class CatalogoLibros:
    def __init__(self) -> None:
        self.libros = []


    def agregar_libro(self, titulo: str, autor: str, status: bool):
        nuevo_libro = Libro(titulo, autor, status)
        self.libros.append(nuevo_libro)


    def editar_status(self, titulo: str, nuevo_status: bool):
        for libro in self.libros:
            if libro.titulo == titulo:
                libro.status = nuevo_status
                return True  # Indica que se realizó la edición con éxito
        return False  # Indica que el libro no se encontró
    

    def eliminar_libro(self, titulo:str):
        for libro in self.libros:
            if libro.titulo == titulo:
                self.libros.remove(libro)


    def mostrar_catalogo(self):
        for libro in self.libros:
            print(f'Título: {libro.titulo}, Autor: {libro.autor}, Status: {"Disponible" if libro.status else "Prestado"}')



class UsuarioCliente:
    def __init__(self, nombre:str, usuario:str , password:str, telefono:int) -> None:
        self._nombre = nombre
        self._usuario = usuario
        self._password = password
        self._telefono = telefono
    

    def buscar_libro(self, catalogo:CatalogoLibros, titulo:str):
        for libro in catalogo.libros:  
            if libro.titulo == titulo:
                print(libro.mostrar_libro())
                return True
        print("Libro no encontrado.")
        return False
    
    def prestamo_libro(self, catalogo:CatalogoLibros, titulo:str):
        if catalogo.editar_status(titulo,False):
            print("Libro prestado")
                


    def devolver_libro(self, catalogo:CatalogoLibros, titulo:str):
        if self.buscar_libro(catalogo,titulo):
            if catalogo.editar_status(titulo,True):
                print("Libro devuelto")


    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre


    @property
    def usuario(self):
        return self._usuario
    @usuario.setter
    def usuario(self, nuevo_usuario):
        self._usuario = nuevo_usuario


    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, nueva_password):
        self._password = nueva_password


    @property
    def telefono(self):
        return self._telefono
    @telefono.setter
    def telefono(self, nuevo_telefono):
        self._telefono = nuevo_telefono

# Crear una instancia del catálogo de libros
catalogo = CatalogoLibros()

# Agregar libros al catálogo
catalogo.agregar_libro("Libro 1", "Autor 1", True)
catalogo.agregar_libro("Libro 2", "Autor 2", False)
catalogo.agregar_libro("Libro 3", "Autor 3", True)

# Mostrar el catálogo
print("\nCatálogo de libros:")
catalogo.mostrar_catalogo()

# Editar el estado de un libro
print("\nEditar status")
titulo_a_editar = "Libro 2"
nuevo_status = True
if catalogo.editar_status(titulo_a_editar, nuevo_status):
    print(f'Status de "{titulo_a_editar}" actualizado a Disponible.')
else:
    print(f'El libro "{titulo_a_editar}" no se encontró en el catálogo.')

# Mostrar el catálogo actualizado
print("\nCatálogo de libros actualizado:")
catalogo.mostrar_catalogo()

print("\nCatálogo de libros actualizado:")
catalogo.eliminar_libro("Libro 1")
catalogo.mostrar_catalogo()

print("\nBusqueda de libro")
usuario = UsuarioCliente("Nombre del Usuario", "usuario123", "contraseña", 123456789)
titulo_buscado = "Libro 2"
libro_encontrado = usuario.buscar_libro(catalogo,titulo_buscado)

print("\nPrestamo")
usuario.prestamo_libro(catalogo,titulo_buscado)

print("\nDevolucion")
usuario.devolver_libro(catalogo,titulo_buscado)
usuario.buscar_libro(catalogo,titulo_buscado)