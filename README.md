# Speech Emotion Recognition (SER) Project

# Overview
This project implements a Speech Emotion Recognition (SER) system to classify emotions from spoken language using the RAVDESS dataset . The system extracts acoustic features such as MFCCs , Chroma , Spectral Contrast , and Mel-Spectrogram from audio files and uses a deep learning model to predict emotions like happiness, sadness, anger, and more.

# Key Features
Feature extraction using librosa.
Multi-input deep learning model combining Mel-Spectrograms and other features.
Evaluation metrics: Accuracy, F1-Score, and Confusion Matrix.
Visualizations for better insights into model performance.
Dataset
The project uses the RAVDESS dataset for Speech Emotion Recognition.

# Dataset Details
Source : RAVDESS Dataset
Structure :
Contains .wav files with corresponding emotion labels.
Emotions include: Neutral, Calm, Happy, Sad, Angry, Fearful, Disgust, Surprised.
Each file is labeled with an emotion code in its filename (e.g., 03 for "Happy").
Preprocessing :
Audio files are preprocessed to extract features like MFCCs, Chroma, Spectral Contrast, and Mel-Spectrogram.
Features are padded/truncated to a fixed length for consistency.
How to Obtain the Dataset
Visit the official RAVDESS dataset page: RAVDESS Dataset on Zenodo .
Download the dataset (Audio-only or Audio-Video versions).
Extract the dataset and place it in the data/ directory.
Dataset Organization
After extraction, organize the dataset as follows:

data/
├── Actor_01/
│   ├── 03-01-01-01-01-01-01.wav
│   ├── 03-01-02-01-01-01-01.wav
│   └── ...
├── Actor_02/
│   ├── 03-01-01-01-01-01-02.wav
│   ├── 03-01-02-01-01-01-02.wav
│   └── ...
└── ...
Each filename encodes metadata about the file:

Example : 03-01-02-01-01-01-01.wav
03: Modality (03 = audio-only).
01: Vocal channel (01 = speech).
02: Emotion (02 = calm).
Remaining fields encode intensity, statement, repetition, and actor ID.

# SER Project -- Ravdess Dataset
For Q1 -- https://github.com/M23CSA520/Speech_Understanding_PA1/blob/main/m23csa520_speech_q1_pa1.py
          https://github.com/M23CSA520/Speech_Understanding_PA1/blob/main/M23CSA520_Speech_Q1_PA1.ipynb
          https://github.com/M23CSA520/Speech_Understanding_PA1/blob/main/SER_Q1_Report.pdf


# Analyzing Different Window Techniques -- Urban8k Dataset
For Q2 -- Task A -- https://github.com/M23CSA520/Speech_Understanding_PA1/blob/main/m23csa520_q2_taska_pa1.py
                    https://github.com/M23CSA520/Speech_Understanding_PA1/blob/main/M23CSA520_Q2_TaskA_PA1.ipynb
                    https://github.com/M23CSA520/Speech_Understanding_PA1/blob/main/Speech_Understanding_Q2_TaskA_PA1.pdf


# Analyzing Spectrograms generated for different genres of music ( Classical , Jazz, Rock , Ghazal )
All Songs were uploaded to Google Colab
    "Classical": "/content/songs/Ek Chatur Naar Karke Sringar - Padosan.mp3",
    "Rock": "/content/songs/Alvida - Life In A Metro 320 Kbps.mp3",
    "Jazz": "/content/songs/Hosanna - Ekk Deewana Tha 320 Kbps.mp3",
    "Ghazal": "/content/songs/Woh Kaghaz Ki Kashti - The Latest 320 Kbps.mp3"
For Q2 -- Task B -- https://github.com/M23CSA520/Speech_Understanding_PA1/blob/main/m23csa520_speech_q2_taskb.py
                    https://github.com/M23CSA520/Speech_Understanding_PA1/blob/main/M23CSA520_Speech_Q2_TaskB.ipynb
                    https://github.com/M23CSA520/Speech_Understanding_PA1/blob/main/PA1_Q2_TaskB.pdf




