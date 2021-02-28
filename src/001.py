'''

primeira interface grafica criada - foi utilizada uma widget de label e tambem a propriedade mais simples do gerenc.
de layout pack, o place

'''

from tkinter import*

root = Tk()

lb = Label(root, text="Olá mundo!!!")
lb.place(x=100, y=100)

root.geometry("300x300+100+100")
root.mainloop()