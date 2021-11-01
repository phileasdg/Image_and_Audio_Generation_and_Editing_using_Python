import numpy as np
import pandas as pd

"""
map values in a range to proportional values in another range
"""


def map_data_to_range(array, min_val, max_val):
    data_min = np.min(array)
    data_max = np.max(array)

    array = array.astype('float64')
    array = min_val + (((array - data_min) / (data_max - data_min)) * (max_val - min_val))
    return array


"""
normalise values in an array to values between 0 and 1, or to values between 0 and 255
"""


def normalise_array(array, uint8=False):
    array = map_data_to_range(array, 0, 1)
    if uint8 is True:
        array = (250 * array).astype(int)
    return array


"""
clip (limit) array values to values in a range
"""


def clip_array(array, val_min=None, val_max=None):
    if val_min is None:
        val_min = np.min(array)
    if val_max is None:
        val_max = np.max(array)
    array = np.clip(array, val_min, val_max)
    return array


"""
convert a 2d array to 1d array by flattening it
"""


def flatten_array(array):
    array = array.flatten()
    print(array)
    return array


"""
reshape an array into a 2d array with n columns
"""


def reshape_array_2d(array, ncol):
    array = np.reshape(array, (-1, ncol))
    return array


"""
get factor list of a number
"""


def get_factor_pairs(value):
    factors = []
    for i in range(1, int(value ** 0.5) + 1):
        if value % i == 0:
            factors.append((i, value / i))
    return factors


"""
invert an array
"""


def invert_array(array):
    array = 1 - array
    return array


"""
split a 1d array into a 2d array (good for converting things to image) split data array along rows into an array of n smaller arrays
"""


def array_1d_to_2d(array, add_empty_pixels=0, channels_per_pixel=3, select=-1, wide=True):
    # normalize the array to be between 0 and 255
    array = normalise_array(array, uint8=True)

    # add observations so as  to enable perfect division of array into pixel cells
    add_observations = len(array) % channels_per_pixel
    array = np.concatenate((array, np.zeros(add_observations)))

    # add add_empty_pixels number of empty pixel arrays to the array
    array = np.concatenate((array, np.tile(np.zeros(channels_per_pixel), add_empty_pixels)))

    # divide the array into an array of pixel arrays
    array = np.asarray(np.split(array, len(array) / channels_per_pixel))

    # get the shapes of all potential 2d arrays which the specified array can be shaped into
    shapes = get_factor_pairs(len(array))
    print(pd.DataFrame({
        "Possible 2d array shapes": shapes
    }))

    # select an output array shape (1), reshape the 1d array (2), and return the new 2d array (3)
    # (1)
    # select the correct shape, check if the array is wide or tall
    if wide is False:
        shape = np.flip(shapes[select])
    shape = np.array((*shapes[select], channels_per_pixel), int)
    print("Output array shape =", shape)

    # (2)
    array_2d = array.reshape(shape)

    # (3)
    return array_2d


# TODO
def shift_array():
    pass
