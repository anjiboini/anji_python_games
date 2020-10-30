from tkinter import *
from PIL import ImageTk,Image

root = Tk()


root.title('Wellcome to India')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')

frame=LabelFrame(root,text="This is Thanu",padx=50,pady=50)
frame.pack(padx=100,pady=100)



b1=Button(frame,text="Dont't Click here!")
b2=Button(frame,text="...or here!")


b1.grid(row=0,column=0)
b2.grid(row=1,column=1)



root.mainloop()