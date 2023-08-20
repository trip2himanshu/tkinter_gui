# python gui using tkinter
# himanshu tripathi

# creating frames using tkinter

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Frames demo")
window.geometry("800x500")

# window label
window_label = ttk.Label(master=window,
                         text="Window Label",
                         font="Roboto 24 bold")
window_label.pack(pady=5)

# frame
frame = ttk.Frame(master=window,
                  width=200,
                  height=100,
                  borderwidth=10,
                  relief=tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side="top")

# frame label
frame_label = ttk.Label(master=frame, text="Frame Label")
frame_label.pack()

# button inside the frame
button = ttk.Button(master=frame, text="Press me")
button.pack(side="right", padx=5)

# frame label 2
frame_label2 = ttk.Label(master=frame, text="Button")
frame_label2.pack(side="left", padx=5)

# run the app
window.mainloop()
