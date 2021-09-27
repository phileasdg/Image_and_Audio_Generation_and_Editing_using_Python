import numpy as np


def normalise_array(array, uint8=False):
    array = (array - np.min(array)) / np.ptp(array)
    if uint8 is True:
        array = (250 * array).astype(int)
    return array


def clip_array(array, val_min=None, val_max=None):
    if val_min is None:
        val_min = np.min(array)
    if val_max is None:
        val_max = np.max(array)
    array = np.clip(array, val_min, val_max)
    return array
