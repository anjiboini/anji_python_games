from tkinter import *
import sqlite3

root=Tk()
root.title('wellcome Thanusri')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
root.geometry("600x400")

#Create Database
createDb = sqlite3.connect('anji_mobile_book17.db')
c = createDb.cursor()

c.execute(""" CREATE TABLE addresses ( 
               first_name   text, 
               last_name    text,
               mobile_number   text)""")

#createDb.commit()
#createDb.close()


def submit():
    # Create a Databases or connect one
    conn = sqlite3.connect('anji_mobile_book17.db')
    # Create cursor
    c = conn.cursor()

    #Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :m_number )",
              {'f_name': f_name.get(),
                    'l_name': l_name.get(),
                    'm_number': m_number.get()})


    #clear the  text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    m_number.delete(0, END)


#Create Query function


#create text boxes
f_name = Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0))
l_name = Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20)
m_number = Entry(root,width=30)
m_number.grid(row=2,column=1,padx=20)



#create text boxes labels
f_name_label= Label(root, text="First Name").grid(row=0,column=0,padx=20,pady=(10,0))
l_name_label= Label(root, text="Last Name").grid(row=1,column=0,padx=20,pady=(10,0))
m_number_label= Label(root, text="Mobile Number").grid(row=2,column=0,padx=20,pady=(10,0))




#Create Submit Button

submit_btn = Button(root, text="Submit", command=submit)
submit_btn.grid(row=3, column=0,columnspan=2,padx=10,pady=10,ipadx=100)

createDb.commit()
createDb.close()

root.mainloop()
