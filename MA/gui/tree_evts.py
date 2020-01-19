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
    def __init__(self):
        super().__init__()

        self._callbacks = dict(zip(TreeEvt, ([],) * len(TreeEvt)))

    def register(self, tree_evt: TreeEvt, callback: Callable):
        self._callbacks[tree_evt].append(callback)

    def broadcast(self, tree_event: TreeEvt, *args, **kwargs):
        for callback in self._callbacks:
            callback(*args, **kwargs)
