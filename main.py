# import library
from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *

# deklarasi objek
hunians = []
hunians.append(Apartemen("Saul Goodman", 3, 3, 400))
hunians.append(Rumah("Gustavo Fring", 5, 2, 400))
hunians.append(Indekos("Chuck McGill", "Howard Hamlin", 400))
hunians.append(Rumah("Mike Ehrmantraut", 1, 4, 500))

root = Tk()
root.title("LATIHAN 9 - DPBO Python")


# bagian detail
def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, text = "Summary\n\n" + "Nama pemilik : " + hunians[index].get_nama_pemilik() + ".\n" + hunians[index].get_summary() + "Dokumen\n" + hunians[index].get_dokumen(), anchor = "w").grid(row = 0, column = 0, sticky = "w")

    # exit button
    b_exit = Button(d_frame, text = "Exit", command = root.quit)
    b_exit.grid(row = 1, column = 0, pady = 10)

# bagian main frame
frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
frame.pack(padx=10, pady=10)

opts = LabelFrame(root, padx=10, pady=10)
opts.pack(padx=10, pady=10)

b_add = Button(opts, text="Add Data", state="disabled")
b_add.grid(row=0, column=0)

# exit button
b_exit = Button(opts, text="Exit", command=root.quit)
b_exit.grid(row=0, column=1)


for index, h in enumerate(hunians):
    idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
    idx.grid(row=index, column=0)

    type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
    type.grid(row=index, column=1)

    if h.get_jenis() != "Indekos": 
        name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)
    else:
        name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)

    b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
    b_detail.grid(row=index, column=3)

root.mainloop()
