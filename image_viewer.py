from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Contoh aplikasi Tkinter')
root.iconbitmap('./cangkir.ico')

img1 = ImageTk.PhotoImage(Image.open("images/avatar.png"))
img2 = ImageTk.PhotoImage(Image.open("images/avatar2.jpg"))
img3 = ImageTk.PhotoImage(Image.open("images/avatar3.jpg"))

image_list = [img1, img2, img3]
image_list[2]

label = Label(image=img1)
label.grid(row=0, column=0, columnspan=3)

def next(img_number):
    global label
    global btn_next
    global btn_back

    label.grid_forget()
    label = Label(image=image_list[img_number - 1])
    btn_next = Button(root, text=">>", command=lambda: next(img_number + 1))
    btn_back = Button(root, text="<<", command=lambda: next(img_number - 1))
    btn_back.grid(row=1, column=0)
    btn_next.grid(row=1, column=2)

    if img_number == 3 :
        btn_next = Button(root, text=">>", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)

def back(img_number):
    global label
    global btn_next
    global btn_back

    label.grid_forget()
    label = Label(image=image_list[img_number - 1])
    btn_next = Button(root, text=">>", command=lambda: next(img_number - 1))
    btn_back = Button(root, text="<<", command=lambda: next(img_number + 1))
    btn_back.grid(row=1, column=0)
    btn_next.grid(row=1, column=2)

    if img_number == 3 :
        btn_back = Button(root, text="<<", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)


btn_back = Button(root, text="<<", command=back)
btn_tutup = Button(root, text="Tutup", command=root.quit)
btn_next = Button(root, text=">>", command=lambda: next(2))


btn_back.grid(row=1, column=0)
btn_tutup.grid(row=1, column=1)
btn_next.grid(row=1, column=2)


root.mainloop()
