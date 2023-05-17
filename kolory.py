import tkinter as tk

win = tk.Tk()
b = tk.Button(win, text="Button #1",
              bg="#9370DB",
              fg="#FFA07A",
              activeforeground="#FFF0F5",
              activebackground="#FF69B4")
b.pack()
win.mainloop()
