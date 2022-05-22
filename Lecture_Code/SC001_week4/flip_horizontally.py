"""
File: flip_horizontally.py
Name: Shane Liu
-------------------------
This program shows how to create an empty SimpleImage
as well as making a mirrored image of poppy.png
by replacing pixels on blank new canvas by ones on poppy.png
"""

from simpleimage import SimpleImage


def main():
    img = SimpleImage("images/poppy.png")
    img.show()
    b_img = SimpleImage.blank(img.width*2, img.height)

    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x, y)

            # left side
            b_img_pixel = b_img.get_pixel(x, y)
            b_img_pixel.red = img_pixel.red
            b_img_pixel.green = img_pixel.green
            b_img_pixel.blue = img_pixel.blue

            # right side
            b_img_pixel2 = b_img.get_pixel(b_img.width-1-x, y)
            b_img_pixel2.red = img_pixel.red
            b_img_pixel2.green = img_pixel.green
            b_img_pixel2.blue = img_pixel.blue
            
    b_img.show()


if __name__ == '__main__':
    main()
