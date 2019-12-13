# === Imports ======================================================================================
from typing import Union, Tuple

# === Functions ====================================================================================

def build_tk_geometry_str(width_in_pixels: Union[int, str], height_in_pixels: Union[int, str],
                          posx_in_pixels: Union[int, str], posy_in_pixels: Union[int, str]) -> str:
    """
    Return a string suitable for passing to tk's geometry method.

    :param width_in_pixels: The width geometry property in units of pixels of type integer or
                            string.
    :param height_in_pixels: The height geometry property in units of pixels of type integer or
                             string.
    :param posx_in_pixels:  The x position geometry property in units of pixels of type integer or
                            string.
    :param posy_in_pixels:  The y position geometry property in units of pixels of type integer or
                            string.

    :return: A string suitable for use with tk's geometry method taking the form of
             <height_in_pixels>x<width_in_pixels>+posx_in_pixels+posy_in_pixels
    """
    return '%sx%s+%s+%s' % (width_in_pixels, height_in_pixels, posx_in_pixels, posy_in_pixels)

def split_tk_geometry_str(geom_str: str) -> Tuple[int, int, int, int]:
    """
    Convert a tk geometry string into a tuple of integers.

    :param geom_str: Must take the form of "<width_in_pixels>x<height_in_pixels>+<pos_x>+<pos_y>"

                     where

                        <width_in_pixels> is a decimal string
                        <height_in_pixels> is a decimal string
                        <pos_x> is a decimal string
                        <pos_y> is a decimal string

    :return: Four item tuple consisting of the width in pixels, the height in pixels, the x position
             in pixels and the y position in pixels. All items are integers.
    """
    geom_str = geom_str.lower().strip()
    shape, posx, posy = geom_str.split('+')
    width, height = shape.split('x')

    return int(width), int(height), int(posx), int(posy)



