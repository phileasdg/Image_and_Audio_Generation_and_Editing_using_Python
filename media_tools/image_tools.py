import cv2
import matplotlib.pyplot as plt
from pathlib import Path
from . import data_tools

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


def array_1d_to_grayscale(array, add_empty_pixels=0, select=-1, wide=False):
    # normalize the array to be between 0 and 255
    array = normalise_array(array, uint8=True)
    array = data_tools.array_1d_to_2d(array, add_empty_pixels=add_empty_pixels, channels_per_pixel=1, select=select,
                                      wide=wide)
    return array.astype(int)


"""
convert a one-dimensional array to an RGB image array
"""


def array_1d_to_rgb(array, add_empty_pixels=0, select=-1, wide=False):
    # normalize the array to be between 0 and 255
    array = normalise_array(array, uint8=True)
    array = data_tools.array_1d_to_2d(array, add_empty_pixels=add_empty_pixels, channels_per_pixel=3, select=select,
                                      wide=wide)
    return array.astype(int)
