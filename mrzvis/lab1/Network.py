import matplotlib.pyplot as plot
import matplotlib.image as image
import numpy as np
import copy
import math
n = 256
m = 256
alpha = 0.001
hidden_layer_size = 512
weight_matrix = np.random.randn(n * m * 3, hidden_layer_size)
recover_weights_matrix = weight_matrix.T
def learning( input, weight_matrix,recover_weights_matrix):
    hidden_output = input @ weight_matrix
    output = hidden_output @ recover_weights_matrix
    delta = output - input
    # alpha = 1 / (hidden_output @ hidden_output.T)
    recover_weights_matrix -= alpha * (hidden_output.T @ delta)
    # alpha = 1 / (input @ input.T)
    weight_matrix -= alpha * (input.T @ (delta @ recover_weights_matrix.T))
    weights_normalize()
    error = np.sum(np.square(delta))
    return error
def normalize_img(pixels):
    pixels = copy.deepcopy(pixels)
    for row in range(len(pixels)):
        for column in range(len(pixels[row])):
            for color in range(len(pixels[row][column])):
                pixels[row][column][color] = pixels[row][column][color] * 2 - 1
    return pixels
def save_image():
    np.save(r"weight_matrix.npy", weight_matrix)
    np.save(r"recover_weights_matrix.npy", recover_weights_matrix)
    with open(r"data.txt", "w") as file:
        file.write(str(n) + " " + str(m) + " " + str(hidden_layer_size))
def load_weights():
    weight_matrix = np.load(r"weight_matrix.npy")
    recover_weights_matrix = np.load(r"recover_weights_matrix.npy")
    return weight_matrix, recover_weights_matrix
def denormalize_img(pixels):
    pixels = copy.deepcopy(pixels)
    for row in range(len(pixels)):
        for column in range(len(pixels[row])):
            for color in range(len(pixels[row][column])):
                pixels[row][column][color] = (pixels[row][column][color] + 1) / 2
                if pixels[row][column][color] > 1:
                    pixels[row][column][color] = 1
                elif pixels[row][column][color] < 0:
                    pixels[row][column][color] = 0
    return pixels
def to_image(colors, n, m):
    return denormalize_img(np.array(colors).reshape((n, m, 3)))
def load_image():
    weight_matrix, recover_weights_matrix = load_weights()
    with open(r"data.txt", "r") as file:
        data = file.read().split()
        n = int(data[0])
        m = int(data[1])
        hidden_layer_size = int(data[2])
def weights_normalize():
    weights_transpose = weight_matrix.T
    decode_weights_transpose = recover_weights_matrix.T
    for col in range(len(weight_matrix[0])):
        module = np.linalg.norm(weights_transpose[col], ord=2)
        for row in range(len(weight_matrix)):
            weight_matrix[row][col] /= module
    for row in range(len(recover_weights_matrix)):
        module = np.linalg.norm(decode_weights_transpose[row], ord=2)
        for col in range(len(recover_weights_matrix[0])):
            recover_weights_matrix[row][col] /= module
def compress_block(block):
    return block
def decompress_block(block):
    return block