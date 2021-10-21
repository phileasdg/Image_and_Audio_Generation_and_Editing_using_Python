import os.path
from IPython.display import Video
from moviepy.editor import *

"""
read video data from a file and returns a video data object
"""


def read_video(path):
    clip = VideoFileClip(path)
    return clip


"""
save a video object as a video file
"""


def save_video(video, path="saved_video.avi", fps=None):
    clip = video

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
    except AttributeError:
        print("An error occurred. Please troubleshoot the following:\n"
              "- make sure the video file referred to by the video_path has audio\n"
              "- make sure the paths specify the appropriate save file formats")


"""
assign audio to a video file
"""


def assign_audio_to_video_from_files(audio_path, video_path, video_copy_save_path=None, fps=None, subclip=None):
    clip = VideoFileClip(video_path)
    if subclip is None:
        subclip = (0, clip.duration)

    if fps is None:
        fps = clip.fps
    clip.subclip(*subclip)

    if video_copy_save_path is None:
        video_copy_save_path = video_path

    audio_clip = AudioFileClip(audio_path).subclip(*subclip)
    clip.audio = audio_clip
    clip.write_videofile(video_copy_save_path, fps=fps)
