"""
File: green_screen.py
Name: Shane Liu
-------------------------
This file creates a new image that uses MillenniumFalcon.png as background 
and replace the green pixels in "ReyGreenScreen.png".
The green pixels are defined as the G value greater than max among R and B
"""

from simpleimage import SimpleImage


def main():
    """
    The program defines the green pixels as the G value greater than
    the maximum among R and B value times two.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    space_ship.make_as_big_as(figure)
    result = combine(space_ship, figure)
    result.show()


def combine(background_img, figure_img):
    """
    :param background_img: img, the background image
    :param figure_img: img, green screen figure image
    :return: img, the green screen pixels are replaced by pixels of background image
    """
    for x in range(background_img.width):
        for y in range(background_img.height):
            pixel = figure_img.get_pixel(x, y)
            bigger = max(pixel.red, pixel.blue)

            if pixel.green > 2*bigger:
                background_pixel = background_img.get_pixel(x, y)
                pixel.red = background_pixel.red
                pixel.blue = background_pixel.blue
                pixel.green = background_pixel.green
    return figure_img


if __name__ == '__main__':
    main()
