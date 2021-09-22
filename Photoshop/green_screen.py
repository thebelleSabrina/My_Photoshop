"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: MillenniumFalcon.png
    :param figure_img: ReyGreenScreen.png
    :return: a new image that uses MillenniumFalcon.png as background and replace the green pixels in ReyGreenScreen.png
    """
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            pixel = figure_img.get_pixel(x, y)  # gets every pixel's location in ReyGreenScreen.png
            pixel_n = background_img.get_pixel(x, y)  # gets every pixel's location in MillenniumFalcon.png
            bigger = max(pixel.red, pixel.blue)   # returns the one that is bigger
            if pixel.green > int(bigger*2):  # replaces the green pixels into pixel in MillenniumFalcon.png
                pixel.red = pixel_n.red
                pixel.green = pixel_n.green
                pixel.blue = pixel_n.blue
    return figure_img


def main():
    """
    This programs creates a new image that combines MillenniumFalcon.png as background and figure in ReyGreenScreen.png.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
