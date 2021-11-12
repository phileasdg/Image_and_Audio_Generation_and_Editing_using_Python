import numpy as np
from media_tools import *

# get a set of points in cartesian coordinates
def get_points(n, x_min=0, x_max=1, y_min=0, y_max=1, ndim=2):
    points = np.zeros((n, 2))
    for i in range(n):
        for j in range(ndim):
            points[i][j] = x_min + (x_max - x_min) * np.random.random()
    return points

points = get_points(10)
points = (points * 10).astype(int)
print("points:\n", points)
# convert points to integer coordinates

# get the coordinates of the smallest rectangle that contains all the points
# the rectangle is defined by the list of points [A, B, C, D] where each point is a tuple (x, y)

def get_rectangle(points):
    x_min = points[0][0]
    x_max = points[0][0]
    y_min = points[0][1]
    y_max = points[0][1]

    for i in range(1, len(points)):
        x_min = min(x_min, points[i][0])
        x_max = max(x_max, points[i][0])
        y_min = min(y_min, points[i][1])
        y_max = max(y_max, points[i][1])

    return [x_min, x_max, y_min, y_max]

smallest_rectangle = get_rectangle(points)
print("smallest rectangle:\n", smallest_rectangle)

# the rectangle is defined by the list [x, y, w, h]

def get_smallest_rectangle_xywh(points):
    x_min = points[0][0]
    x_max = points[0][0]
    y_min = points[0][1]
    y_max = points[0][1]

    for i in range(1, len(points)):
        x_min = min(x_min, points[i][0])
        x_max = max(x_max, points[i][0])
        y_min = min(y_min, points[i][1])
        y_max = max(y_max, points[i][1])

    return [x_min, y_min, x_max - x_min, y_max - y_min]

smallest_rectangle_xywh = get_smallest_rectangle_xywh(points)
print("smallest rectangle xywh:\n", smallest_rectangle_xywh)
smallest_rectangle_array = np.zeros(smallest_rectangle_xywh[2:])
print("smallest rectangle array:\n", smallest_rectangle_array)

image_tools.show_image(smallest_rectangle_array, axis=True, title="smallest rectangle array")

# test with a rectangle
points = np.array([[0, 0], [0, 2], [1, 2], [1, 0]])
print("points:\n", points)
smallest_rectangle = get_rectangle(points)
print("smallest rectangle:\n", smallest_rectangle)
smallest_rectangle_xywh = get_smallest_rectangle_xywh(points)
print("smallest rectangle xywh:\n", smallest_rectangle_xywh)
smallest_rectangle_array = np.zeros(smallest_rectangle_xywh[2:])
print("smallest rectangle array:\n", smallest_rectangle_array)

image_tools.show_image(smallest_rectangle_array, axis=True, title="smallest rectangle array")


# get a set of points in n-dimensional coordinates
def get_points(n, x_min=0, x_max=1, y_min=0, y_max=1, ndim=2):
    points = np.zeros((n, 2))
    for i in range(n):
        for j in range(ndim):
            points[i][j] = x_min + (x_max - x_min) * np.random.random()
    return points


# find the bounding box
def get_bounding_box(points):
    # check how many dimensions the points have
    ndim = len(points[0])
    # find the bounding box
    bounding_box = []
    for i in range(ndim):
        min_val = points[0][i]
        max_val = points[0][i]
        for j in range(1, len(points)):
            min_val = min(min_val, points[j][i])
            max_val = max(max_val, points[j][i])
        bounding_box.append([min_val, max_val])
    return bounding_box

bounding_box = get_bounding_box(points)


# convert the ndim bounding box data to point coordinates:
def convert_bounding_box_to_points(bounding_box):
    # get the number of dimensions
    ndim = len(bounding_box)

    return np.asarray(points)

bounding_box_points = convert_bounding_box_to_points(bounding_box)
print("bounding_box_points:\n", bounding_box_points)
