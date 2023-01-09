import matplotlib.pyplot as plot
import matplotlib.image as image
import numpy as np
import copy
import math
from Network import *
import datetime
def print_function(new_image):
    return np.delete(new_image, -1)
def image_recovery(img, color_count, block_size):
    pixels_in_blocks = img.reshape((color_count // int(block_size * 3), int(block_size * 3)))
    new_compress_blocks=[]
    for pixels_in_block in pixels_in_blocks:
        new_compress_blocks.append(compress_block(pixels_in_block))
    new_image = np.array(new_compress_blocks)
    new_image = new_image.flatten()
    while new_image.shape[0] % 3 != 0 or int(math.sqrt(new_image.shape[0] / 3)) != math.sqrt(new_image.shape[0] / 3):
        new_image = new_image(new_image)
    size = int(math.sqrt(new_image.shape[0] / 3))
    new_image = denormalize_img(np.array(new_image).reshape((size, size, 3)))
    show_result(new_image)
    return new_image
def show_result(new_image):
    plot.imshow(new_image)
    plot.show()
def first_choice():
    load_image()
    n, m, neyron_layer_size = 4, 4, 42
    recovered_weights = neyron_layer_size
    return n, m, neyron_layer_size,recovered_weights
def second_choice(recovered_weights):
    error = 100
    sum_error = 1e7
    pixels_in_blocks_size = 0
    iter = 0
    file = "Image.png"
    iamge = file.imread(file)
    show_result(iamge)
    image = normalize_img(iamge)
    color_arr = image.shape
    j = color_arr[0] * color_arr[1] * color_arr[2]
    pixels_in_blocks = iamge.reshape((j // pixels_in_blocks_size * 3, pixels_in_blocks_size * 3))
    while sum_error > error:
        sum_error = 0
        for pixels_in_block in pixels_in_blocks:
            sum_error += learning(pixels_in_block.reshape((1, len(pixels_in_block))))
        iter += 1
        print("Iteration", iter)
        print("Sum_error = ", sum_error)
    save_image()
    title = "Image"
    iamge = image.imread(title)
    plot.imshow(iamge)
    plot.show()
    iamge = normalize_img(iamge)
    j = color_mult
    image_compress(iamge, j, iamge)
    title = input()
    image_recovery(recovered_weights, title)
def color_mult(iamge):
    return iamge.shape[0] * iamge.shape[1] * iamge.shape[2]
def run():
    recovered_weights=0
    print('1 - compress', '2 - learning', sep='\n')
    choice = int(input())
    if choice == 1:
        n, m, neyron_layer_size,recovered_weights = first_choice()
    if choice == 2:
        second_choice(recovered_weights)
def image_compress(recovered_weights, title):
    new_image = np.load(title+".npy")
    standard_height_width = new_image[-1]
    new_image = np.delete(new_image, -1)
    while new_image.shape[0] != standard_height_width:
       new_image = print_function(new_image)
    pixels_in_blocks = new_image.reshape((new_image.shape[0] // recovered_weights, recovered_weights))
    new_decompress_blocks = []
    for pixels_in_block in pixels_in_blocks:
        new_decompress_blocks.append(decompress_block(pixels_in_block))
    new_image = np.array(new_decompress_blocks)
    new_image = new_image.flatten()
    height_width = int(math.sqrt(new_image.shape[0] / 3))
    new_image = denormalize_img(np.array(new_image).reshape((height_width, height_width, 3)))
    show_result(new_image)
run()
