import tkinter as tk
from tkinter import Tk, mainloop, ttk
root = Tk()

s = ttk.Style()
s.configure(root.Tbutton,font=('Arial',12))
root.geometry("400x400")
Mic_Button = ttk.Button(root,text="Tap to speak",style='root.Tbutton')
Mic_Button.pack(side="top")

mainloop()