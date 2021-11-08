### plot a face portrait

import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# make a large empty array
face = np.zeros((500, 500))

# draw the head
face[100:300, 100:300] = 0.2
# draw the eyes
face[150:200, 150:200] = 0.5
# draw the mouth
face[200:250, 200:250] = 0.5
# draw the nose
face[150:200, 250:300] = 0.3

# plot the face
plt.imshow(face, cmap='gray')
plt.show()