import numpy as np
from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt

wave_file = "1-103995-A-30.wav"


def read_wave_file(file, sample_rate):
    # read sample rate and data from wave file
    original_sample_rate, orginal_audio_data = wavfile.read(file)

    # normalize input to floating-point value, if needed
    if orginal_audio_data.dtype is np.float32:
        audio_data_float32 = orginal_audio_data
    else:
        audio_data_float32 = orginal_audio_data / np.iinfo(orginal_audio_data.dtype).max

    # down sample to desired sample rate
    audio_data = signal.resample(audio_data_float32, (len(audio_data_float32) // original_sample_rate) * sample_rate)

    return audio_data


audio_sample_rate = 16000

audio_samples = read_wave_file(wave_file, audio_sample_rate)

print(f"Successfully read {len(audio_samples)} samples from '{wave_file} with sample rate of {audio_sample_rate}")


fig = plt.figure(figsize=(8, 6))

plt.title("Audio waveform for wave file.")
plt.plot(audio_samples)
plt.xlabel("Samples")
plt.xlim(0, len(audio_samples))
plt.ylabel("Amplitude")
plt.show()
