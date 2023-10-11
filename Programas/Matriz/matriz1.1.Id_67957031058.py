

class Matrix:
    def __init__(self,matrix:list)->None:
        self._values = matrix
        self._columns_len = len(matrix[0])
        self._rows_len = len(matrix)

    @property           #getter
    def values(self):
        return self._values
    
    @values.setter      #setter
    def values(self,matrix:list):
        self._values=matrix

    @property
    def columns(self):
        return self._columns_len
    
    @property
    def rows(self):
        return self._rows_len

    def imprimir(self):
        print(self._values)



class Admin:
    def __init__(self,dict_matrix:dict) -> None:
        self._dict_matrix = dict_matrix
    
    @property
    def dict_matrix(self):
        return self._dict_matrix
    
    def operacion_elemental(self, opcion:str, name_matrix_A:str, name_matrix_B:str):
        if opcion == "suma":
            operacion_obj = Operacion(self.dict_matrix[name_matrix_A],self.dict_matrix[name_matrix_B])



class Operacion:
    def __init__(self, matrix_A:Matrix, matrix_B:Matrix ) -> None:
        self.matrix_A = matrix_A
        self.matrix_B = matrix_B

    def suma_matrix(self):
        #Suma de matrices
        if (self.matrix_A.columns) != (self.matrix_B.columns) or (self.matrix_A.rows) != (self.matrix_B.rows):
            return "Sus dimensiones no son compatibles"
        
        resultado = []
        for i in range(self.matrix_A.columns):
            fila_resultado = []
            for j in range(self.matrix_A.columns):
                suma = self.matrix_A.values[i][j] + self.matrix_B.values[i][j]
                fila_resultado.append(suma)
            resultado.append(fila_resultado)
        return resultado
    
    def producto_matrix(self):
        #Producto de matrices
        if (self.matrix_A.columns != self.matrix_B.rows):
            return "Las dimensiones no son compatibles"
        
        resultado = []
        for i in range(self.matrix_A.columns):
            fila_resultado = []
            for j in range(self.matrix_A.columns):
                producto=0
                for k in range(self.matrix_A.columns):
                    producto += (self.matrix_A.values[i][k]) * (self.matrix_B.values[k][j])
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

matriz_a_obj = Matrix(matriz_a)
matriz_b_obj = Matrix(matriz_b)

matriz_a_obj.imprimir()
matriz_b_obj.imprimir()
print('\n')

print(Operacion(matriz_a_obj,matriz_b_obj).producto_matrix())
print(Operacion(matriz_a_obj,matriz_b_obj).suma_matrix())
