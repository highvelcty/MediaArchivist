# === Imports ======================================================================================
# Standard library
from enum import Enum
import os
import time
import tkinter as tk
from tkinter import ttk
from typing import Iterable

# Local library
from .tree_evts import TreeEvt, TreeEvts
from .utils import ascii_bell

# === Enumerations =================================================================================
class Event(TreeEvt):
    LIST_CANDIDATE_DIRS                         = 0x00000001

# === Classes ======================================================================================
class NavBar(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self._nav_entry = NavEntry(self)
        self._nav_filter = NavFilter(self)
        self._nav_options = NavOptions(self)
        self._close_button = tk.Button(self, text='x')

        self.columnconfigure(0, weight=1)
        self._nav_entry.grid(row=0, column=0, sticky=tk.EW)

class NavEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.bind('<Tab>', self._on_tab)
        self.bind('<Return>', self._on_enter_pressed)
        self.bind('<KP_Enter>', self._on_enter_pressed)
        self.bind('<Control-u>', self._clear_cursor_to_prompt)
        self.bind('<Control-U>', self._clear_cursor_to_prompt)

        self._first_notification = False

        # ..todo:: Set the default focus properly on application start.
        self.focus_set()

    def _clear_cursor_to_prompt(self, event):
        self.delete(0, tk.INSERT)

    def _notify_operator(self):
        ascii_bell()
        current_input = self.get()
        self.delete(0, tk.END)
        self.update_idletasks()
        time.sleep(.05)
        self.insert(0, current_input)
        self._first_notification = True

    def _on_enter_pressed(self, event):
        print('on enter')

    def _on_tab(self, event):
        current_input = self.get()

        head, tail = os.path.split(current_input)

        if os.path.isdir(head):
            root, dirs, files = next(os.walk(head))

            candidate_dirs = []
            for dir in dirs:
                if dir.startswith(tail):
                    candidate_dirs.append(dir)

            if len(candidate_dirs) == 1:
                self.delete(0, tk.END)
                self.insert(0, os.path.join(root, candidate_dirs[0]))
            else:
                if not self._first_notification:
                    self._notify_operator()
                else:
                    print('list dir')

        # Stop event propagation.
        return 'break'

    def _reset_notification(self):
        self._first_notification = False

class NavFilter(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

class NavOptions(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

class Listing(ttk.Treeview):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)

class AvailableDirOutput(tk.Text):
    _MAX_DIR_LIST_SPACES = 24
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, wrap=tk.WORD, **kw)

    def list_dirs(self, dirs: Iterable[str]):
        self.delete(0.0, tk.END)

        spaces = max((len(dir) for dir in dirs))
        spaces = min(spaces, self._MAX_DIR_LIST_SPACES)
        spaces = ' ' * spaces

        for dir in dirs:
            self.insert(tk.END, '%s%s' % (dir, spaces))

        self.see(tk.END)

class DirView(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self._tree_evts = TreeEvts(self)

        self._nav_bar = NavBar(self)
        self._listing = Listing(self)
        self._avail_dir_output = AvailableDirOutput(self)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self._avail_dir_output.grid(row=0, column=0, sticky=tk.NSEW)
        self._nav_bar.grid(row=1, column=0, sticky=tk.EW)

