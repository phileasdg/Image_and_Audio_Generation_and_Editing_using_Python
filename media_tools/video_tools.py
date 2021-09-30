import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import os.path

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
play video from video array
"""


def play_from_array(video, fps=30, axis=False, scale_ratio = .5):
    fig = plt.figure(figsize=[scale_ratio*x for x in plt.rcParams["figure.figsize"]])
    for frame in video:
        plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), animated = True)
    if axis is not True:
        plt.axis('off')
    animation.ArtistAnimation(fig, video, interval=1000/fps, blit=True)
    plt.show()
