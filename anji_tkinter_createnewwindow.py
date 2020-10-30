from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
root = Tk()
root.title('Wellcome to India')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')

def open():
    global photo
    top = Toplevel()
    btn2 = Button(top, text="Close window", command=top.destroy).pack()
    photo = ImageTk.PhotoImage(Image.open("D:/anji_python software/python/anji tkinter projects/resources/thanu.jpg"))
    lbl = Label(top, image=photo).pack()


btn1=Button(root,text="Open second Window1", command=open).pack()

root.mainloop()