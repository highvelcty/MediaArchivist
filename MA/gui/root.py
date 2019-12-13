# === Imports ======================================================================================
# Standard Library
import tkinter as tk

# Local Library
from . import utils
from .cfg import gui_cfg, CfgSection, RootGeometrySectKey, MIN_HEIGHT_IN_PIXELS, MIN_WIDTH_IN_PIXELS
from .dirview import DirView

# === Classes ======================================================================================
class MediaArchivistGUI(tk.Tk):
    """
    .. note:: The save/restore x,y position is off by a handful of pixels in both directions
              following a repositioning. It seems like reported geometry is off with repositioning.

    """
    def __init__(self):
        super().__init__()

        self.title('Media Archivist')
        self.minsize(MIN_WIDTH_IN_PIXELS, MIN_HEIGHT_IN_PIXELS)

        cfg_zoomed = gui_cfg[CfgSection.ROOT_GEOMETRY].getboolean(RootGeometrySectKey.ZOOMED)

        cfg_geometry = \
            utils.build_tk_geometry_str(gui_cfg[CfgSection.ROOT_GEOMETRY]
                                        [RootGeometrySectKey.WIDTH_PIXELS],
                                        gui_cfg[CfgSection.ROOT_GEOMETRY]
                                        [RootGeometrySectKey.HEIGHT_PIXELS],
                                        gui_cfg[CfgSection.ROOT_GEOMETRY]
                                        [RootGeometrySectKey.POSX_PIXELS],
                                        gui_cfg[CfgSection.ROOT_GEOMETRY]
                                        [RootGeometrySectKey.POSY_PIXELS])

        self.grid_propagate(False)
        self.pack_propagate(False)
        # avoid flicker
        self.withdraw()

        # --- Widgets ---
        self._dir_view = DirView(self)

        # --- Layout ---
        self._dir_view.grid(row=0, column=0, sticky=tk.NSEW)

        self.geometry(cfg_geometry)
        self.wm_attributes('-zoomed', cfg_zoomed)
        self.deiconify()

    def destroy(self):
        """
        This is an override. This is called on root window destruction.
        :return:
        """
        # Grab the window position and geometry state
        width_pixels, height_pixels, posx_pixels, posy_pixels = \
            utils.split_tk_geometry_str(self.geometry())

        zoomed = bool(self.wm_attributes('-zoomed'))

        if zoomed:
            # This is the geometry that is set if/when the window is moved out of "zoomed" mode.
            width_pixels = MIN_WIDTH_IN_PIXELS
            height_pixels = MIN_HEIGHT_IN_PIXELS

        # Save the geometry attributes to the GUI configuration.
        gui_cfg[CfgSection.ROOT_GEOMETRY][RootGeometrySectKey.WIDTH_PIXELS] = str(width_pixels)
        gui_cfg[CfgSection.ROOT_GEOMETRY][RootGeometrySectKey.HEIGHT_PIXELS] = str(height_pixels)
        gui_cfg[CfgSection.ROOT_GEOMETRY][RootGeometrySectKey.POSX_PIXELS] = str(posx_pixels)
        gui_cfg[CfgSection.ROOT_GEOMETRY][RootGeometrySectKey.POSY_PIXELS] = str(posy_pixels)
        gui_cfg[CfgSection.ROOT_GEOMETRY][RootGeometrySectKey.ZOOMED] = str(zoomed)

        super().destroy()