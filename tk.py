import tkinter as tk

win = tk.Tk()
b1 = tk.Button(win, text="Button #1")
b2 = tk.Button(win, text="Button #2")
b3 = tk.Button(win, text="Button #3")
b1.grid(row=0,column=0)
b2.grid(row=3,column=1)
b3.grid(row=0,column=2)
win.mainloop()
