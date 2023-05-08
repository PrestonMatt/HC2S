from PIL import Image
from winsound import Beep
import numpy as np
import sounddevice as sd

def compile_sounds(width:int, h_curve:list, img):
    """
        Given the length of one of the sides in a square image
        assign a frequency based on RGBA value.

        Then it adds them all together.

        Intuitively, I think it makes sense that the brighter
        colors have a higher freqency and so forth.

        The frequency is louder the higher the transparency.
    """

    """
        First we need a mapping of RGB values to frequencies
        RGB values go from 0x000000 (cooler)
        to 0xFFFFFF (warmer).

        winsound's Beep takes frequencys 37 hertz through 32,767 hertz
        This is only 0x7fda values
    """
    #define the range that winsound takes:
    min_hertz = 37
    max_hertz = 32767

    #try to evenly map out the smaller frequency lane to the color space of RBG
    colors = np.zeros((256,256,256), dtype = np.int32)
    for red in range(256):
        for green in range(256):
            for blue in range(256):
                #log scale of mapping frequency
                freq = np.exp( (np.log(max_hertz) - np.log(min_hertz))
                                    / 16777215 * (red * 65536 + green * 256 + blue) 
                                    + np.log(min_hertz) )
                colors[red, green, blue] = int(freq)

    sounds = []
    area = width * width
    for pixel_index in range(area):
        pixel_coords = h_curve[pixel_index]
        rgba_val = img.getpixel(pixel_coords)
        red_ = rgba_val[0]
        green_ = rgba_val[1]
        blue_ = rgba_val[2]
        pixel_freq = colors[red_, green_, blue_]
        sounds.append(pixel_freq)

    play_multiple_freq_at_once(freqs=sounds,duration=1.0)
    
    
def play_multiple_freq_at_once(freqs:list, duration=1.0):
    """
        Given a list of freqencies to play and a duration,
        play the frequencies at once using math
        to calculate and summate their sinwaves in the air.
    """
    #The sound duration will be one second by default

    #This creates a time array which corresponds to the duration of the sinwave
    time = np.arange(int(44100 * duration)) / 44100

    #We need to add together the sinwaves of each frequency to play them at once.
    #This will hold our sinwaves:
    sounds = []
    for freq in freqs:
        #calculate the sinwave:
        wave = np.sin(2*np.pi * freq * time)
        sounds.append(wave)

    #add together the sinwaves now:
    comosite_sinwave = np.sum(sounds, axis = 0)
    #This normalizes the composite_sinwave as a range in [-1, 1]
    comosite_sinwave /= np.max(np.abs(comosite_sinwave))

    #Finally, play the composite wave:
    sd.play(comosite_sinwave, samplerate=44100, blocking=True)