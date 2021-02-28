'''

gerenciador de layout pack - side - com ele nos definimos um sentido para nossos componentes na janela

'''

from tkinter import*

root = Tk()

lb1 = Label(root, text="Label 1", bg="lightblue")
lb2 = Label(root, text="Label 2", bg="lightpink")
lb3 = Label(root, text="Label 3", bg="lightgreen")
lb4 = Label(root, text="Label 4", bg="orangered")

lb1.pack()
lb2.pack(side=LEFT)
lb3.pack(side=RIGHT)
lb4.pack(side=BOTTOM)

root.geometry("300x300+100+100")
root.mainloop()