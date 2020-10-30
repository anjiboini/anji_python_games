from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Wellcome to India')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')

r = IntVar()
r.set("2")

def clicked(value):
    myLabel=Label(root,text=value)
    myLabel.pack()

Radiobutton(root,text="option 1", variable=r,value=1, command=lambda : clicked(r.get())).pack()
Radiobutton(root,text="option 2", variable=r,value=2,command=lambda : clicked(r.get())).pack()

myLabel=Label(root, text=r.get())
myLabel.pack()

myButton = Button(root, text="Click Here", command=lambda :clicked(r.get()))
myButton.pack()




root.mainloop()