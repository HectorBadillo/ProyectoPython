class CD:

    def __init__(self, autor, titulo, canciones) -> None:
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self) -> str:       #Como se comporta al imprimir
        return f"Album: {self.titulo} de {self.autor}"
    
    def __len__(self):
        return self.canciones
    
    def __del__(self):
        print("Se ha eliminado el cd")


mi_cd = CD('Pink Floyd', 'The Wall', 24)

print(mi_cd)
print(len(mi_cd))

del mi_cd
 