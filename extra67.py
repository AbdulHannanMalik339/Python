from tkinter import *

gui = Tk()
gui.title("My First GUI")
gui.geometry("700x700")

lb1 = Label(gui, text="Username", font=("Arial Bold", 10))
lb2 = Label(gui, text="Password", font=("Arial Bold", 10))
lb3 = Label(gui, text="", font=("Arial Bold", 10))
lb1.grid(column=0, row=0)
lb2.grid(column=0, row=1)
lb3.grid(column=1, row=3)

e1 = Entry(gui, width=10)
e2 = Entry(gui, width=10)
e1.grid(column=1, row=0)
e2.grid(column=1, row=1)

def clicked():
    res = "Welcome to " + e1.get()
    lb3.configure(text=res)

btn = Button(gui, text="Login", bg="black", fg="white", command=clicked)
btn.grid(column=1, row=2)

gui.mainloop()