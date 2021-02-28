'''

foi aplicado o gerenc. de layout fill, o qual faz com que o componente estenda ao tamanho da janela/disponivel, podendo
ser no sentido vertical ou horizontal

'''

from tkinter import*

root = Tk()

lb1 = Label(root, text="escrito 1", bg="purple")
lb1.pack(side=TOP, fill=X)

lb2 = Label(root, text="escrito 2", bg="pink")
lb2.pack(side=LEFT, fill=Y)

lb3 = Label(root, text="escrito 3", bg="yellowgreen")
lb3.pack(side=RIGHT, fill=Y)

lb4 = Label(root, text="escrito 4", bg="green")
lb4.pack(side=BOTTOM, fill=X)

root.geometry("300x300+100+100")
root.mainloop()