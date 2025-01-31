from tkinter import Tk, Label, Entry, Button
from tkinter.messagebox import showinfo

my_app = Tk(className='Luas Bangun Geometri')
L1 = Label(my_app, text="Bangun Geometri",
           font=('Arial',24))
L1.grid(row=0, column=0)
L2 = Label(my_app, text="Prisma Segitiga")
L2.grid(row=1, column=0)
L3 = Label(my_app, text="Alas Segitiga")
L3.grid(row=2, column=0)
E3 = Entry(my_app)
E3.grid(row=2, column=1)
L4= Label(my_app, text="Tinggi Alas")
L4.grid(row=3, column=0)
E4 = Entry(my_app)
E4.grid(row=3, column=1)
L5= Label(my_app, text="Tinggi Prisma")
L5.grid(row=4, column=0)
E5 = Entry(my_app)
E5.grid(row=4, column=1)
L6= Label(my_app, text="Panjang Alas")
L6.grid(row=5, column=0)
E6 = Entry(my_app)
E6.grid(row=5, column=1)


def Prisma():
    LuasAlas = (0.5*int(E3.get())*int(E4.get()))
    LuasSelimut = (3*int(E6.get())*int(E5.get()))
    Luas.configure(text=(LuasAlas+LuasSelimut))

B = Button(my_app, text="Hitung Luas", command=Prisma)
B.grid(row=6, column=0)
Luas = Label(my_app, text="0")
Luas.grid(row=6, column=1)
