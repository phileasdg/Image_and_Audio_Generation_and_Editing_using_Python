import numpy as np
from moviepy.editor import *

sample_media = "C:/Users/pdazeley-gaist23/PycharmProjects/Image_and_Audio_Generation_and_Editing_using_Python/sample_media/"

# read video
path = sample_media + "sample_video.mp4"
clip = VideoFileClip(path)


def my_filter(get_frame, t):
    frame = get_frame(t)
    white_frame = np.full(frame.shape, 255)
    frame = white_frame - frame
    return frame


clip = clip.fl(my_filter)

# save video
save_path = sample_media + "example_saved_video.mp4"
# clip = ImageSequenceClip(frames, fps=fps, load_images=True)
clip.write_videofile(save_path, fps=clip.fps)
