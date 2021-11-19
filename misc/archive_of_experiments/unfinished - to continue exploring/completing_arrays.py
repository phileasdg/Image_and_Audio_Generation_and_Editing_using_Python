import numpy as np
from media_tools import *

sample_media = "C:/Users/pdazeley-gaist23/PycharmProjects/Image_and_Audio_Generation_and_Editing_using_Python/sample_media/"

image = np.array([[1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
                  ])

audio = np.random.randint(0, 255, 231168)  # len = 231168
audio = audio_tools.read_audio(sample_media+"stereo_sample.wav", mono=True, return_sr=False)

image_greyscale = image_tools.array_1d_to_grayscale(audio)
image_tools.show_image(image_greyscale)

image_colour = image_tools.array_1d_to_rgb(audio)
image_tools.show_image(image_colour)
image_tools.show_image(data_tools.invert_array(image_colour))