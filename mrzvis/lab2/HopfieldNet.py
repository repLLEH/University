import functools
import math
from Matrix import Matrix
class HopfieldNetwork:
    def __init__(self):
        pass
    def writeInFile(self,file_name, matrix):
        with open(file_name, 'w') as file:
            for row_index in range(len(matrix)):
                for value_index in range(len(matrix[0])):
                    if value_index == len(matrix[0])-1:
                        file.write((str(matrix[row_index][value_index])+'\n'))
                    else:
                        file.write(str(matrix[row_index][value_index]) + ',')

    def readFromFile(self,file_name):
        images = []
        image = []
        with open(file_name, 'r') as file:
            for line in file:
                if line == '\n':
                    images.append(image)
                    image = []
                else:
                    for x in line.split(','):
                        if int(x) == 1:
                            image.append(1)
                        elif int(x) == 0:
                            image.append(-1)

            images.append(image)

        file.close()
        return images
    def getMatrix(self,file_name):
        matrix = []
        with open(file_name, 'r') as file:
            matrix = [[int(x) for x in line.split(',')] for line in file]
        file.close()
        return matrix
    def printModel(self,image):
        count_new_line = 0
        for row_index in range(len(image)):
            for value_index in range(len(image[row_index])):
                count_new_line += 1
                if count_new_line == 5:
                    if image[row_index][value_index] == 1:
                        print(1)
                    elif image[row_index][value_index] == -1:
                        print(0)
                    if image[row_index][value_index] == 0:
                        print(0)
                    count_new_line = 0
                else:
                    if image[row_index][value_index] == 1:
                        print(1, end='')
                    elif image[row_index][value_index] == -1:
                        print(0, end='')
                    if image[row_index][value_index] == 0:
                        print(0, end='')



    def getWeightFromModels(self,images):
        matrix_1 = Matrix(25,1)
        matrix_2 = Matrix(1,25)
        matrix_1.createMatrix(images[0])
        matrix_1.matrix_transpose()
        matrix_2.createMatrix(images[0])
        weight_m = matrix_1*matrix_2
        for model_index in range(1, len(images)):
            matrix_3=Matrix(25,1)
            matrix_4=Matrix(1,25)
            matrix_3.createMatrix(images[model_index])
            matrix_3.matrix_transpose()
            matrix_4.createMatrix(images[model_index])
            final_matrix=weight_m+(matrix_3*matrix_4)
            weight_m = final_matrix
        weight_matrix = weight_m.zero()
        return weight_matrix

    def func_activ(self,matrix : Matrix):
        n=matrix.get_matrix_size_N()
        m=matrix.get_matrix_size_M()
        n_matrix = Matrix(n, m)
        value_vector=[]
        matrix_vector=[]
        for i in range(n):
            for j in range(m):
                matrix_vector.append(matrix.matrix[i][j])

        for i in range(n*m):
            value_vector.append(round(math.tanh(matrix_vector[i])))
        n_matrix.createMatrix(value_vector)

        return n_matrix

    def run(self,X, weight_matrix):
        x_matrix=Matrix(1,25)
        x_matrix.createMatrix(X[0])
        prev = x_matrix.matrix_transpose()
        matrix_vector = []
        for i in range(len(weight_matrix)):
            for j in range(len(weight_matrix[i])):
                matrix_vector.append(weight_matrix[i][j])
        weight_m = Matrix(25,25)
        weight_m.createMatrix(matrix_vector)
        relax = False
        i = 0
        while relax is not True:
            if i >= 1000:
                print('\n error')
                break
            mult=weight_m*prev
            current = self.func_activ(mult)
            print(current.matrix)

            self.printModel(prev.matrix_transpose().matrix)
            print('\n')
            if functools.reduce(lambda x, y: x and y, map(lambda a, b: a == b, prev.matrix, current.matrix), True):
                print('\n recognized')
                self.printModel(current.matrix_transpose().matrix)
                relax = True
            prev = current
            i += 1
