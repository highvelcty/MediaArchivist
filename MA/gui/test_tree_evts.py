# === Imports ======================================================================================
# Standard library
import unittest

# Local library
from .tree_evts import TreeEvt, TreeEvts

# === GUI Tree =====================================================================================
class TheRoot(object):
    pass

# === Globals ======================================================================================
tree_evts  = TreeEvts(TheRoot)

# === Classes ======================================================================================
class TestTreeEvts(unittest.TestCase):
    def test_the_root(self):
        pass
