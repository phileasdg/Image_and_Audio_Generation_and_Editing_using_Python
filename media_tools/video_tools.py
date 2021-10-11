import os.path
import cv2
import numpy as np
from IPython.display import Video
from moviepy.editor import *
from moviepy.audio.AudioClip import AudioArrayClip

"""
read video data from a file and returns a video data array
"""


def read_video(path, video_as_array=True):
    clip = VideoFileClip(path)

    if video_as_array is True:
        nframes = clip.reader.nframes
        frames = []
        for i in range(nframes):
            frames.append(clip.get_frame(i))
        fps = clip.fps*2
        return np.asarray(frames), fps
    else:
        return clip


"""
save a video array as a video file
"""


def save_video(video, path="saved_video.avi", fps=None, video_is_image_array=True):
    clip = video

    # is the video data in an array of images?
    if video_is_image_array is True:
        if fps is None:
            print("fps parameter left out, defaulting to fps == 30")
            fps = 30
        clip = ImageSequenceClip(list(video), fps=fps)

    # is the video a moviepy video object
    else:
        if fps is None:
            fps = clip.fps

    # save the video
    clip.write_videofile(path, fps=fps)


"""
open a video file using the os default application
"""


def open_video_os_default(path):
    os.startfile(path, 'open')


"""
play video from file (will not work for large video files)
"""


def play_from_file(path):
    return Video(path)


"""
save an audio file copy from a video file
"""


def save_audio_from_video(video_path, audio_save_path):
    audio_clip = VideoFileClip(video_path).audio

    try:
        audio_clip.write_audiofile(audio_save_path)
    except:
        AttributeError()
        print("The video file referred to by the video_path has no audio.")


"""
assign audio to a video file
"""


def assign_audio_to_video(audio, video, fps=None, sample_rate=None, video_is_image_array=True, subclip=None):
    clip = video

    if video_is_image_array is True:
        if fps is None:
            print("fps parameter left out, defaulting to fps == 30")
            fps = 30
        clip = ImageSequenceClip(list(video), fps=fps)

    if sample_rate is None:
        print("sample_rate parameter left out, defaulting to sample_rate == 22050")
        sample_rate = 22050

    if subclip is None:
        subclip = (0, clip.duration)

    clip.subclip(*subclip)
    audio_clip = AudioArrayClip(audio, fps=sample_rate)
    audio_clip.subclip(*subclip)

    clip.set_audio(audio_clip)
    return clip


def assign_audio_to_video_from_files(audio_path, video_path, video_copy_save_path, fps=30, subclip=None):
    clip = VideoFileClip(video_path)
    if subclip is None:
        subclip = (0, clip.duration)
    clip.subclip(subclip)
    audio_clip = AudioFileClip(audio_path).subclip(subclip)
    clip.set_audio(audio_clip)
    clip.write_videofile(video_copy_save_path, fps=fps)
