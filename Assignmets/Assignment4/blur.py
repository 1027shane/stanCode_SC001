"""
File: blur.py
Name: Shane Liu
-------------------------
This file shows the original image(smiley-face.png) first, 
and then its blurred image. 
The blur algorithm uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def main():
    """
    The program uses the average RGB values of a pixel's nearest neighbors,
    to make the input image blur.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(3):
        blurred_img = blur(blurred_img)
    blurred_img.show()


def blur(img):
    """
    :param img: img, the original image
    :return: img, the blurred image
    """
    blurred_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            sum_red = sum_blue = sum_green = 0
            # counter: to count the neighbor of refilled pixel
            counter = 0
            # blurred filter
            for i in range(-1, 2):
                for j in range(-1, 2):
                    new_x = x+i
                    new_y = y+j
                    
                    if 0 <= new_x < img.width and 0 <= new_y < img.height:
                        new_pixel = img.get_pixel(new_x, new_y)
                        sum_red += new_pixel.red
                        sum_green += new_pixel.green
                        sum_blue += new_pixel.blue
                        counter += 1
                    
            blurred_pixel = blurred_img.get_pixel(x, y)
            blurred_pixel.red = sum_red//counter
            blurred_pixel.blue = sum_blue//counter
            blurred_pixel.green = sum_green//counter
    return blurred_img


if __name__ == '__main__':
    main()
