import functools
from matrix_operations import *
import math

def writeInFile(file_name, matrix):
    with open(file_name, 'w') as file:
        for row_index in range(len(matrix)):
            for value_index in range(len(matrix[0])):
                if value_index == len(matrix[0])-1:
                    file.write((str(matrix[row_index][value_index])+'\n'))
                else:
                    file.write(str(matrix[row_index][value_index]) + ',')

def readFromFile(file_name):
    models = []
    model = []
    with open(file_name, 'r') as file:
        for line in file:
            if line == '\n':
                models.append(model)
                model = []
            else:
                for x in line.split(','):
                    if int(x) == 1:
                        model.append(1)
                    elif int(x) == 0:
                        model.append(-1)

        models.append(model)

    file.close()
    return models
def getMatrix(file_name):
    matrix = []
    with open(file_name, 'r') as file:
        matrix = [[int(x) for x in line.split(',')] for line in file]
    file.close()

    return matrix
def printModel(model):
    count_new_line = 0
    for value_index in range(len(model[0])):
        count_new_line += 1
        if count_new_line == 4:
            if model[0][value_index] == 1:
                print(1)
            elif model[0][value_index] == -1:
                print(0)
            count_new_line = 0

        else:
            if model[0][value_index] == 1:
                print(1, end='')
            elif model[0][value_index] == -1:
                print(0, end='')

def vectorToMatrix(vector):
    new_vector = []
    new_vector.append(vector)
    return new_vector

def getWeightFromModels(models):
    weight_matrix = matrix_multiplication(matrix_transposition(vectorToMatrix(models[0])), vectorToMatrix(models[0]))
    # for j in weight_matrix:
    #     print(j)
    for model_index in range(1, len(models)):
        matrix = matrix_sum(weight_matrix, matrix_multiplication(matrix_transposition(vectorToMatrix(models[model_index])),vectorToMatrix(models[model_index])))
        weight_matrix = matrix
        # for i in weight_matrix:
        #     print(i)
        # print('---------------------------')
    weight_matrix = zero(weight_matrix)
    return weight_matrix

def vector_to_matrix(vector):
    matrix = []
    for index in range(len(vector)):
        row_in_matrix = []
        row_in_matrix.append(vector[index])
        matrix.append(row_in_matrix)
    return matrix

def zero(matrix):
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[0])):
            if row_index == col_index:
                matrix[row_index][col_index] = 0
    return matrix

def activation_function(matrix):
    new_matrix = generate_matrix(len(matrix), len(matrix[0]))
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[0])):
            new_matrix[row_index][col_index] = round(math.tanh(matrix[row_index][col_index]))
    return new_matrix


def run(X, weight_matrix):
    previous_state = matrix_transposition(X)
    relax = False
    iteration = 0

    while relax is not True:
        if iteration >= 1000:
            print('error')
            break

        current_state = activation_function(matrix_multiplication(weight_matrix, previous_state))


        printModel(matrix_transposition(previous_state))
        print()
        if functools.reduce(lambda x, y: x and y, map(lambda a, b: a == b, previous_state, current_state), True):

            print('recognized')
            relax = True



        previous_state = current_state
        iteration += 1
