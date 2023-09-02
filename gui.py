import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from code_1 import organizer
import os
from tkPDFViewer import tkPDFViewer as pdf
import sys


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def browse_button(v1):
    filename = filedialog.askopenfilename(filetypes=[('pdf file', '*.pdf')])
    frame = ttk.Frame(notebook1)
    v3 = pdf.ShowPdf()
    v3.img_object_li.clear()
    v1.append(v3)
    wid = str(int(window.winfo_screenwidth()) // 14)
    v2 = v3.pdf_view(frame, pdf_location = filename, width = wid, height = "60")
    v2.pack()
    notebook1.add(frame, text = os.path.basename(filename).split(".")[0])
    folder_path.set(filename)
    button_convert['state'] = "enabled"
    

def convert(v1):
    folder_dest = filedialog.askdirectory()
    wid = str(int(window.winfo_screenwidth()) // 15)
    folders = organizer(folder_path.get(), folder_dest)
    for fol in folders:
        files = os.listdir(fol)
        i = 0
        for file in files:
            i = i + 1
            frame = ttk.Frame(notebook2)
            v3 = pdf.ShowPdf()
            v1.append(v3)
            v2 = v3.pdf_view(frame, pdf_location = fol + "/" + file, width = wid, height = "60")
            v2.pack()
            notebook2.add(frame, text= os.path.basename(fol) + "_" + file)

    

    



v1 = []
v2 = []
window = tk.Tk()
window.title("University schedule")
width= window.winfo_screenwidth()               
height= window.winfo_screenheight()               
window.geometry("%dx%d" % (width, height))
window.tk.call("source", resource_path("Azure-ttk-theme-main\\azure.tcl"))
window.tk.call("set_theme", "light")
folder_path = tk.StringVar()
frame = ttk.Frame(window)
button_browser = ttk.Button(frame, text = "Ouvrir", command = lambda: browse_button(v1))
button_browser.grid(row=0,column=0, sticky=tk.W)
notebook1 = ttk.Notebook(window)
notebook2 = ttk.Notebook(window)
button_convert = ttk.Button(frame, text = "Convertir", state = "disabled", command = lambda: convert(v2))
button_convert.grid(row=0,column=1, sticky=tk.W)
frame.pack()
notebook1.pack(side="left")
notebook2.pack(side="right")


window.mainloop()
