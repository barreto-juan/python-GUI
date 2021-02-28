from tkinter import*

def bt_click():
    if (str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
        lb["text"] = int(ed1.get()) + int(ed2.get())
    else:
        lb["text"] = "Valores informados inválidos!"

root = Tk()

ed1 = Entry(root)
ed1.place(x=100, y=70)

ed2 = Entry(root)
ed2.place(x=100, y=100)

bt = Button(root, text="Somar", command=bt_click)
bt.place(x=100, y=130)

lb = Label(root, text="Resultado aqui")
lb.place(x=100, y=160)

root.geometry("300x300+100+100")
root.mainloop()