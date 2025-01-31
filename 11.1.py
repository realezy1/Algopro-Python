from tkinter import Tk, Label, Entry, Button
from tkinter.messagebox import showinfo

my_app = Tk(className='Data diri')
L1 = Label(my_app, text="Data diri",
           font=('Arial',24))
L1.grid(row=0, column=0)
L2 = Label(my_app, text="Nama")
L2.grid(row=1, column=0)
E2 = Entry(my_app)
E2.grid(row=1, column=1)
L3 = Label(my_app, text="NIM")
L3.grid(row=2, column=0)
E3 = Entry(my_app)
E3.grid(row=2, column=1)
L4 = Label(my_app, text="Buku favorit")
L4.grid(row=3, column=0)
E4 = Entry(my_app)
E4.grid(row=3, column=1)
L4 = Label(my_app, text="Idola di kalangan sahabat")
L4.grid(row=4, column=0)
E4 = Entry(my_app)
E4.grid(row=4, column=1)
L5 = Label(my_app, text="Motto")
L5.grid(row=5, column=0)
E5 = Entry(my_app)
E5.grid(row=5, column=1)


def tutup():
    my_app.destroy()

B= Button(my_app, text ="Tutup", command=tutup)
B.grid(row=6, column=1)
my_app.mainloop()

