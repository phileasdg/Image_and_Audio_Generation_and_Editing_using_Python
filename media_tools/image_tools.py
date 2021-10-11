import cv2
import matplotlib.pyplot as plt
from pathlib import Path

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


def show_image(image, axis=True, title="", scale_ratio=2):
    plt.figure(figsize=[scale_ratio*x for x in plt.rcParams["figure.figsize"]])
    plt.title(title)
    plt.imshow(image, cmap="gray")
    if axis is not True:
        plt.axis('off')
    plt.show()


"""
save a numpy array as an image
"""


def save_image(image, path="saved_image.png"):
    cv2.imwrite(path, image)
    file = Path(path)
    if file.is_file():
        print("Image saved at: "+path)
