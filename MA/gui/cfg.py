"""
This module is the GUI configuration file interface.
"""
# === Imports ======================================================================================
# Standard Library
import configparser
import os

# Local Library

# === Constants ====================================================================================
CONFIG_HIDDEN_FOLDER = '.config'
HOME_SHORTCHUT = '~'
ENV_XDG_CONFIG_HOME = 'XDG_CONFIG_HOME'
MEDIA_ARCHIVIST_CFG_DIR = '.mediaarchivist'
GUI_CFG_FILENME = 'guicfg.cfg'
CFG_DIR_AND_FILE_PERMISSIONS = 0o700

# === Functions ====================================================================================
def get_cfg_dir() -> str:
    try:
        path_to_cfg_dir = os.environ[ENV_XDG_CONFIG_HOME]
    except KeyError:
        path_to_cfg_dir = os.path.join(os.path.expanduser(HOME_SHORTCHUT), CONFIG_HIDDEN_FOLDER)
    return path_to_cfg_dir

# === Classes ======================================================================================
class GUIConfig(configparser.ConfigParser):
    def __init__(self):
        super().__init__()

        # Initialize the configuration directory structure if needed.
        self._path_to_dir = os.path.join(os.path.join(get_cfg_dir(), MEDIA_ARCHIVIST_CFG_DIR))
        if not os.path.isdir(self._path_to_dir):
            os.makedirs(self._path_to_dir, CFG_DIR_AND_FILE_PERMISSIONS)

        self._path_to_file = os.path.join(self._path_to_dir, GUI_CFG_FILENME)

        try:
            self.read(self._path_to_file)
        # Nice! A base exception for the package.
        except configparser.Error:
            self._generate_defaults()

    def _generate_defaults(self):
        pass






