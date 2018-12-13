from Tkinter import *
from tkMessageBox import showinfo

my_app = Tk(className= " Data Diri" )

L1 = Label(my_app, text = "Data Diri Mahasiswa" , font = ('Arial', 50))
L1.grid(row = 0, column = 0)
L2 = Label(my_app, text = "Nama", font = ('Arial', 25))
L2.grid(row = 1, column = 0, sticky = W)
L2 = Label(my_app, text = "Afrialdy Asyura Buana", font = ('Arial', 25))
L2.grid(row = 1, column = 1, sticky = W)
L2 = Label(my_app, text = "NIM ", font = ('Arial', 25))
L2.grid(row = 2, column = 0, sticky = W)
L2 = Label(my_app, text = "L200180175", font = ('Arial', 25))
L2.grid(row = 2, column = 1, sticky = W)
L2 = Label(my_app, text = "Buku Favorit", font = ('Arial', 25))
L2.grid(row = 3, column = 0, sticky = W)
L2 = Label(my_app, text = "Harry Potter", font = ('Arial', 25))
L2.grid(row = 3, column = 1, sticky = W)
L2 = Label(my_app, text = "Idola di Kalangan Sahabat", font = ('Arial', 25))
L2.grid(row = 4, column = 0, sticky = W)
L2 = Label(my_app, text = "Abu Bakar", font = ('Arial', 25))
L2.grid(row = 4, column = 1, sticky = W)
L2 = Label(my_app, text = "Motto", font = ('Arial', 25))
L2.grid(row = 5, column = 0, sticky = W)
L2 = Label(my_app, text = "Banyak jalan menuju Roma", font = ('Arial', 25))
L2.grid(row = 5, column = 1, sticky = W)

def logout ():
    my_app.quit()
    my_app.destroy()

A1 = Button(my_app, text ="keluar", command=logout)
A1.grid(row = 6, column = 2,)

my_app.mainloop()
