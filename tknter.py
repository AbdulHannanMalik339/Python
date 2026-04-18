from tkinter import *

window = Tk()
window.title("Welcome to tkinter app")
window.geometry('300x300')

greeting = Label(text="Hello, Tkinter" , fg='black' , bg='white' )
button = Button(text="Click me" , fg='white' , bg='black' )
entry = Entry(fg ="yellow", bg='blue', width=50)
greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=1)
frame.pack()
label = Label(master=frame, text="Smple Frame")
label.pack()

textbox = Text(fg='green' , bg='blue')
textbox.pack()

window.mainloop()