# Transformation index:

In this repository, we will explore the following transformations of image arrays:

- **Scaling**: we can scale the data by a constant factor, or to fit a range.
- **Rotations**: we can rotate the data by a given angle.
- **Translation**: we can translate the data by a given offset.
- **Rolling**: we can roll the data by a given offset.
- **Shear**: we can shear the data by a given angle.
- **Reflection**: we can reflect the data by a given angle, or by a given axis.
- **Cropping**: we can crop the data to a range of indices.
- **Blitting**: we can blit the data from a source array to a destination array.

Note: While the examples provided here work with image arrays, they are able to work with any data cast into an image array
format. Consequently, with data mapping, these transformations can be applied to any array of values, whether intended to
be viewed as an image or not, although depending on the number of dimensions of the source array, the steps required to map
it into two dimensions, and either 1, 3, or 4 colour channels will vary. See the documentation in this repository on direct
data mapping for more information. 