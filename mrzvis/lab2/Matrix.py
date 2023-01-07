class Matrix():
    
    def __init__(self,N,M):
         self.__N_size = N    # Number of rows in the matrix
         self.__M_size = M     # Number of cols in the matrix
         self.matrix = [[0] * M for _ in range(N)]


    def createMatrix (self, args : list):   # take list [] of matrix elements
        if(self.__N_size * self.__M_size == len(args)):
            for i in range(self.__N_size):
                for j in range(self.__M_size):
                    self.matrix[i][j]=args[j+self.__M_size*i]
        else:
            print("the number of list items does not match the size of the matrix")


    def printMatrix(self):
        for rows in self.matrix:
            print(*rows)
        print("")

    def __add__(self, other):
        result=Matrix(self.__N_size,self.__M_size)
        for i in range(self.__N_size):
            for j in range(self.__M_size):
                result.matrix[i][j]=self.matrix[i][j]+other.matrix[i][j]
        return result
    def __sub__(self, other):
        result = Matrix(self.__N_size, self.__M_size)
        for i in range(self.__N_size):
            result.matrix.append([])
            for j in range(self.__M_size):
                result.matrix[i].append(self.matrix[i][j] - other.matrix[i][j])
        return result



    def __str__(self):
        self.printMatrix()
        return ""

    def __mul__(self, other):
        if(type(other) is int):
            result = Matrix(self.__N_size, self.__M_size)
            for rows in range(self.__N_size):
                result.matrix.append([])
                for cols in range(self.__M_size):
                    result.matrix[rows].append(self.matrix[rows][cols]*other)
            return result
        else:
            result = Matrix(self.__N_size, other.__M_size)

            for i in range(self.__N_size):
                for j in range(other.__M_size):
                    for q in range(self.__M_size):
                        result.matrix[i][j] += self.matrix[i][q] * other.matrix[q][j]
            return result

    def matrix_transpose(self):
        result=Matrix(self.__M_size,self.__N_size)
        new_matrix_elements = [0] * (self.__N_size * self.__M_size)
        for i in range(self.__N_size):
            for j in range(self.__M_size):
                new_matrix_elements[(j * self.__N_size) + i] = self.matrix[i][j]
        result.createMatrix(new_matrix_elements)
        return result

    def zero(self):
        for row_index in range(self.__N_size):
            for col_index in range(self.__M_size):
                if row_index == col_index:
                    self.matrix[row_index][col_index] = 0
        return self.matrix

    def get_matrix_size_N(self):
        return self.__N_size

    def get_matrix_size_M(self):
        return self.__M_size
