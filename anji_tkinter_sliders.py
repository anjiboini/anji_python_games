from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
root = Tk()
root.title('Wellcome to India')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')

#verrical= Scale(root, from_=0, to=200).pack()
#horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL).pack()

#...............................................................................

root.geometry("400x400")

def show():
    mylabel=Label(root, text=var.get()).pack()

var = StringVar()
c = Checkbutton(root, text="check this box, I dare you", variable=var, onvalue="Thanu Sri", offvalue="Yesha Sri")
c.deselect()
c.pack()

btn=Button(root, text="show selection", command=show).pack()




root.mainloop()