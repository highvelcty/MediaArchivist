# === Imports ======================================================================================
# Standard library
import os
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

        self.columnconfigure(0, weight=1)
        self._nav_entry.grid(row=0, column=0, sticky=tk.EW)


class NavEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.bind('<Tab>', self._on_tab)
        self.bind('<Return>', self._on_enter)
        self.bind('<KP_Enter>', self._on_enter)

        # ..todo:: Where the default focus is set on application start needs to be more dynamic
        self.focus_set()

    def _on_enter(self, event):
        print('on enter')

    def _on_tab(self, event):
        # current_input = self._string_var.get()
        current_input = self.get()

        print('on tab %s' % current_input)

        # Stop event propagation.
        return 'break'

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
        super().__init__(master, cnf, background='blue', **kw)

        self._nav_bar = NavBar(self)
        self._listing = Listing(self)

        self.columnconfigure(0, weight=1)
        self._nav_bar.grid(row=0, column=0, sticky=tk.EW)




