# -*- coding: utf-8 -*-
"""M23CSA520_Speech_Q2_TaskB.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kMvB0npGYq8a7lk0bKCQ2GvI1UZ2rTrc
"""

import os
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Define paths to the songs (in .mp3 format)
song_paths = {
    "Classical": "/content/songs/Ek Chatur Naar Karke Sringar - Padosan.mp3",
    "Rock": "/content/songs/Alvida - Life In A Metro 320 Kbps.mp3",
    "Jazz": "/content/songs/Hosanna - Ekk Deewana Tha 320 Kbps.mp3",
    "Ghazal": "/content/songs/Woh Kaghaz Ki Kashti - The Latest 320 Kbps.mp3"
}

# Function to generate and plot spectrograms
def generate_spectrograms(song_paths):
    plt.figure(figsize=(15, 10))

    for i, (genre, path) in enumerate(song_paths.items(), 1):
        # Load the audio file
        y, sr = librosa.load(path, sr=None)  # Librosa can handle .mp3 files

        # Compute the spectrogram using STFT
        D = librosa.stft(y)
        D_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

        # Plot the spectrogram
        plt.subplot(2, 2, i)
        librosa.display.specshow(D_db, sr=sr, x_axis='time', y_axis='log')
        plt.colorbar(format='%+2.0f dB')
        plt.title(f"Spectrogram - {genre}")

    plt.tight_layout()
    plt.show()

# Generate spectrograms for all songs
generate_spectrograms(song_paths)