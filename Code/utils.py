##### UTILS.py

import tkinter as tk

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
