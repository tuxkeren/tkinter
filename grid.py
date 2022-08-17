from tkinter import *

root = Tk()

# membuat sebuah widget label
Labelku1 = Label(root, text="Halo Dunia!")
Labelku2 = Label(root, text="Nama saya TkInter.")

Labelku1.grid(row=0, column=0)
Labelku2.grid(row=1, column=0)


root.mainloop()
