"""
This module is the GUI configuration file interface.
"""
# === Imports ======================================================================================
# Standard Library
import atexit
import configparser
import os

# Local Library

# === Globals ======================================================================================
gui_cfg = None

# === Constants ====================================================================================
CONFIG_HIDDEN_FOLDER = '.config'
HOME_SHORTCHUT = '~'
ENV_XDG_CONFIG_HOME = 'XDG_CONFIG_HOME'
MEDIA_ARCHIVIST_CFG_DIR = 'mediaarchivist'
GUI_CFG_FILENME = 'guicfg.cfg'
CFG_DIR_AND_FILE_PERMISSIONS = 0o700

# === Enumerations =================================================================================
class CfgSection(object):
    ROOT_GEOMETRY = 'ROOT_GEOMETRY'

class RootGeometrySectKey(object):
    HEIGHT_PIXELS = 'HEIGHT_PIXELS'
    WIDTH_PIXELS = 'WIDTH_PIXELS'
    POSX_PIXELS = 'POSX_PIXELS'
    POSY_PIXELS = 'POSY_PIXELS'
    ZOOMED = 'ZOOMED'

DEFAULT_CFG = {
    CfgSection.ROOT_GEOMETRY: {
        RootGeometrySectKey.HEIGHT_PIXELS: 600,
        RootGeometrySectKey.WIDTH_PIXELS: 800,
        RootGeometrySectKey.POSX_PIXELS: 0,
        RootGeometrySectKey.POSY_PIXELS: 0,
        RootGeometrySectKey.ZOOMED: False,
    }
}

# === Functions ====================================================================================
def get_cfg_dir() -> str:
    try:
        path_to_cfg_dir = os.environ[ENV_XDG_CONFIG_HOME]
    except KeyError:
        path_to_cfg_dir = os.path.join(os.path.expanduser(HOME_SHORTCHUT), CONFIG_HIDDEN_FOLDER)
    return path_to_cfg_dir

def make_gui_cfg():
    global gui_cfg
    gui_cfg = GUIConfig()

# === Classes ======================================================================================
class GUIConfig(configparser.ConfigParser):
    def __init__(self):
        super().__init__()

        # Initialize the configuration directory structure if needed.
        self._path_to_dir = os.path.join(os.path.join(get_cfg_dir(), MEDIA_ARCHIVIST_CFG_DIR))
        if not os.path.isdir(self._path_to_dir):
            os.makedirs(self._path_to_dir, CFG_DIR_AND_FILE_PERMISSIONS)

        self._path_to_file = os.path.join(self._path_to_dir, GUI_CFG_FILENME)

        # Read the default dictionary first. The defaults will/may be masked by data read from file
        # next
        self.read_dict(DEFAULT_CFG)

        try:
            self.read(self._path_to_file)
        # The base exception for the configparser package.
        except configparser.Error:
            pass

        atexit.register(self._destroy)

    def _destroy(self):
        print('writing to: %s' % self._path_to_file)
        """
        This method is called on python exit.
        """
        try:
            with CfgFile(self._path_to_file) as cfgfile:
                self.write(cfgfile)
        except:
            print('Warning: Failed to write the GUI configuration file to:\n%s' %
                  self._path_to_file)
            print('Here is the traceback when attempting to write the file:')
            import traceback
            traceback.print_exc()
            
class CfgFile(object):
    def __init__(self, file_path):
        self._file_path = file_path
    def __enter__(self):
        self._fd = os.open(self._file_path, os.O_WRONLY | os.O_CREAT, CFG_DIR_AND_FILE_PERMISSIONS)
        return self

    def write(self, data):
        os.write(self._fd, data.encode())

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.close(self._fd)

