from media_tools import *
import numpy as np
import cv2
from random import randint, choice

sample_media = "C:/Users/pdazeley-gaist23/PycharmProjects/Image_and_Audio_Generation_and_Editing_using_Python/sample_media/"
img = image_tools.read_image(sample_media + "fire.jpg")

# image_tools.show_image(img, axis=True)

# copy the image
img_copy = img.copy()

n=360*5
#rotation = randint(0, 359)
rotation = choice([-1, 1, -5, 5])
#translate_x = randint(-img_copy.shape[0], img_copy.shape[0])
#translate_y = randint(-img_copy.shape[1], img_copy.shape[1])
translates = [-250, 250, -500, 500]
translate_x = choice(translates)
translate_y = choice(translates)
for i in range(n):
    # rotate the copy
    img_copy = image_tools.rotate_image(img_copy, rotation, False, border_type=cv2.BORDER_REPLICATE)
    # roll the color channels
    img_copy = data_tools.roll_array(img_copy, 1, 2)
    # translate the copy
    img_copy = data_tools.translate_2d_array(img_copy, translate_x, translate_y)
    # rescale the copy
    img_copy = data_tools.rescale_2d_array(img_copy, (2000, 2000))

    print("step", i, "of" ,n)

# show the copy
image_tools.show_image(img_copy, axis=True)

# replace values in array

