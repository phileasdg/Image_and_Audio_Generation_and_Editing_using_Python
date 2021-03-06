import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import IPython.display as ipd
import soundfile as sf
from pathlib import Path

"""
read audio file as an array
"""


def read_audio(path, mono=False, return_sr=False):
    y, sr = librosa.load(path, mono=mono)
    if return_sr is False:
        return np.asarray(y)
    else:
        return np.asarray(y), sr


"""
plot audio file as a graph
"""


def plot_waveform(audio_data, sample_rate=22050, title=""):
    plt.figure(figsize=(14, 5))
    plt.title(title)
    librosa.display.waveshow(audio_data, sample_rate)


"""
plot audio file as a spectrogram
"""


def plot_spectrogram(audio_data, sample_rate=22050, title="", log_frequency_scale=False, figsize=(14, 5),
                     axis=True, save_path=None):
    # "The first thing we might want to do is display an ordinary (linear) spectrogram.
    # We’ll do this by first computing the short-time Fourier transform, and then mapping
    # the magnitudes to a decibel scale". (librosa.org: Using display.specshow)

    data = librosa.stft(audio_data)  # STFT of audio_data
    S_db = librosa.amplitude_to_db(np.abs(data), ref=np.max)  # decibel scale magnitudes

    fig, ax = plt.subplots(figsize=figsize)
    y_scale = ("linear", "log")
    img = librosa.display.specshow(S_db, x_axis="time", y_axis=y_scale[log_frequency_scale], ax=ax, sr=sample_rate)
    if axis is True:
        ax.set(title=title)
        fig.colorbar(img, ax=ax, format="%+2.f dB")
    else:
        plt.axis('off')
    if save_path is not None:
        if axis is True:
            plt.savefig(save_path)
        else:
            plt.savefig(save_path, bbox_inches='tight', pad_inches=0)


"""
play audio from array
"""


def play_audio_from_array(audio_data, sample_rate=22050):
    return ipd.Audio(audio_data, rate=sample_rate)


"""
save an array as an audio file
"""


def save_audio(audio_data, sample_rate=22050, path="saved_audio.wav", mono=False):
    if mono is True:
        sf.write(path, audio_data, sample_rate)
    else:
        sf.write(path, audio_data.T, sample_rate)
    file = Path(path)
    if file.is_file():
        print("Audio saved at: " + path)
