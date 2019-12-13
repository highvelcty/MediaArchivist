# === Imports ======================================================================================
# Standard Library
import tkinter as tk

# Local Library
from . import utils
from .cfg import gui_cfg, CfgSection, RootWindowKey, MIN_HEIGHT_IN_PIXELS, MIN_WIDTH_IN_PIXELS
from .dirview import DirView

# === Classes ======================================================================================
class MediaArchivistGUI(tk.Tk):
    """
    .. note:: The save/restore x,y position is off by a handful of pixels in both directions
              following a repositioning. It seems like reported geometry is off with repositioning.

    """
    def __init__(self):
        super().__init__()

        # --- Configuration ---
        self.title('Media Archivist')
        self.minsize(MIN_WIDTH_IN_PIXELS, MIN_HEIGHT_IN_PIXELS)

        # prevent internal widgets from resizing this root window.
        self.grid_propagate(False)
        self.pack_propagate(False)

        # avoid flicker
        self.withdraw()

        # --- Widgets ---:
        self._dir_view = DirView(self)

        # --- Layout ---
        self._dir_view.grid(row=0, column=0, sticky=tk.NSEW)

        # --- Finalize ---
        self._set_initial_geometry()
        self.deiconify()

    def _save_geometry(self):
        # Grab the window position and geometry state
        width_pixels, height_pixels, posx_pixels, posy_pixels = \
            utils.split_tk_geometry_str(self.geometry())

        zoomed = bool(self.wm_attributes('-zoomed'))
        if zoomed:
            # This is the geometry that is set if/when the window is moved out of "zoomed" mode.
            width_pixels = MIN_WIDTH_IN_PIXELS
            height_pixels = MIN_HEIGHT_IN_PIXELS

        geometry = utils.build_tk_geometry_str(width_pixels, height_pixels,
                                               posx_pixels, posy_pixels)
        gui_cfg[CfgSection.ROOT_WINDOW][RootWindowKey.GEOMETRY] = geometry
        gui_cfg[CfgSection.ROOT_WINDOW][RootWindowKey.ZOOMED] = str(zoomed)

    def _set_initial_geometry(self):
        self.geometry(gui_cfg[CfgSection.ROOT_WINDOW][RootWindowKey.GEOMETRY])
        zoomed = gui_cfg[CfgSection.ROOT_WINDOW].getboolean(RootWindowKey.ZOOMED)
        self.wm_attributes('-zoomed', zoomed)

    def destroy(self):
        """
        This is an override. This is called on root window destruction.
        """
        self._save_geometry()
        super().destroy()
