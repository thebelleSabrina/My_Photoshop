"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename:str, the file path of the original image
    :return:The updated mirrored image by inserting old pixels into the blank new canvas
    """
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width, img.height*2)
    for x in range(b_img.width):
        for y in range(img.height):
            # get the colored pixel in the original image
            pixel = img.get_pixel(x, y)
            # get the blank pixel
            b_img_pixel1 = b_img.get_pixel(x, y)
            b_img_pixel2 = b_img.get_pixel(x, b_img.height-y-1)
            # color the blank pixel
            b_img_pixel1.red = pixel.red
            b_img_pixel1.green = pixel.green
            b_img_pixel1.blue = pixel.blue

            b_img_pixel2.red = pixel.red
            b_img_pixel2.green = pixel.green
            b_img_pixel2.blue = pixel.blue
    return b_img


def main():
    """
    This program shows how to create an empty SimpleImage as well as making a mirrored image
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
