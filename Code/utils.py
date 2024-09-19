##### UTILS.py

import tkinter as tk

def enable_next_tab(notebook, positions=1):
    """
    Enable the next shadowed tab
    """
    current_tab = notebook.index('current')
    total_tabs = len(notebook.tabs())
    
    # If there are more tabs: True
    if current_tab < total_tabs - 1:
        next_tab = current_tab + positions
        notebook.tab(next_tab, state="normal")
        notebook.select(next_tab)

    # If there are not more tabs: False
    else:
        return False
    
def enable_next_tab_prueba(self, next_tab_index):
        """Enable the next tab and draw the frame"""
        self.notebook.tab(next_tab_index, state="normal")
        self.notebook.select(next_tab_index)
        self.create_tab_content(next_tab_index)

def split_frame(frame):
    """
    Split a frame into two sides with a divider line using grid.
    """
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    # Left frame
    left_frame = tk.Frame(frame)
    left_frame.grid(row=0, column=0, sticky="nsew")

    # Divider line
    divider = tk.Frame(frame, bg="grey", width=2)
    divider.grid(row=0, column=1, sticky="ns")

    # Right frame
    right_frame = tk.Frame(frame)
    right_frame.grid(row=0, column=2, sticky="nsew")

    return left_frame, right_frame
