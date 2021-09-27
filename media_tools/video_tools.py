from moviepy.editor import *


# loading video dsa gfg intro video
def read_video(path):
    clip = VideoFileClip(path)
    return clip


def video_subclip(video_data, subclip=None):
    # if the subclip parameter is undefined, do not clip the video
    if subclip is None:
        subclip = (0, video_data.duration())
    # getting video for only starting 10 seconds
    clip = video_data.subclip(subclip)
    return clip


def rotate_video(video_data):
    # rotate video by 180 degree
    clip = video_data.rotate(180)
    return clip


def scale_volume(video_data):
    # Multiply the audio volume by the multiplying factor (volume x 0.5)
    clip = video_data.volumex(0.5)
    return clip


def show_video(video_data):
    # showing clip
    video_data.ipython_display(width=280)
