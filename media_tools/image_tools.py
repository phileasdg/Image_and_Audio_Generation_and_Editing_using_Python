import cv2
import matplotlib.pyplot as plt
from pathlib import Path
from . import data_tools
import numpy as np

"""
read an image as an array
"""


def read_image(path):
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


"""
display an array as an image
"""


def show_image(image, axis=False, title="", scale_ratio=2):
    plt.figure(figsize=[scale_ratio * x for x in plt.rcParams["figure.figsize"]])
    plt.title(title)
    plt.imshow(image, cmap="gray")
    if axis is not True:
        plt.axis('off')
    plt.show()


"""
save a numpy array as an image
"""


def save_image(image, path="saved_image.png"):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(path, image)
    file = Path(path)
    if file.is_file():
        print("Image saved at: " + path)


"""
convert an image array to an audio array by flattening the data
"""


def image_to_audio(image):
    # normalise image data to values between 0 and 1
    picture_norm = data_tools.normalise_array(image)
    # flatten the image data into a time series
    audio_data = data_tools.flatten_array(picture_norm)
    return audio_data


"""
convert a one-dimensional array to an grey-scale image array
"""


def array_1d_to_grayscale(array, add_empty_pixels=0, select=-1, wide=False, return_possible_shapes=False):
    # normalize the array to be between 0 and 255
    array = data_tools.normalise_array(array, uint8=True)
    array = data_tools.array_1d_to_2d(array, add_empty_pixels=add_empty_pixels, channels_per_pixel=1, select=select,
                                      wide=wide, return_possible_shapes=return_possible_shapes)
    return array.astype(int)


"""
convert a one-dimensional array to an RGB image array
"""


def array_1d_to_rgb(array, add_empty_pixels=0, select=-1, wide=False, return_possible_shapes=False):
    # normalize the array to be between 0 and 255
    array = data_tools.normalise_array(array, uint8=True)
    array = data_tools.array_1d_to_2d(array, add_empty_pixels=add_empty_pixels, channels_per_pixel=3, select=select,
                                      wide=wide, return_possible_shapes=return_possible_shapes)
    return array.astype(int)


"""
invert an image array
"""


def invert_image(image):
    return 255 - image


"""
rotate an image array around a point (default is the centre of the image)

# cv2 border types: # cv2.BORDER_CONSTANT, cv2.BORDER_REPLICATE, cv2.BORDER_REFLECT, cv2.BORDER_WRAP, 
cv2.BORDER_REFLECT_101, cv2.BORDER_DEFAULT 
"""


def rotate_image(image, angle, bound=True, point=None, border_type=cv2.BORDER_CONSTANT, border_value=(0, 0, 0)):
    if point is None:
        # make the point of rotation the center of the image
        point = tuple(np.array(image.shape[1::-1]) / 2)

    # get height and width of the image
    h, w = image.shape[:2]

    if bound:
        # get the rotation matrix
        matrix = cv2.getRotationMatrix2D(point, -angle, scale=1.0)
        # get the sine and cosine
        cos = np.abs(matrix[0, 0])
        sin = np.abs(matrix[0, 1])
        # compute the new bounding dimensions of the image
        nH = int((h * cos) + (w * sin))
        nW = int((h * sin) + (w * cos))
        # adjust the rotation matrix to take into account translation
        matrix[0, 2] += (nW / 2) - point[0]
        matrix[1, 2] += (nH / 2) - point[1]
        # perform the actual rotation and return the image
        return cv2.warpAffine(image, matrix, dsize=(nW, nH), borderMode=border_type, borderValue=border_value)
    else:
        # rotate the image
        return cv2.warpAffine(image, cv2.getRotationMatrix2D(point, -angle, 1.0), image.shape[1::-1],
                              borderMode=border_type, borderValue=border_value)
