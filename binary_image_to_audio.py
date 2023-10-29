import numpy as np
from PIL import Image
import random
import time
import beep_generator

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_path', nargs='?', default="WolframRule30.png", type=str)
    parser.add_argument('--min_random_freq', nargs='?', default="400", type=int)
    parser.add_argument('--max_random_freq', nargs='?', default="4000", type=int)
    parser.add_argument('--beep_duration_ms', nargs='?', default="100", type=int)
    parser.add_argument('--silence_duration_ms', nargs='?', default="50", type=int)

    args = parser.parse_args()

    # Load the binary image (pure black and white)
    image = Image.open(args.image_path)
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
                frequency = random.randint(args.min_random_freq, args.max_random_freq)
                bg.append_sinewave(volume=1, duration_milliseconds=args.beep_duration_ms, freq=frequency)
            else:
                bg.append_silence(duration_milliseconds=args.silence_duration_ms)
    
    output_filename = f'{time.strftime("%Y%m%d-%H%M%S")}.wav'
    print (f"Audio saved at {output_filename}")
    bg.save_wav(output_filename)