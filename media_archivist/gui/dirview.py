# === Imports ======================================================================================
# Standard library
import tkinter as tk
from tkinter import ttk

# Local library

# === Classes ======================================================================================
class NavBar(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self._nav_entry = NavEntry(self)
        self._nav_filter = NavFilter(self)
        self._nav_options = NavOptions(self)
        self._close_button = tk.Button(self, text = 'x')

class NavEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

class NavFilter(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

class NavOptions(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

class Listing(ttk.Treeview):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)

class DirView(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self._nav_bar = NavBar(self)
        self._listing = Listing(self)


