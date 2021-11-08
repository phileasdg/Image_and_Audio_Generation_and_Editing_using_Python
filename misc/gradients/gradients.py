import collections

import numpy as np
from media_tools import *
import cv2

# generate a 2d rgb gradient from a given color to another
def rgb_gradient(dim, color1, color2, vertical=True):
    # generate a 2d array of the given dimensions
    arr = np.zeros((*dim, 3), np.uint8)
    # fill the red, green, and blue channels with gradient values from color1 to color2
    for i in range(3):
        arr[:, :, i] = grey_gradient(dim[0], color1[i], color2[i], vertical=vertical)
    # return the array
    return arr

# generate a 2d greyscale gradient from a given shade to another
def grey_gradient(dim, shade1, shade2, vertical=True):
    # generate a 2d array of the given dimensions
    arr = np.zeros(dim, np.uint8)
    if vertical is False:
        arr = arr.T
    # fill the array with gradient values from shade1 to shade2
    arr[:] = np.linspace(shade1, shade2, arr.size).reshape(arr.shape)
    # return the array
    return arr

# generate a 2d greyscale or rgb gradient at an angle
def gradient_at_angle(dim, value1, value2, angle=0, vertical=True):
    # generate a container array which will contain the full gradient after rotation
    container_shape = data_tools.rotate_2d_array_around_point(np.zeros(dim), angle, bound=True).shape[:2]
    gradient = np.zeros(container_shape)
    # if the gradient is greyscale, fill the container with a greyscale gradient
    if len(value1) == 1:
        gradient = grey_gradient(container_shape, value1, value2, vertical=vertical)
    # if the gradient is rgb, fill the container with an rgb gradient
    elif len(value1) == 3:
        gradient = rgb_gradient(container_shape, value1, value2, vertical=vertical)
    # rotate the gradient by the given angle
    gradient = data_tools.rotate_2d_array_around_point(gradient, angle, bound=True)
    # crop the gradient to the gradient area
    # calculate the crop area based on the angle
    # the top left corner of the crop area is the center of the hipotenuse of the triangle (top left corner of the gradient, first gradient row, and first gradient column)
    # get the index of the first gradient row and column
    row_index = int(gradient.shape[0] / 2)
    col_index = int(gradient.shape[1] / 2)
    # get the length of the hipotenuse of the triangle
    hipotenuse_length = np.sqrt(gradient.shape[0] ** 2 + gradient.shape[1] ** 2)
    # get the coordinate of the middle of the hipotenuse
    hipotenuse_middle = (int(hipotenuse_length / 2), int(hipotenuse_length / 2))
    #crop the gradient to the top left corner of the crop area
    gradient = gradient[hipotenuse_middle[0]:, hipotenuse_middle[1]:]
    # return the gradient
    return gradient

    # crop_top_left = (int(np.cos(angle) * dim[0] / 2), int(np.sin(angle) * dim[1] / 2))
    # the bottom right corner of the crop area is the center of the hipotenuse of the triangle (bottom right corner of the gradient, last gradient row, and last gradient column)
    # crop_bottom_right = (int(np.cos(angle) * dim[0] / 2 + dim[0]), int(np.sin(angle) * dim[1] / 2 + dim[1]))
    # crop the gradient to the crop area
    # gradient = gradient[crop_top_left[1]:crop_bottom_right[1], crop_top_left[0]:crop_bottom_right[0]]
    # gradient = gradient[50:-50,50:-50]
    # return the rotated gradient
    # return gradient


# try it
if __name__ == '__main__':
    # generate a gradient
    gradient = rgb_gradient((100,100), (255, 0, 0), (0, 255, 0), vertical=False)
    # image_tools.show_image(gradient, axis=True, title='gradient')

    # generate a gradient
    gradient = grey_gradient((100,100), 0, 255, vertical=False)
    # image_tools.show_image(gradient, axis=True, title='gradient')

    # generate a gradient
    gradient = gradient_at_angle((100, 100), (255, 0, 0), (0, 255, 0), angle=20, vertical=False)
    image_tools.show_image(gradient, axis=True, title='gradient')
