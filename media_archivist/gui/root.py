# === Imports ======================================================================================
# Standard Library
import tkinter as tk

# Local Library
from . import utils
from .dirview import  DirView

# === Constants ====================================================================================
DEFAULT_ROOT_GEOMETRY = '800x600'
DEFAULT_ROOT_POSITION = '0+0'

# === Classes ======================================================================================
class MediaArchivistGUI(tk.Tk):
    def __init__(self, screenName=None, baseName=None, className='Tix'):
        super().__init__(screenName, baseName, className)

        self.title('Media Archivist')
        self.geometry(utils.concate_geom_and_pos(DEFAULT_ROOT_GEOMETRY, DEFAULT_ROOT_POSITION))

        self._dir_view = DirView(self)

        self._dir_view.grid(row=0, column=0, sticky=tk.NSEW)