from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Contoh aplikasi Tkinter')
root.iconbitmap('./cangkir.ico')

img = ImageTk.PhotoImage(Image.open("avatar.png"))
label = Label(image=img)
label.pack()

btn_tutup = Button(root, text="Tutup", command=root.quit)
btn_tutup.pack()

root.mainloop()
