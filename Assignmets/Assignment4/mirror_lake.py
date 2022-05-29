"""
File: mirror_lake.py
Name: Shane Liu
-------------------------
This file reads in mt-rainier.jpg and makes a new image
that creates a mirror lake vibe,
by placing an inverse image of mt-rainier.jpg below the original one.
"""

from simpleimage import SimpleImage


def main():
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


def reflect(filename):
    """
    :param filename: str, the input image's path
    :return: img, a mirror lake vibe image
    """
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width, img.height*2)
    for x in range(img.width):
        for y in range(img.height):
            img_pix = img.get_pixel(x, y)
            
            # upper
            b_img_pix = b_img.get_pixel(x, y)
            b_img_pix.red = img_pix.red
            b_img_pix.green = img_pix.green
            b_img_pix.blue = img_pix.blue
            
            # lower
            b_img_pix2 = b_img.get_pixel(x, b_img.height-1-y)
            b_img_pix2.red = img_pix.red
            b_img_pix2.green = img_pix.green
            b_img_pix2.blue = img_pix.blue
    return b_img


if __name__ == '__main__':
    main()
