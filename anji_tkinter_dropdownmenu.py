from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
root = Tk()
root.title('Wellcome to India')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
root.geometry("400x400")
#deop down Boxes

def show():
    mylabel=Label(root, text=clicked.get()).pack()

options=[("Monday"),("Tuesday"),("Wednesday"),("Tursady"),("Friday"),("Saturday"),("Sunday")]
clicked=StringVar()
clicked.set(options[1])
drop = OptionMenu(root, clicked, *options ).pack()

btn = Button(root, text="Show Selection", command=show).pack()

root.mainloop()