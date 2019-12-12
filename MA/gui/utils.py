# === Imports ======================================================================================
from typing import Union

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
