from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
root = Tk()
root.title('Wellcome to India')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')

#showinfo, showwarning, showerror, askquestion,askokcancel, askyesno
def popup():
    response=messagebox.askquestion("This is thanu sri popup!", "Hello Yesha Sri")
    Label(root, text=response).pack()
    if response =="yes":
        Label(root, text="You clicked thanu sri").pack()
    else:
        Label(root, text="You clicked Yesha sri").pack()

Button(root, text="Popup", command=popup).pack()







root.mainloop()
