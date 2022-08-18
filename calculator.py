from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Logic program untuk command tombol.
def btn_click(nomor):
    sekarang = e.get()
    e.delete(0,END)
    e.insert(0, str(sekarang) + str(nomor))


def btn_hapus():
    e.delete(0, END)


def btn_tambah():
    nomor_awal = e.get()
    global f_num
    global math
    math = "tambah"
    f_num = int(nomor_awal)
    e.delete(0, END)

def btn_kurang():
    nomor_awal = e.get()
    global f_num
    global math
    math = "kurang"
    f_num = int(nomor_awal)
    e.delete(0, END)

def btn_kali():
    nomor_awal = e.get()
    global f_num
    global math
    math = "kali"
    f_num = int(nomor_awal)
    e.delete(0, END)

def btn_bagi():
    nomor_awal = e.get()
    global f_num
    global math
    math = "bagi"
    f_num = int(nomor_awal)
    e.delete(0, END)

def btn_sama_dengan():
    nomor_akhir = e.get()
    e.delete(0,END)
    if math == "tambah":
        e.insert(0, f_num + int(nomor_akhir))

    if math == "kurang":
        e.insert(0, f_num - int(nomor_akhir))

    if math == "kali":
        e.insert(0, f_num * int(nomor_akhir))

    if math == "bagi":
        e.insert(0, f_num / int(nomor_akhir))

# Akhir logic program.     

# Mendefinisikan tombol-tombol
tombol_1 = Button(root,text="1", padx=40, pady=20, command=lambda: btn_click(1))
tombol_2 = Button(root,text="2", padx=40, pady=20, command=lambda: btn_click(2))
tombol_3 = Button(root,text="3", padx=40, pady=20, command=lambda: btn_click(3))
tombol_4 = Button(root,text="4", padx=40, pady=20, command=lambda: btn_click(4))
tombol_5 = Button(root,text="5", padx=40, pady=20, command=lambda: btn_click(5))
tombol_6 = Button(root,text="6", padx=40, pady=20, command=lambda: btn_click(6))
tombol_7 = Button(root,text="7", padx=40, pady=20, command=lambda: btn_click(7))
tombol_8 = Button(root,text="8", padx=40, pady=20, command=lambda: btn_click(8))
tombol_9 = Button(root,text="9", padx=40, pady=20, command=lambda: btn_click(9))
tombol_0 = Button(root,text="0", padx=40, pady=20, command=lambda: btn_click(0))
tombol_tambah = Button(root, text="+", padx=39, pady=20, command=btn_tambah)
tombol_kurang = Button(root, text="-", padx=41, pady=20, command=btn_kurang) 
tombol_kali = Button(root, text="*", padx=40, pady=20, command=btn_kali)
tombol_bagi = Button(root, text="/", padx=41, pady=20, command=btn_bagi)
tombol_sama_dengan = Button(root, text="=", padx=91, pady=20, command=btn_sama_dengan)
tombol_hapus = Button(root, text="Hapus", padx=79, pady=20, command=btn_hapus)
# Akhir mendefiniskan tombol-tombol

# Menampilkan tombol-tombol ke layar
tombol_1.grid(row=3, column=0)
tombol_2.grid(row=3, column=1)
tombol_3.grid(row=3, column=2)
tombol_4.grid(row=2, column=0)
tombol_5.grid(row=2, column=1)
tombol_6.grid(row=2, column=2)
tombol_7.grid(row=1, column=0)
tombol_8.grid(row=1, column=1)
tombol_9.grid(row=1, column=2)
tombol_0.grid(row=4, column=0)
tombol_hapus.grid(row=4, column=1, columnspan=2)
tombol_tambah.grid(row=5, column=0)
tombol_kurang.grid(row=6, column=0)
tombol_kali.grid(row=6, column=1)
tombol_bagi.grid(row=6, column=2)
tombol_sama_dengan.grid(row=5, column=1, columnspan=2)
# Akhir menampilkan tombol-tombol

# menjalankan program
root.mainloop()
