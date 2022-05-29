"""
File: shrink.py
Name: Shane Liu
-------------------------
Create a new out image half the width and height of the original.
Set pixels at x=0 1 2 3 in out, from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def main():
    """
    The program uses the average of RGB in each pixel's neighbor(right/down) side.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


def shrink(filename):
    """
    :param filename: str, the input image's path
    :return: img, half the width and height of the original image
    """
    img = SimpleImage(filename)
    shrink_img = SimpleImage.blank(img.width//2, img.height//2)
    for x in range(0, img.width-1, 2):
        for y in range(0, img.height-1, 2):
            sum_red = sum_green = sum_blue = 0
            
            # algorithm
            for i in range(x, x+2):
                for j in range(y, y+2):
                    pixel = img.get_pixel(i, j)                    
                    sum_red += pixel.red
                    sum_green += pixel.green
                    sum_blue += pixel.blue

            shrink_pixel = shrink_img.get_pixel(x//2, y//2)        
            shrink_pixel.red = sum_red//4
            shrink_pixel.blue = sum_blue//4
            shrink_pixel.green = sum_green//4
    return shrink_img


if __name__ == '__main__':
    main()
