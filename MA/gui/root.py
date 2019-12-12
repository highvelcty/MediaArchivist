# === Imports ======================================================================================
# Standard Library
import tkinter as tk

# Local Library
from . import utils
from .cfg import gui_cfg, CfgSection, RootGeometrySectKey
from .dirview import DirView

# === Constants ====================================================================================
DEFAULT_ROOT_GEOMETRY = '800x600'
DEFAULT_ROOT_POSITION = '0+0'

# === Classes ======================================================================================
class MediaArchivistGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Media Archivist')

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

        self.geometry(cfg_geometry)
        self.wm_attributes('-zoomed', cfg_zoomed)

        # --- Widgets ---
        self._dir_view = DirView(self)

        # --- Layout ---
        self._dir_view.grid(row=0, column=0, sticky=tk.NSEW)

    def destroy(self):
        print(self.geometry())

        super().destroy()