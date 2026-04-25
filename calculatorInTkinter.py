from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

upload = Image.open("Luffy.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(root,
    text="Hey User! Welcome to Denomination Counter Application.",
    bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)


def topwin():
    top = Toplevel(root)
    top.title("Currency Denomination Counter")
    top.configure(bg='grey')
    top.geometry('600x400')

    title_lbl = Label(top,
        text="Enter the amount:",
        bg='grey', fg='white',
        font=('Arial', 12, 'bold'))
    title_lbl.place(x=230, y=50)

    entry = Entry(top, font=('Arial', 12), justify='center')
    entry.place(x=200, y=80, width=200)

    result_header = Label(top,
        text="Denomination Breakdown",
        bg='grey', fg='white',
        font=('Arial', 12, 'bold'))
    result_header.place(x=180, y=170)

    l1 = Label(top, text="500 x", bg='grey', fg='white',
               font=('Arial', 11))
    l2 = Label(top, text="100 x", bg='grey', fg='white',
               font=('Arial', 11))
    l3 = Label(top, text="50  x", bg='grey', fg='white',
               font=('Arial', 11))
    l1.place(x=180, y=210)
    l2.place(x=180, y=240)
    l3.place(x=180, y=270)

    t1 = Label(top, text="0", bg='white', fg='black',
               font=('Arial', 11), width=10)
    t2 = Label(top, text="0", bg='white', fg='black',
               font=('Arial', 11), width=10)
    t3 = Label(top, text="0", bg='white', fg='black',
               font=('Arial', 11), width=10)
    t1.place(x=270, y=210)
    t2.place(x=270, y=240)
    t3.place(x=270, y=270)

    def calculate():
        try:
            amount = int(entry.get())
            if amount < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input",
                "Please enter a valid non-negative whole number.")
            return

        c500 = amount // 500
        amount %= 500
        c100 = amount // 100
        amount %= 100
        c50 = amount // 50
        remainder = amount % 50

        t1.config(text=str(c500))
        t2.config(text=str(c100))
        t3.config(text=str(c50))

        if remainder:
            messagebox.showinfo("Note",
                f"Remaining amount that cannot be broken into "
                f"500/100/50: {remainder}")

    btn = Button(top, text="Calculate", command=calculate,
                 bg='brown', fg='white', font=('Arial', 11, 'bold'))
    btn.place(x=265, y=120)


def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomination count?")
    if MsgBox == 'ok':
        topwin()


button1 = Button(root,
    text="Let's get started!",
    command=msg,
    bg='brown',
    fg='white')
button1.place(x=260, y=360)

root.mainloop()