from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Main")

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("TopLevel")
    l2 = Label(top, text="This is a TopLevel Window")
    l2.pack()
    top.mainloop()

l = Label(root, text="This is root Window")
btn = Button(root, text="Open TopLevel Window", command=topwin)
l.pack()
btn.pack()
root.mainloop()