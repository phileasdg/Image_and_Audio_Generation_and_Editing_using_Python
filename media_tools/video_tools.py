import os.path
import cv2
import numpy as np
from IPython.display import Video

"""
read video data from a file and returns a video data array
"""


def read_video(path):
    frames = []
    video = cv2.VideoCapture(path)
    ret = True
    while ret:
        ret, frame = video.read()  # read one frame from the video capture object
        if ret:
            frames.append(frame)
    fps = video.get(cv2.CAP_PROP_FPS)
    video.release()
    video = np.stack(frames, axis=0)
    return video, fps


"""
read video data from the device camera and returns a video data array
"""


def read_video_from_camera():
    pass


"""
save a video array as a video file
"""


def save_video(video, fps=30, path="saved_video.avi"):
    height, width = video.shape[1:3]

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_out = cv2.VideoWriter(path, fourcc, fps, (width, height))

    for frame in video:
        video_out.write(frame)
    video_out.release()
    if os.path.isfile(path):
        print("Video saved at:", path)


"""
open a video file using the os default application
"""


def open_video_os_default(path):
    os.startfile(path, 'open')


"""
play video from file
"""


def play_from_file(path):
    return Video(path)