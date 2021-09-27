import cv2
import matplotlib.pyplot as plt

"""
read an image as an array
"""


def read_image(path):
    image = cv2.imread(path)
    return image


"""
display an array as an image
"""


def show_image(image, axis=True, title="", scale_ratio=2):
    plt.figure(figsize=[scale_ratio*x for x in plt.rcParams["figure.figsize"]])
    plt.title(title)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    if axis is not True:
        plt.axis('off')
    plt.show()


"""
save a numpy array as an image
"""


def save_image(image, path="saved_image.png"):
    cv2.imwrite(path, image)
