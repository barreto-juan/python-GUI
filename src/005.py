'''

foi utilizado o gerenc. de layout pack - anchor - o mesmo desempenha o papel de definir uma direcao para nosso componente

'''

from tkinter import*

root = Tk()

lb1 = Label(root, text="Side - 1", bg="orange")
lb2 = Label(root, text="Side - 2", bg="blue")
lb3 = Label(root, text="Anchor - 1", bg="blue")
lb4 = Label(root, text="Anchor - 2", bg="orange")

lb1.pack(side=LEFT)
lb2.pack(side=LEFT)
lb3.pack(side=TOP, anchor=E)
lb4.pack(side=BOTTOM, anchor=E)


root.geometry("300x300+100+100")
root.mainloop()