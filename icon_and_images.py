from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Contoh aplikasi Tkinter')
root.iconbitmap('images/cangkir.ico')

img = ImageTk.PhotoImage(Image.open("images/avatar.png"))
label = Label(image=img)
label.pack()

btn_tutup = Button(root, text="Tutup", command=root.quit)
btn_tutup.pack()

root.mainloop()
