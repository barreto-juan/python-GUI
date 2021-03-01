'''

neste arquivo foi aplicado a propriedade do gerenc. de layout grid - sticky - o qual posiciona o componente dentro de
uma celula, ele funciona similar ao anchor

'''
from tkinter import*

root = Tk()

lb1 = Label(root, font = ("consolas"), text="Label - 1", width=30, height=2, bg="lightgreen")
lb2 = Label(root, font = ("consolas"), text="Label - 2", height=2, bg="lightblue")
lb3 = Label(root, font = ("consolas"), text="Label - 3", bg="yellow")

lb1.grid(row=0, column=0,)
lb2.grid(row=1, column=0, sticky=E)
lb3.grid(row=0, column=1, sticky=N)


root.geometry("600x100+100+100")
root.mainloop()