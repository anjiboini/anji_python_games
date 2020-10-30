from tkinter import *
from PIL import ImageTk,Image
import sqlite3
root = Tk()
root.title('Wellcome to India')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
root.geometry("400x400")
#Databases
#Create a Databases or connect one
conn = sqlite3.connect('address_book.db')
#Create cursor
c = conn.cursor()

#Create table

c.execute(""" CREATE TABLE addresses ( 
               first_name   text, 
               last_name    text,
               address      text,
               city   text,
               state   text,
               zipcode integer)""")

conn.commit()
conn.close()

root.mainloop()