'''

estaudo do gernec. de laytou pack - expand - propriedade que deixa nossos componentes responsivos

'''

from tkinter import *

root = Tk()

lb1 = Label(root, text="Label - 1", bg="pink")
lb2 = Label(root, text="Label - 2", bg="purple")

lb1.pack(side=LEFT, fill=BOTH, expand=1)
lb2.pack(side=RIGHT, fill=BOTH, expand=1)

root.geometry("300x300+100+100")
root.mainloop()