from tkinter import *
from PIL import ImageTk,Image
import sqlite3
root = Tk()
root.title('Wellcome to India')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
root.geometry("400x400")
#Databases
# Create a Databases or connect one
conn = sqlite3.connect('address_book8.db')
    # Create cursor
c = conn.cursor()
#Create table
''''
c.execute(""" CREATE TABLE addresses ( 
               first_name   text, 
               last_name    text)""")

'''

def submit():
    # Create a Databases or connect one
    conn = sqlite3.connect('address_book8.db')
    # Create cursor
    c = conn.cursor()

    #Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name )",
                { 'f_name': f_name.get(),
                    'l_name': l_name.get(),})

    conn.commit()
    conn.close()
    #clear the  text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)

#Create Query function


#create text boxes
f_name = Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0))
l_name = Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20)



#create text boxes labels
f_name_label= Label(root, text="First Name").grid(row=0,column=0,padx=20,pady=(10,0))
l_name_name_label= Label(root, text="Last  Name").grid(row=1,column=0,padx=20)




#Create Submit Button

submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=3, column=0,columnspan=2,padx=10,pady=10,ipadx=100)



conn.commit()
conn.close()


root.mainloop()

