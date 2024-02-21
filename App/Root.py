import tkinter as tk
from AppFunctions.Functions import button_click


def run_app():
    root = tk.Tk()

    label = tk.Label(root, text="Hello, Tkinter!")
    label.pack()

    button = tk.Button(root, text="Click me!", command=button_click)
    button.pack()

    root.mainloop()
