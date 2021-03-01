'''

estudando o gerenc. de laytou grid - row e column - os quais posicionam os componentes como uma "tabela"
ordenando os componentes, se nao houver nenhum componente no inicio, o componente sera realoca a posicao
inicial 0, 0

'''

#sistema de login

from tkinter import*

root = Tk()

lb1 = Label(root, text="Login: ")
lb2 = Label(root, text="Senha: ")

ed1 = Entry(root)
ed2 = Entry(root)

bt = Button(root, text="Confirmar")

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
ed1.grid(row=0, column=1)
ed2.grid(row=1, column=1)
bt.grid(row=2, column=1)

root.title("Login")
root.geometry("200x100+100+100")
root.mainloop()