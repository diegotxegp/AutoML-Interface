# UTILS

import tkinter as tk
from tkinter import PanedWindow

# Enables the next shadowed tab
def enable_next_tab(notebook) -> bool:
    current_tab = notebook.index('current')
    total_tabs = len(notebook.tabs())
    
    # There is more tabs: True
    if current_tab < total_tabs - 1:
        next_tab = current_tab + 1
        notebook.tab(next_tab, state="normal")
        notebook.select(next_tab)

    # If there are not more tabs, False
    else:
        return False

# Creates a two-side window
def paned_window(frame):
        paned_window = PanedWindow(frame, orient=tk.HORIZONTAL, sashrelief=tk.RAISED, sashwidth=5)
        paned_window.pack(fill=tk.BOTH, expand=True)

        left_frame = tk.Frame(paned_window)
        right_frame = tk.Frame(paned_window)

        paned_window.add(left_frame)
        paned_window.add(right_frame)

        return left_frame, right_frame