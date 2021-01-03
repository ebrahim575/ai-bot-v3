import sounddevice as sd
import numpy as np
from pygame import mixer  # Load the popular external library
import winsound


def music():
    mixer.init()
    mixer.music.load('C:\\Users\\ezulq\\Desktop\\Music\\iwachan.mp3')
    mixer.music.play()


def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    print(int(volume_norm))
    if int(volume_norm) > 100:
        frequency = 500  # Set Frequency To 2500 Hertz
        duration = 800  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
with sd.Stream(callback=print_sound):
    sd.sleep(2147483646)
