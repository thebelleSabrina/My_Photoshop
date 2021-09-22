"""
File: fire.py
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename:str, the file path of the original image
    :return:The updated image with all pixels are recognized as fire and highlights them
    """
    fire_img = SimpleImage(filename)
    for pixel in fire_img:  # check all pixel in the original image
        avg = (pixel.red+pixel.green+pixel.blue)//3  # calculate the average of the value of RGB in the image
        if pixel.red > (avg * HURDLE_FACTOR):  # if the red value of a pixel higher than average,highlight the pixel
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:  # if not, turning those pixel into gray
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return fire_img


def main():
    """
    This program detects the pixels that are recognized as fire and highlights them for better observation.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
