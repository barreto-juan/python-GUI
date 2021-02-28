'''

alteracao de conteudo de label atraves do que o usuario digitar

'''

from tkinter import *
from functools import partial

def bt_click(e):
    lb["text"] = e.get()

root = Tk()

ed = Entry(root)
ed.place(x=100, y=70)

bt = Button(root, text="Imprimir")
bt["command"] = partial(bt_click, ed)
bt.place(x=100, y=100)

lb = Label(root, text="Texto")
lb.place(x=100, y=130)

root.geometry("300x300+100+100")
root.mainloop()