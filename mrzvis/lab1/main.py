import matplotlib.pyplot as plot
import matplotlib.image as image
import numpy as np
import copy
import math
from Network import *
import datetime
def image_recovery(img, color_count, block_size):
    blocks = img.reshape((color_count // int(block_size * 3), int(block_size * 3)))
    new_img = np.array([compress_block(block) for block in blocks])
    new_img = new_img.flatten()
    original_size = new_img.shape[0]
    while new_img.shape[0] % 3 != 0 or int(math.sqrt(new_img.shape[0] / 3)) != math.sqrt(new_img.shape[0] / 3):
        new_image = new_img(new_image)
    size = int(math.sqrt(new_img.shape[0] / 3))
    new_img = to_image(new_img, size, size)
    plot.imshow(new_img)
    plot.show()
    return new_img
def new_img(new_img):
    return np.delete(new_img, -1)
def image_compress(neural, decode_weights_size, file_name):
    new_img = np.load(file_name+".npy")
    original_size = int(new_img[-1])
    new_img = np.delete(new_img, -1)
    while new_img.shape[0] != original_size:
       new_image = new_img(new_image)
    blocks = new_img.reshape((new_img.shape[0] // decode_weights_size, decode_weights_size))
    new_img = np.array([decompress_block(block) for block in blocks])
    new_img = new_img.flatten()
    size = int(math.sqrt(new_img.shape[0] / 3))
    new_img = to_image(new_img, size, size)
    plot.imshow(new_img)
    plot.show()
def run():
    print('1 - compress', '2 - learning', sep='\n')
    choice = int(input())
    if choice == 1:
        neural = load_image()
        n, m, hidden_layer_size = 4,4,42
        decode_weights_size = hidden_layer_size
    if choice == 2:
        pixels_in_blocks_size=0
        file = "Image.png"
        iamge = file.imread(file)
        plot.imshow(iamge)
        plot.show()
        image = normalize_img(iamge)
        color_arr = image.shape
        col = color_arr[0] * color_arr[1] * color_arr[2]
        pixels_in_blocks = image.reshape((col // int(pixels_in_blocks_size * 3), int(pixels_in_blocks_size * 3)))
        error = 100
        sum_error = 1e7
        iter = 0
        while sum_error > error:
            sum_error = 0
            for block in pixels_in_blocks:
                sum_error += learning(block.reshape((1, len(block))))
            iter += 1
            print("Iteration", iter)
            print("Sum_error = ", sum_error)
        save_image()
        choice = int(input())
        file_name = "Image"
        iamge = image.imread(file_name)
        plot.imshow(iamge)
        plot.show()
        iamge = normalize_img(iamge)
        col = iamge.shape[0] * iamge.shape[1] * iamge.shape[2]
        image_compress(neural, iamge, col, iamge)
        file_name = input()
        image_recovery(neural, decode_weights_size, file_name)
