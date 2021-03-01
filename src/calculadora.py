'''

brincando de criar calculadora com operacoes de dois numeros e com as operacoes basicas

obs:. a funcao "isnumeric" do python reconheceu o sinal de menos como caractere e nao efetuou calculos
de valores negativos

'''

def sum(a, b):
    if (str(a.get()).isnumeric() and str(b.get()).isnumeric()):
        lbres["text"] = float(a.get()) + float(b.get())
    else:
        lbres["text"] = "Valores informados inválidos!"

def sub(a, b):
    if (str(a.get()).isnumeric() and str(b.get()).isnumeric()):
        lbres["text"] = float(a.get()) - float(b.get())
    else:
        lbres["text"] = "Valores informados inválidos!"

def mult(a, b):
    if (str(a.get()).isnumeric() and str(b.get()).isnumeric()):
        lbres["text"] = float(a.get()) * float(b.get())
    else:
        lbres["text"] = "Valores informados inválidos!"

def div(a, b):
    if (str(a.get()).isnumeric() and str(b.get()).isnumeric()):
        if(int(b.get()) == 0):
            lbres["text"] = "Não é possível dividir por zero!"
        else:
            lbres["text"] = float(a.get()) / float(b.get())
    else:
        lbres["text"] = "Valores informados inválidos!"

from functools import partial
from tkinter import*


root = Tk()

lb1 = Label(root, font = ("consolas"), text="Valor 1 : ")
lb2 = Label(root, font = ("consolas"), text="Valor 2 : ")

ed1 = Entry(root)
ed2 = Entry(root)

bt1 = Button(root, font = ("consolas"), text="Sum")
bt1["command"] = partial(sum, ed1, ed2)
bt2 = Button(root, font = ("consolas"), text="Sub")
bt2["command"] = partial(sub, ed1, ed2)
bt3 = Button(root, font = ("consolas"), text="Mult")
bt3["command"] = partial(mult, ed1, ed2)
bt4 = Button(root, font = ("consolas"), text="Div")
bt4["command"] = partial(div, ed1, ed2)

lbres = Label(root, font = ("consolas"), text="Resultado aqui!")


lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)

ed1.grid(row=0, column=1)
ed2.grid(row=1, column=1)

bt1.grid(row=2, column=0)
bt2.grid(row=2, column=1)
bt3.grid(row=3, column=0)
bt4.grid(row=3, column=1)


lbres.grid(row=4, column=0, columnspan=2)


root.title("Calculadora")
root.geometry("400x300+200+200")
root.mainloop()