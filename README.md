# picamera
PiCamera Basic and Advanced Recipes adapted from "official" documentation for training purposes. The purpose of this document to record my experience in following the documentation prepared by Dave Jones.

## Basic Recipes

1. Capturing to a file

This example is a basic use of the `capture` method in the PiCamera classs. The `capture` method has the following parameters:

- output: the value can a string (i.e. filename) or an object that has a `write` method; if this parameter is omitted then the image data is written to a buffer where overflow constraints are the responsibility of the client code.

- format: the value can a string or a MIME-type; if this parameter is omitted then the format is deduced from the filetype extension otherwise an exception, `PiCameraValueError` is raised. The supported formats are JPEG, PNG, GIF, BMP, YUV, RGB, RGBA, BGR, BGRA and RAW.

- use_video_port: the value is boolean and defaults to `False` whereby the higher quality image port is used.

- resize: a two element tuple specifying the width and height of the image if the default value None needs to be overriden

- splitter_port: see PiCamera documentation if you really need to use this parameter

- bayer: if the value is `True` then the Exif metadata receives the raw bayer data from the camera's sensor

- options: if the format is "jpeg" then the addtional parameters are:

- quality: an integer from 1 to 100 representing the quality of the image; the default value is 85.

- restart: the restart intervval for the encoder.

- thumbnail: the size and quality of the thumbnail image as a tuple `(width, height, quality)` with the default being `(64,48,35)`; if the value is `None` then no thumbnail is prepared.

2. Capturing to a stream

3. Capturing to a PIL Image

4. Capturing resized images

5. Capturing consistent images

6. Capturing time-lapse sequences

7. Capturing in low light

8. Capturing to a network stream

9. Recording video to a file

10. Recording video to a stream

11. Recording over multiple files

12. Recording to a circular stream

13. Recording to a network stream

14. Overlaying images on the preview

15. Overlaying text on the output

16. Controlling the LED

## Advanced Recipes

1. Capturing to a numpy array

2. Capturing to an OpenCV object

3. Unencoded image capture in YUV format

4. Unencoded image capture in RGB format

5. Custom outputs

6. Unconventional file outputs

7. Rapid capture and processing

8. Unencoded video capture

9. Rapid capture and streaming

10. Web streaming

11. Capturing images whilst recording

12. Recording at multiple resolutions

13. Recording motion vector data

14. Splitting to/from a circular stream

15. Custom encoders

16. Raw Bayer data captures

17. Using a flash with the camera

# Conclusions

# References
- PiCamera release 1.13, Dave Jones https://picamera.readthedocs.io/en/release-1.13/index.html
