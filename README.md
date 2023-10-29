# Binary Image to Audio Converter

## Introduction

The Binary Image to Audio Converter is a Python script designed to convert binary images into audio files. It provides a simple command-line interface with various configurable options to customize the generated audio.

## Usage

```shell
python binary_image_to_audio.py [--image_path IMAGE_PATH] [--min_random_freq MIN_RANDOM_FREQ]
                               [--max_random_freq MAX_RANDOM_FREQ] [--beep_duration_ms BEEP_DURATION_MS]
                               [--silence_duration_ms SILENCE_DURATION_MS] [--varied_tones] [--constant_freq CONSTANT_FREQ]
```

## Arguments

    --image_path: Path to the binary image file for audio conversion. (Default: "WolframRule30.png")

    --min_random_freq: Minimum frequency for random tone generation in Hz. (Default: 400)

    --max_random_freq: Maximum frequency for random tone generation in Hz. (Default: 4000)

    --beep_duration_ms: Duration of each beep in milliseconds. (Default: 100)

    --silence_duration_ms: Duration of silence between beeps in milliseconds. (Default: 50)

    --varied_tones: Use this flag if you want the generated audio to have varied tones.

    --constant_freq: Constant frequency for audio generation in Hz (if not using varied tones) (Default: 440)
    
    --display_image: Use this flag if you want print the binary image array to the console. It will print a '0' for a black pixel and '1' for a whte pixel
    
## Examples

- Convert a binary image to audio with default settings:

```shell
python binary_image_to_audio.py
```

- Convert a binary image to audio with custom parameters:

```shell
python binary_image_to_audio.py --min_random_freq 200 --max_random_freq 3000 --beep_duration_ms 150 --silence_duration_ms 60
```

- Convert a binary image to audio with constant frequency tone of 800 Hz:

```shell
python binary_image_to_audio.py --constant_freq 880
```

- Convert a binary image to audio with varied tones randomly betwwen 200 Hz and 3000 Hz:

```shell
python binary_image_to_audio.py --varied_tones min_random_freq 200 --max_random_freq 3000
```

## Acknowledgements
* Beep generation code: "python - how can I generate a WAV file with beeps?"; StackOverflow; Rik Mulder; Dec 6, 2022 at 23:48; https://stackoverflow.com/a/74710298
* Test image: 1st 50 rows of Stephen Wolfram's Rule 30 cell automaton. Generated by Zhiming Wang (zmwangx): https://github.com/zmwangx/rule30; Cropped from https://github.com/zmwangx/rule30/blob/master/images/rule30.png 
