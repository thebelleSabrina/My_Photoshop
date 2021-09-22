"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, the file path of the original image
    :return img: SimpleImage,a new image half the width and height of the original.
    """
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width // 2, img.height // 2)  # create a blank canvas half the size of the original
    for x in range(b_img.width):  # select pixel based on the blank canvas pixel's location
        for y in range(b_img.height):
            pixel = b_img.get_pixel(x, y)
            img_p0 = img.get_pixel(2*x, 2*y)  # 2 is the number of shrink
            img_p1 = img.get_pixel(2*x+1, 2*y)
            img_p2 = img.get_pixel(2*x, 2*y+1)
            img_p3 = img.get_pixel(2*x+1, 2*y+1)
            pixel.red = (img_p0.red + img_p1.red + img_p2.red + img_p3.red) // 4  # get the shrink image's pixel
            pixel.green = (img_p0.green + img_p1.green + img_p2.green + img_p3.green) // 4
            pixel.blue = (img_p0.blue + img_p1.blue + img_p2.blue + img_p3.blue) // 4
    return b_img


def main():
    """
    The program creates a new image half the width and height of the original.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
