import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from code_1 import organizer
import os

def browse_button():
    filename = filedialog.askopenfilename()
    folder_path.set(filename)
    button_convert['state'] = "enabled"

def convert():
    folder_dest = filedialog.askdirectory()
    organizer(folder_path.get(), folder_dest)


window = tk.Tk()
window.title("exercice")
window.geometry("600x500")
folder_path = tk.StringVar()
button_browser = ttk.Button(window, text = "Ouvrir", command = browse_button)
button_browser.pack()
button_convert = ttk.Button(window, text = "Convert", state = "disabled", command = convert)
button_convert.pack()


window.mainloop()