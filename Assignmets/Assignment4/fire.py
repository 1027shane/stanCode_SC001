"""
File: fire.py
Name: Shane Liu
-------------------------
This file contains a method called highlight_fires,
 which detects the pixels that are recognized as fire
and highlights them for better observation.
"""

from simpleimage import SimpleImage

HURDLE_FACTOR = 1.05


def main():
    """
    The program uses the average of RGB multipled by HURDLE_FACTOR,
    to find the area with higher R value and mark it out.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


def highlight_fires(filename):
    """
    :param filename: str,the input image's path
    :return: img, with highlighted fire
    """
    img = SimpleImage(filename)
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x, y)
            avg = (pixel.red+pixel.green+pixel.blue)//3
            
            # fired
            if pixel.red > HURDLE_FACTOR*avg:
                pixel.red = 255
                pixel.green = 0
                pixel.blue = 0
                
            # unfired
            else:
                pixel.red = avg
                pixel.green = avg
                pixel.blue = avg
    return img


if __name__ == '__main__':
    main()
