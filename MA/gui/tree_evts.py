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
    def __init__(self, toplevel_type):
        self._toplevel_type = toplevel_type
        self._toplevels = {}

    def _get_toplevel(self, widget: tk.Widget):
        if type(widget) is self._toplevel_type:
            return widget
        elif not hasattr(widget, 'master'):
            raise Exception('Widget %s does not have a parent' % widget)
        else:
            return self._get_toplevel(widget.master)

    def register(self, widget: tk.Widget, tree_event: TreeEvt, callback: Callable):
        toplevel = self._get_toplevel(widget)
        if toplevel not in self._toplevels:
            self._toplevels[toplevel] = {}

        callbacks = self._toplevels[toplevel]

        if tree_event not in callbacks:
            callbacks[tree_event] = []

        if callback not in callbacks[tree_event]:
            callbacks[tree_event].append(callback)

    def broadcast(self, widget: tk.Widget, tree_event: TreeEvt, *args, **kwargs):
        for callback in self._toplevels[self._get_toplevel(widget)][tree_event]:
            callback(*args, **kwargs)
