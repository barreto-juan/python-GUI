'''

trabalhando com imagens - PhotoImage()

'''

from tkinter import*


root = Tk()

label = Label(root, font = ("arial", 10, "bold"),text="Adicionando imagens", bg="lightblue")
label.pack(side=TOP, fill=X, expand=1)

imagem = PhotoImage(file = "homercat.png")
lphoto = Label(root, image = imagem)
lphoto.pack()

root.geometry()
root.mainloop()