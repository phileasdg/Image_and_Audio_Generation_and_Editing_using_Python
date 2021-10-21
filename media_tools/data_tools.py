import numpy as np

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
split data array along rows or columns into n smaller arrays 
"""


#TODO
def split_array(array):
    if type(array) == np.ndarray:
        print("you did it")

# TODO
def shift_array():
    pass
