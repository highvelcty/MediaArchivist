# === Imports ======================================================================================
# Standard library
import unittest

# Local library
from .tree_evts import TreeEvt, TreeEvts

# === GUI Trees ====================================================================================
class TheRoot(object):
    pass

class TheRoot2(object):
    pass

# === Classes ======================================================================================
class TestRootTreeEvts(unittest.TestCase):
    def test_the_root(self):
        tree_evts_1  = TreeEvts(self)
        tree_evts_2 = TreeEvts(self)

        self.assertNotEqual(tree_evts_1, tree_evts_2)
        self.assertEqual(len(tree_evts_1._callbacks), len(TreeEvt))
        # Make sure the callbacks are initialized for each event.
        self.assertEqual(list(tree_evts_1._callbacks.keys()).sort(), list(TreeEvt).sort())
