import matplotlib.pyplot as plot
import matplotlib.image as image
import numpy as np
import copy
import math
def learning(first_layer_values, w_matrix,recover_weights_matrix):
    img_out = first_layer_values @ w_matrix
    last_layer_values = img_out @ recover_weights_matrix
    d = last_layer_values - first_layer_values
    recover_weights_matrix -= a * (img_out.T @ d)
    w_matrix -= a * (first_layer_values.T @ (d @ recover_weights_matrix.T))
    w_matrix_standart()
    e = np.sum(d*1/2)
    return e
def deep_copy(pix):
    return copy.deepcopy(pix)
def normalize_img(pix):
    pix=deep_copy(pix)
    for i in range(len(pix)):
        for j in range(len(pix[i])):
            for color in range(len(pix[i][j])):
                pix[i][j][color] = pix[i][j][color] * 2 - 1
    return pix
def save_image():
    np.save(r"w_matrix.npy", w_matrix)
    save_recovered_weights()
    with open(r"info.txt", "w") as file:
        file.write(str(n))
        file.write(str(m))
        file.write(str(neyron_layer_size))

def save_recovered_weights():
    np.save(r"recover_weights_matrix.npy", recover_weights_matrix)

def pix_compare_with_1(pix):
    if pix > 1:
        pix=1
    return pix
def pix_compare_with_0(pix):
    if pix < 0:
        pix=0
    return pix
def denormalize_img(pix):
    pix = deep_copy(pix)
    for i in range(len(pix)):
        for j in range(len(pix[i])):
            for o in range(len(pix[j][o])):
                pix[i][j][o] = (pix[i][j][o] + 1) / 2
                pix_compare_with_1(pix[i][j][o])
                pix_compare_with_0(pix[i][j][o])
    return pix
def load_image():
    w_matrix = np.load(r"w_matrix.npy")
    recover_weights_matrix = np.load(r"recover_weights_matrix.npy")
    with open(r"info.txt", "r") as info:
        info = info.read()
        info.split()

def w_matrix_standart():
    weights_transpose = w_matrix.T
    transpose_weight_matrix = recover_weights_matrix.T
    for j in range(len(w_matrix[0])):
        mode = np.linalg.norm(weights_transpose[j], ord=2)
        for i in range(len(w_matrix)):
            w_matrix[i][j] /= mode
    for i in range(len(recover_weights_matrix)):
        mode = np.linalg.norm(transpose_weight_matrix[i], ord=2)
        for j in range(len(recover_weights_matrix[0])):
            recover_weights_matrix[i][j] /= mode
def compress_block(block):
    return block
def decompress_block(block):
    return block

n = 256
m = 256
a = 0.001
neyron_layer_size = 512
w_matrix = np.random.randn(n * m * 3, neyron_layer_size)
recover_weights_matrix = w_matrix.T