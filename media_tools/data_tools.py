import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

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


def invert_array(array, uint8=False):
    if uint8 is True:
        array = 255 - array
    else:
        array = 1 - array
    return array


"""
split a 1d array into a 2d array (good for converting things to image) split data array along rows into an array of n 
smaller arrays 
"""


def array_1d_to_2d(array, add_empty_pixels=0, channels_per_pixel=3, select=-1, wide=True, return_possible_shapes=False):
    # add observations so as  to enable perfect division of array into pixel cells
    add_observations = len(array) % channels_per_pixel
    array = np.concatenate((array, np.zeros(add_observations)))

    # add add_empty_pixels number of empty pixel arrays to the array
    array = np.concatenate((array, np.tile(np.zeros(channels_per_pixel), add_empty_pixels)))

    # divide the array into an array of pixel arrays
    array = np.asarray(np.split(array, len(array) / channels_per_pixel))

    # get the shapes of all potential 2d arrays which the specified array can be shaped into
    shapes = get_factor_pairs(len(array))
    if return_possible_shapes is True:
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


"""
plot a histogram of the data in an array (flatten it first)
"""


def plot_histogram(array, bins="auto"):
    array = array.flatten()
    plt.hist(array, bins=bins)
    plt.show()


"""clip an array to values within a range around the mean of the array, or another value (point), expressed in 
standard deviations """


def clip_array_stdev_around_point(array, n_stdev=4, point=None):
    if point is None:
        point = np.mean(array)
    stdev = np.std(array)
    array = np.clip(array, point - n_stdev * stdev, point + n_stdev * stdev)
    return array


"""
clip an array to values within a range around a value in the array (point), expressed as an upper and lower bound
"""


def clip_array_around_point(array, point=None, lower_bound=None, upper_bound=None):
    if point is None:
        point = np.mean(array)
    if lower_bound is None:
        lower_bound = point - np.std(array) * 4
    if upper_bound is None:
        upper_bound = point + np.std(array) * 4
    array = np.clip(array, point - lower_bound, point + upper_bound)
    return array


"""
rotate a 2d array around a point (default is the centre of the array)

# cv2 border types: # cv2.BORDER_CONSTANT, cv2.BORDER_REPLICATE, cv2.BORDER_REFLECT, cv2.BORDER_WRAP, 
cv2.BORDER_REFLECT_101, cv2.BORDER_DEFAULT 
"""


def rotate_2d_array_around_point(array, angle, bound=True, border_type=cv2.BORDER_CONSTANT, border_value=0,
                                 interpolation=cv2.INTER_LINEAR):
    # make the point of rotation the center of the array
    point = tuple(np.array(array.shape[1::-1]) / 2)

    # get height and width of the array
    h, w = array.shape[:2]

    if bound:
        # get the rotation matrix
        matrix = cv2.getRotationMatrix2D(point, -angle, scale=1.0)
        # get the sine and cosine
        cos = np.abs(matrix[0, 0])
        sin = np.abs(matrix[0, 1])
        # compute the new bounding dimensions of the array
        nH = int((h * cos) + (w * sin))
        nW = int((h * sin) + (w * cos))
        # adjust the rotation matrix to take into account translation
        matrix[0, 2] += (nW / 2) - point[0]
        matrix[1, 2] += (nH / 2) - point[1]
        # perform the actual rotation and return the array
        return cv2.warpAffine(array, matrix, dsize=(nW, nH), borderMode=border_type, borderValue=border_value,
                              flags=interpolation)
    else:
        # rotate the array
        return cv2.warpAffine(array, cv2.getRotationMatrix2D(point, -angle, 1.0), array.shape[1::-1],
                              borderMode=border_type, borderValue=border_value)


"""
rescale an array to a new size (by stretching and squishing)

# interpolation methods: # cv2.INTER_NEAREST, cv2.INTER_LINEAR, cv2.INTER_AREA, cv2.INTER_CUBIC, cv2.INTER_LANCZOS4
"""


def rescale_2d_array(array, new_dimensions=(2000, 2000), interpolation=cv2.INTER_CUBIC):
    array = cv2.resize(array, dsize=new_dimensions, interpolation=interpolation)
    return array


"""
rescale a 2d array by a factor along one or more axes
"""


def rescale_2d_array_by_factor(array, factor, axes: tuple = (0, 1), interpolation=cv2.INTER_CUBIC):
    # get the original dimensions of the array
    dim = np.flip(np.asarray(array.shape[:2]))
    for axis in axes:
        # get the new dimensions of the array
        dim[axis] *= factor
    # resize the array
    array = cv2.resize(array, dsize=(dim), interpolation=interpolation)
    return array


"""
flip an array along one or more axes
"""


def flip_2d_array(array, axes: tuple = (0, 1)):
    array = np.flip(array, axes)
    return array


"""
translate a 2d array
"""


def translate_2d_array(image, x, y, border_type=cv2.BORDER_WRAP, border_value=(0, 0, 0)):
    # define the translation matrix and perform the translation
    matrix = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]), borderMode=border_type,
                             borderValue=border_value)
    # return the translated image
    return shifted


"""
roll an array along one or more axes (you can use this to translate an array along one or more axes)
"""


def roll_array(array, shift, axes=0):
    array = np.roll(array, shift, axis=axes)
    return array
