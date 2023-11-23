import numeros

def preguntar():
    print("Bienvenido a Farmacia Chelito")
    while True:
        print("""
              [P] - Perfumeria
              [F] - Farmacia
              [C] - Cosmeticos
              """)
        try:
            mi_rubro = input("Opcion: ").upper()
            ["P","F","C"].index(mi_rubro)
        except ValueError:
            print("Esa no es una opcion valida.")
        else:
            break
    numeros.decorador(mi_rubro)


def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("¿Desea tomar turno? [S] [N]: ").upper()
            ["S","N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opcioen valida.")
        else:
            if otro_turno == "N":
                print("Gracias por su visita.")
                break

inicio()