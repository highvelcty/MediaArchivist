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
CFG_DIR_AND_FILE_PERMISSIONS = 0o700
CONFIG_HIDDEN_FOLDER = '.config'
ENV_XDG_CONFIG_HOME = 'XDG_CONFIG_HOME'
GUI_CFG_FILENME = 'guicfg.cfg'
HOME_SHORTCHUT = '~'
MEDIA_ARCHIVIST_CFG_DIR = 'mediaarchivist'
MIN_HEIGHT_IN_PIXELS = 600
MIN_WIDTH_IN_PIXELS = 800

# === Enumerations =================================================================================
class CfgSection(object):
    ROOT_WINDOW = 'ROOT_WINDOW'

class RootWindowKey(object):
    GEOMETRY = 'GEOMETRY'
    ZOOMED = 'ZOOMED'

DEFAULT_CFG = {
    CfgSection.ROOT_WINDOW: {
        RootWindowKey.GEOMETRY: '%sx%s+%d+%d' % (MIN_WIDTH_IN_PIXELS, MIN_HEIGHT_IN_PIXELS, 0, 0),
        RootWindowKey.ZOOMED: False,
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
            print('Warning: Failed to read GUI configuration file at:\n%s' % self._path_to_file)
            print('Here is the traceback:')
            import traceback
            traceback.print_exc()

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
            print('Here is the traceback:')
            import traceback
            traceback.print_exc()
            
class CfgFile(object):
    def __init__(self, file_path):
        self._file_path = file_path
    def __enter__(self):
        self._fd = os.open(self._file_path, os.O_WRONLY | os.O_CREAT, CFG_DIR_AND_FILE_PERMISSIONS)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.close(self._fd)

    def write(self, data):
        os.write(self._fd, data.encode())