from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image")
root.geometry("400x400")

upload = Image.open("front-of-a-white-bmw-m4-parked-on-a-street-with-trees-in-the-background.webp")
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, height=350, width=300)
label.place(x=50, y=0)
label2 = Label(root, text="Bmw M4")
label2.place(x=40, y=360)

root.mainloop()