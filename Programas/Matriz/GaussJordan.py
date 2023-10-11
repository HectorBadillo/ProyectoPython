
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
    
    @columns.setter
    def columns(self,values_setter:int):
        self._columns_len = values_setter
    
    @property
    def rows(self):
        return self._rows_len
    
    @rows.setter
    def rows(self,values_setter:int):
        self._rows_len = values_setter


    def imprimir(self):
        print("\n")
        bandera = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if bandera == self.columns:
                    print("\n")
                    bandera = 0
                print(f"{self.values[i][j]} \t",end=' ')
                bandera += 1
        print("\n")



class Sistema_Ecuaciones:
    def __init__(self, matrix_A:Matrix, vector:list) -> None:
        self.matrix = matrix_A
        self.vector = vector

        self.matrix_aux = matrix_A
        for i in range(self.matrix.columns):
            self.matrix_aux.values[i].append(vector[i])
        self.matrix_aux.columns = (self.matrix.columns) + 1

    def gaus_jordan(self):
        if (self.matrix_aux.columns != (self.matrix_aux.rows)+1) or (self.matrix_aux.rows != len(self.vector)):
             print("Las dimensiones no son compatibles")
             return 0
        for i in range(self.matrix_aux.rows):
            if self.matrix_aux.values[i][i] == 0:
                print("La matriz no es invertible")
                return 0
                      
        
        for i in range(self.matrix_aux.rows):
             # Hacemos que el pivote sea igual a 1
            pivot = self.matrix_aux.values[i][i]
            for j in range(self.matrix_aux.columns):
                self.matrix_aux.values[i][j] /= pivot
            # Eliminación gaussiana para hacer ceros en las otras filas
            for k in range(self.matrix_aux.rows):
                if k != i:
                    factor = self.matrix_aux.values[k][i]
                    for j in range(self.matrix_aux.columns):
                        self.matrix_aux.values[k][j] -= factor * self.matrix_aux.values[i][j]

        self.matrix_aux.imprimir()
        return self.matrix_aux


matrix_A = [
    [2,-3,2],
    [1,1,-4],
    [5,-8,7]
]

vector = [1,8,1]

matriz_obtA = Matrix(matrix_A)

Resultado =(Sistema_Ecuaciones(matriz_obtA,vector).gaus_jordan())
Resultado.imprimir