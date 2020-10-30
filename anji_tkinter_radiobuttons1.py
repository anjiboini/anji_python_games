from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Wellcome to India')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')


MODES=[ ("Pepperoni","Pepperoni"),("Cheese","Cheese"),("Mushroom","Muchroom"),("Onion","Onion")]
pizza = StringVar()
pizza.set("Select Itemes")

for text,mode in MODES:
    Radiobutton(root,text=text, variable=pizza, value=mode).pack()


def clicked(value):
    mylabel=Label(root, text=value)
    mylabel.pack()

myLable=Label(root,text=pizza.get()).pack()

myButton=Button(root, text="Clicked me", command=lambda :clicked(pizza.get())).pack()



root.mainloop()
