

class Matriz:
    def __init__(self,matriz:list)->None:
        self._matriz = matriz

    @property           #getter
    def matriz(self):
        return self._matriz
    
    @matriz.setter      #setter
    def matriz(self,matriz:list):
        self._matriz=matriz
    
    def imprimir(self):
        print(self._matriz)



class Admin:
    def __init__(self,lista_matriz:list) -> None:
        self.lista_matriz = lista_matriz



class Operacion:
    def __init__(self, matrizA:list, matrizB:list) -> None:
        self.matrizA = matrizA
        self.matrizB = matrizB

    def suma_matriz(self):
        if (len(self.matrizA) != len(self.matrizB)) or (len(self.matrizA[0]) != len(self.matrizB[0])):
            return "Sus dimensiones no son compatibles"
        
        resultado = []
        for i in range(len(self.matrizA)):
            fila_resultado = []
            for j in range(len(self.matrizA[0])):
                suma = self.matrizA[i][j] + self.matrizB[i][j]
                fila_resultado.append(suma)
            resultado.append(fila_resultado)
        return resultado
    
    def producto_matriz(self):
        if (len(self.matrizA[0]) != len(self.matrizB)):
            return "Las dimensiones no son compatibles"
        
        resultado = []
        for i in range(len(self.matrizB)):
            fila_resultado = []
            for j in range(len(self.matrizB)):
                producto=0
                for k in range(len(self.matrizB)):
                    producto += (self.matrizA[i][k]) * (self.matrizB[k][j])
                fila_resultado.append(producto)
            resultado.append(fila_resultado)
        return resultado

    

matriz_a = [
    [1,2],
    [3,4]
]

matriz_b= [
    [5,6],
    [7,8]
]

print(Operacion(matriz_a,matriz_b).producto_matriz())
