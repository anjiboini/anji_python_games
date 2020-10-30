from tkinter import  *
from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
import csv
from tkinter import ttk

root = Tk()
root.title('well come to India thanudatabase')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
root.geometry('600x400')

def myclick():
    hello = "Hello " + e.get()
    mylabel=Label(root,text=hello)
    mylabel.pack(pady=10)

e = Entry(root, width = 50)
e.pack(padx=10,pady=10)

myButton = Button(root,text="Enter you Name", command =myclick)
myButton.pack(pady=10)



root.mainloop()