import numpy as np
from media_tools import *
import cv2


# given a list of points described by (x, y), an origin point described by (ox,oy), and an angle, return the coordinates of the rotated point
def rotate_points(points, origin=None, angle=0):
    points = np.array(points)
    if origin is None:
        # origin is the center of the points
        origin = (np.mean(points[:, 0]), np.mean(points[:, 1]))
        print("origin:", origin)
    # find the new coordinates of each point based on the origin and angle
    # formula = (cos(theta) * (x - ox) - sin(theta) * (y - oy) + ox, sin(theta) * (x - ox) + cos(theta) * (y - oy) + oy)
    points = np.dot(np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]), (points - origin).T).T + origin
    return points.tolist()

# test the rotation function
points = ((0, 0), (10, 0), (10, 10), (0, 10))
print("points:", points)
# origin = mean (points)
origin = np.mean(points, axis=0)
print("origin:", origin)

# given a rectangle, described by the tuple (x, y, w, h, theta), what is the rectangle with theta = 0 that contains the rotated rectangle?


# given a rectangle rotated around its center, described by the tuple (x, y, w, h, theta), what are the coordinates of
# the corners of the rectangle?

def find_point_coords(rect):
    x, y, w, h, theta = rect
    theta = theta % 360
    if theta == 0:
        return (x, y), (x + w, y), (x + w, y + h), (x, y + h)
    else:
        # create a list of points on the rectangle
        points = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
        # apply rotation to each point around the center of the rectangle
        points = rotate_points(points, angle=theta)
        return points


# convert coordinates of points on a plane to coordinates on an image array
# coords = a list of tuples of coordinates
def coordinate_convert_plane_to_array(coords, image_shape):
    # convert coordinate tuples to support item assignment
    coords = np.array(coords).astype(list)
    for coord in coords:
        coord[0] = coord[0] + image_shape[1] // 2
        coord[1] = image_shape[0] - coord[1] + image_shape[0] // 2

    # return a list of tuples of converted coordinates
    return coords

# generate a white image
img = np.ones((500, 500, 3), np.uint8) * 255
# rotate the image by an angle
img_rot = image_tools.rotate_image(img, 45)
# show the image
# image_tools.show_image(img_rot, axis=True, title="rotated image")

# calculate the coordinates of the corners of the rotated rectangle
rect1 = (0, 0, 500, 500, 45)
rect1_points = find_point_coords(rect1)

# convert the coordinates of the corners to the coordinates of the corners of the image
rect1_points = coordinate_convert_plane_to_array(rect1_points, img_rot.shape[:2])
print(rect1_points)

# draw the rectangle on the image
# # fill the area in between the corners of the rectangle with green
# cv2.fillConvexPoly(img_rot, np.array(((0,350), (350,0), (350, 700), (700, 350)), dtype=np.int32), (0, 255, 0))
img_filled = cv2.fillConvexPoly(img_rot, np.array(rect1_points, dtype=np.int32), (0, 255, 0))
image_tools.show_image(img_filled, axis=True, title="filled rectangle")