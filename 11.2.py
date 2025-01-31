from tkinter import Tk, Label, Entry, Button
from tkinter.messagebox import showinfo

my_app = Tk(className='Hitung')
L1 = Label(my_app, text="Angka 1")
L1.grid(row=1, column=0)
E1 = Entry(my_app)
E1.grid(row=1, column=1)
L2 = Label(my_app, text="Angka 2")
L2.grid(row=2, column=0)
E2 = Entry(my_app)
E2.grid(row=2, column=1)

def tambah():
     L4.configure(text=(int(E1.get())+int(E2.get())))
def kurang():
     L4.configure(text=(int(E1.get())-int(E2.get())))
def bagi():
     L4.configure(text=(int(E1.get())/int(E2.get())))
def kali():
     L4.configure(text=(int(E1.get())*int(E2.get())))

B1 = Button(my_app, text="+", command=tambah)
B1.grid(row=3, column=0)
B2 = Button(my_app, text="-", command=kurang)
B2.grid(row=3, column=1)
B3 = Button(my_app, text="x", command=kali)
B3.grid(row=4, column=0)
B4 = Button(my_app, text=":", command=bagi)
B4.grid(row=4, column=1)

L3 = Label(my_app, text="Hasil")
L3.grid(row=5, column=0)
L4 = Label(my_app, text="0")
L4.grid(row=5, column=1)


my_app.mainloop()
    
    
    
    
