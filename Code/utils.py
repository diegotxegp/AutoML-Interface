##### UTILS.py

import tkinter as tk

def enable_next_tab(notebook):
    """
    Enable the next shadowed tab
    """
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

def split_frame(frame):
    """
    Split a frame into two sides.
    """
    # Left frame
    left_frame = tk.Frame(frame)
    left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    #Right frame
    right_frame = tk.Frame(frame)
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Divider line
    divider = tk.Frame(frame, bg="grey", width=2)
    divider.place(relx=0.5, rely=0, relheight=1)

    return left_frame, right_frame