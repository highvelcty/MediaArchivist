# === Imports ======================================================================================
# Standard library
import tkinter as tk
from enum import Enum
from typing import Callable

# === Enumerations =================================================================================
class TreeEvt(Enum):
    pass

# === Classes ======================================================================================
class TreeEvts(object):
    """
    This is a way to propagate events throughout a tkinter GUI tree. The root of the tree or a root
    node of the tree instantiates this object, passing itself as an argument to the "the_root"
    parameter. All other sub-widgets in the GUI tree instantiate this object using the default
    argument to "the_root" parameter.

    Non-root instances will traverse up the GUI tree to locate the root. This is how coordination
    is achieved throughout the GUI tree. The root instance is the ledger for the entire tree and
    the sub-instances communicate up through the tree to the root instance.
    """
    def __init__(self, the_root: object = None):
        super().__init__()

        self._the_root = the_root

        if self._the_root is None:
            self._callbacks = self._get_the_root()._callbacks
        else:
            self._callbacks = dict(zip(TreeEvt, ([],) * len(TreeEvt)))

    def register(self, tree_evt: TreeEvt, callback: Callable):
        self._callbacks[tree_evt].append(callback)

    def broadcast(self, tree_event: TreeEvt, *args, **kwargs):
        for callback in self._callbacks:
            callback(*args, **kwargs)
