'''

foi trabalhado a mesclagem de celulas - liinhas e colunas com o rowspan e comlumnspan e foi revisado o conteudo
de sticky

'''

from tkinter import*

root = Tk()

lb1 = Label(root, text="Label - 1", width=10, height=4, bg="red")
lb2 = Label(root, text="Label - 2", width=10, height=4, bg="green")
lb3 = Label(root, text="Label - 3", width=10, height=4, bg="blue")
lb4 = Label(root, text="Label - 4", width=10, height=4, bg="yellow")


lb5 = Label(root, text="Label - 5", bg="orangered")
lb6 = Label(root, text="Label - 6", bg="darkred")

lb1.grid(row=0, column=0)
lb2.grid(row=0, column=1)
lb3.grid(row=1, column=0)
lb4.grid(row=1, column=1)

lb5.grid(row=2, column=0, columnspan=2, sticky=W+E)
lb6.grid(row=0, column=2, rowspan=2, sticky=N+S)

root.geometry()
root.mainloop()