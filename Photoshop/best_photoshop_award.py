"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


def combine(fig, bg):
    """
    :param fig: figure image of 'Gozilla vs King Kong'
    :param bg: background image of angry mama
    :return: a new image that uses angry mama as background and Gozilla vs King Kong as figure
    """
    for x in range(fig.width):  # gets every pixel in figure image
        for y in range(fig.height):
            pixel = fig.get_pixel(x,y)
            avg = (pixel.red+pixel.green+pixel.blue)//3
            # total = pixel.red+pixel.green+pixel.blue
            if avg > 159.9:  # replaces gray pixel
                bg_pixel = bg.get_pixel(x,y)
                pixel.red = bg_pixel.red
                pixel.green = bg_pixel.green
                pixel.blue = bg_pixel.blue
    return fig


def main():
    """
    the program creates a new image that uses angry mama as background and Gozilla vs King Kong as figure
    """
    bg = SimpleImage('image_contest/422*236.jpeg')  # 422*236
    fig = SimpleImage('image_contest/Q.jpg')  # 1050*536
    fig.make_as_big_as(bg)  # makes two images have the same size
    new_img = combine(fig, bg)
    new_img.show()


if __name__ == '__main__':
    main()
