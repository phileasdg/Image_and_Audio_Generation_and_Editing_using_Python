import numpy as np
from media_tools import *
import cv2

# create an array of zeros, and a smaller array of ones

zeros = np.zeros((100, 100))
ones = np.ones((50, 50))

# crete a blit function

def blit(src, dst, x, y, convert_src=None, convert_dst=None):
    # convert
    if convert_src is not None:
        src = cv2.cvtColor(src, convert_src)
    if convert_dst is not None:
        dst = cv2.cvtColor(dst, convert_dst)
    # blit
    # create a layer of zeros of the same shape as dst, and copy src into it
    layer = np.zeros(dst.shape, dtype=dst.dtype)
    # copy src into layer at 0, 0
    layer[0:src.shape[0], 0:src.shape[1]] = src
    # translate the layer to the correct position
    layer = data_tools.translate_2d_array(layer, x, y, border_type=cv2.BORDER_TRANSPARENT)
    # paste the layer into dst
    dst[0:layer.shape[0], 0:layer.shape[1]] = layer
    return dst

# blit the ones array into the zeros array
blitted = blit(ones, zeros, 0, 0)
image_tools.show_image(blitted, axis=True, title='blitted')

# blit the ones array into the zeros array, but offset by 10 pixels
blitted_2 = blit(ones, zeros, 25, 25)
image_tools.show_image(blitted, axis=True, title='blitted')

# as long as the arrays are the same shape, we can use the blit function
# let's try with an empty dst 200x200 colour image with alpha, and a 100x100 src image
dest = np.zeros((200, 200, 4), dtype=np.uint8)
colour_array = np.random.randint(0, 255, (100, 100, 4))
colour_array[:, :, 3] = 255
blitted_colour = blit(colour_array, dest, 50, 50)
image_tools.show_image(blitted_colour, axis=True, title='colour_array')

# blit 2 arrays to the same destination
dest_2 = np.zeros((200, 200, 4), dtype=np.uint8)
colour_array_2 = np.random.randint(0, 255, (100, 100, 4))
colour_array_2[:, :, 3] = 255
blitted_colour_2 = blit(colour_array_2, dest_2, 25, 25)
blitted_colour_2 = blit(colour_array_2, dest_2, 100, 100)
image_tools.show_image(blitted_colour_2, axis=True, title='colour_array_2')

