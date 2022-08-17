from tkinter import *
from langdetect import detect
from langcodes import *


root = Tk()
root.title('Belajar Python GUI with TKInter - Deteksi Bahasa!')
root.geometry("500x350")


def cek_bahasa():
    if my_text.compare("end-1c", "==", "1.0"):
        my_label.config(text="Hei! ada yang belum diisi, lupa ya?")
    else:
        code = detect(my_text.get(1.0, END))
        my_result = Language.make(language=code).display_name()
        my_label.config(text=f"Bahasa ini adalah bahasa: {my_result}!")


my_text = Text(root, height=10, width=50)
my_text.pack(pady=20)

my_button = Button(root, text="Cek Bahasa!", command=cek_bahasa)
my_button.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=10)


root.mainloop()
