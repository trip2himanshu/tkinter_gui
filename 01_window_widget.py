# python gui using tkinter
# himanshu tripathi

# creating widgets with tkinter

import tkinter as tk
from tkinter import ttk


def Abutton_func():
    print("A button is pressed")


def exercise():
    print("Exercise button is pressed")


# create a window
window = tk.Tk()
window.title("Window Widget App")
window.geometry("800x500")

# ttk label widget
label = ttk.Label(master=window, text="Window Widget App")
label.pack()

# tk text widget
text = tk.Text(master=window)
text.pack()

# ttk entry widget
entry = ttk.Entry(master=window)
entry.pack()

# exercise label
exercise_label = ttk.Label(master=window, text="New Label")
exercise_label.pack()

# button widget
button = ttk.Button(master=window, text="A button", command=Abutton_func)
button.pack()

# exercise button
exercise_button = ttk.Button(master=window, text="Exercise", command=exercise)
exercise_button.pack()

# run the app
window.mainloop()
