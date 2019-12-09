# === Imports ======================================================================================
# Standard Library
from tkinter import Tk

# Local Library

# === Classes ======================================================================================
class MediaArchivistGUI(Tk):
    def __init__(self, screenName=None, baseName=None, className='Tix'):
        super().__init__(screenName, baseName, className)

        self.title('Media Archivist')

