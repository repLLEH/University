import random
from math import sqrt


# function to calculate the MULTIPLICATION OF MATRIXES
def matrix_multiplication(matrix_1, matrix_2):
    # check for consistence of the matrixes
    if len(matrix_1[0]) == len(matrix_2):
        # fill result matrix with 0's
        matrix_result = []
        for index1 in range(len(matrix_1)):
            row = []
            for index2 in range(len(matrix_2[0])):
                row.append(0)
            matrix_result.append(row)


        # calculate the values of the RESULT MATRIX
        for row in range(len(matrix_1)):
            for index1 in range(len(matrix_1[0])):
                for index2 in range(len(matrix_2[0])):
                    matrix_result[row][index2] += (matrix_1[row][index1] * matrix_2[index1][index2])

        return matrix_result
    else:
        print('Matrices cannot be multiplied')


# function to create a TRANSPOSED MATRIX
def matrix_transposition(matrix):
    result_matrix = []
    # go through rows
    for i in range(len(matrix[0])):
        col = []
        # go through columns
        for j in range(len(matrix)):
            col.append(matrix[j][i])
        result_matrix.append(col)
    return result_matrix


# multiplication of number on matrix
def number_matrix_multiplication(number, matrix):
    result_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append((number * matrix[i][j]))
        result_matrix.append(row)
    return result_matrix

# function for MATRIX DIFFERENCE
def matrix_difference(matrix1, matrix2):
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        result_matrix = []
        for row_id in range(len(matrix1)):
            row = []
            for col_id in range(len(matrix1[0])):
                row.append((matrix1[row_id][col_id] - matrix2[row_id][col_id]))
            result_matrix.append(row)
        return result_matrix
    else:
        print("Error!")


# function for MUTRIX SUMMARY
def matrix_sum(matrix1, matrix2):
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        result_matrix = generate_matrix(len(matrix1), len(matrix1[0]))
        for row_index in range(len(matrix1)):
            for col_index in range(len(matrix1[0])):
                result_matrix[row_index][col_index] = matrix1[row_index][col_index]+matrix2[row_index][col_index]
        return result_matrix
    else:
        print('Matrices cannot be summarized')



# create a VECTOR from MATRIX
def from_matrix_to_vector(matrix):
    # create to vectors to make a vector inside of
    # another one -> [ [] ]
    # to proceed work with it like a 1xN sized matrix
    result_vector = []
    vector = []
    for row in matrix:
        for pixel in row:
            for rgb_value in pixel:
                vector.append(rgb_value)
    result_vector.append(vector)
    return result_vector


# generate weight matrix
def generate_matrix(n, p):
    w_matrix = []
    for i in range(n):
        w_matrix_row = []
        for j in range(p):
            # w_matrix_row.append(float('{:.2f}'.format(random.uniform(-1,1))))
            w_matrix_row.append(random.uniform(-1,1))
        w_matrix.append(w_matrix_row)
    return w_matrix

# normilize matrices
def normalize_w_matrices(w_matrix):
    new_matrix = [[0 for i in range(len(w_matrix[0]))] for j in range(len(w_matrix))]
    for row in range(len(w_matrix)):
        for col in range(len(w_matrix[0])):
            new_matrix[row][col] = (w_matrix[row][col]/abs_col(w_matrix, col))
    return new_matrix

# |W(j)|
def abs_col(w_matrix, col_index):
    abs = 0
    for row_id in range(len(w_matrix)):
        abs += w_matrix[row_id][col_index] * w_matrix[row_id][col_index]
    abs = sqrt(abs)
    return abs

# calculate the ADAPTIVE STEP = a
def adaptive_step(y_i):
    arg = matrix_multiplication(y_i,matrix_transposition(y_i))
    return (1/arg[0][0])


# the training of neurons on the first layer
# W(t+1) = W(t) - a * [X(i)]T * dX(i) * [W`(t)]T
def first_layer_neurons_training(adaptive_step, xi, dx_i, w, w_):
    first_arg = number_matrix_multiplication(adaptive_step, matrix_transposition(xi))
    second_arg = matrix_multiplication(first_arg,dx_i)
    third_arg = matrix_multiplication(second_arg, matrix_transposition(w_))
    return matrix_difference(w, third_arg)


# the training of neurons on the second layer
# W`(t+1) = W`(t) - a` * [Y(i)]T * dX(i)
def second_layer_neurons_training(adaptive_step, w, y_i, dx_i):
    return matrix_difference(w, matrix_multiplication(number_matrix_multiplication(adaptive_step, matrix_transposition(y_i)), dx_i))



# calculate total RMSE (root mean square error) = E(q)
def total_rmse(d_x_vector):
    rmse = 0
    for i in d_x_vector[0]:
        # take dx_vector[0][i] because the vector is actually
        # a one row matrix
        rmse  += (i**2)
    return rmse
