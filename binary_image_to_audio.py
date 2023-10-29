import numpy as np
from PIL import Image
import random
import time
import beep_generator

# Load the binary image (pure black and white)
image_path = "WolframRule30.png"
image = Image.open(image_path)
img_data = np.array(image)

# Generate audio samples

bg = beep_generator.BeepGenerator()

i=0
for row in img_data:
    print(f"row {i}:", end="")
    i = i+1
    print(''.join(str(i) for i in row))
    for pixel_value in row:
        
        if pixel_value == 0:  # Black pixel
            frequency = random.randint(400, 4000)
            bg.append_sinewave(volume=1, duration_milliseconds=100, freq=frequency)
        else:
            bg.append_silence(duration_milliseconds=50)

bg.save_wav(f'{time.strftime("%Y%m%d-%H%M%S")}.wav')


    