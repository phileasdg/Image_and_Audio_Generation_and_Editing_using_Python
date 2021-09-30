import cv2
import numpy as np

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
    video = np.stack(frames, axis=0)
    return video


"""
read video data from the device camera and returns a video data array
"""


def read_video_from_camera():
    pass


def save_video(video, path="saved_video.avi"):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    length, width = video.shape[1:3]
    video_out = cv2.VideoWriter(path, fourcc, format(video.get(cv2.CAP_PROP_FPS)))
    for frame in video:
        video_out.write(frame)
    video_out.release()
    cv2.destroyAllWindows()


def show_video():
    pass
