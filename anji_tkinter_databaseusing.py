from tkinter import *
from PIL import ImageTk,Image
import sqlite3
root = Tk()
root.title('Wellcome to India')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
root.geometry("400x400")
#Databases
# Create a Databases or connect one
conn = sqlite3.connect('address_book.db')
    # Create cursor
c = conn.cursor()
#Create table
'''
c.execute(""" CREATE TABLE addresses ( 
               first_name   text, 
               last_name    text,
               address      text,
               city   text,
               state   text,
               zipcode integer)""")

'''
def edit():
    editor = Tk()
    editor.title('Update A Record')
    editor.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
    editor.geometry("400x600")

    # Create a Databases or connect one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    record_id = delete_box.get()
    c = conn.cursor()
    c.execute("SELECT * FROM addresses WHERE oid = "+ record_id)
    records = c.fetchall()

    # Loop thru results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + "  " + str(record[1]) + "  " + "\t" + str(record[6]) + "\n"

    # create text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    a_name_editor = Entry(editor, width=30)
    a_name_editor.grid(row=1, column=1, padx=20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)


    # create text boxes labels
    f_name_label = Label(editor, text="First Name").grid(row=0, column=0, padx=20, pady=(10, 0))
    a_name_label = Label(editor, text="Last  Name").grid(row=1, column=0, padx=20)
    address_label = Label(editor, text="Address").grid(row=2, column=0, padx=20)
    city_label = Label(editor, text="City").grid(row=3, column=0, padx=20)
    state_label = Label(editor, text="State").grid(row=4, column=0, padx=20)
    zipcode_label = Label(editor, text="Pin Code").grid(row=5, column=0, padx=20)
    #Loop thru results
    for record in records:
        f_name_editor.insert(0, record[0])
        a_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])


    #Create Save Button
    edit_btn = Button(editor, text="Save Record", command=edit).grid(row=6, column=0, columnspan=2, padx=10, pady=10,
                                                                   ipadx=145)






#Create Submit Function to Delete A Record
def delete():
    # Create a Databases or connect one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
    #Delete a record
    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())
    delete_box.delete(0, END)
    conn.commit()
    conn.close()

#create submit function for database

def submit():
    # Create a Databases or connect one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    #Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :a_name, :address, :city, :state, :zipcode )",
            {
                'f_name': f_name.get(),
                'a_name': a_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get(),
            })

    conn.commit()
    conn.close()
    #clear the  text boxes
    f_name.delete(0, END)
    a_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    zipcode.delete(0, END)
#Create Query function
def query():
    # Create a Databases or connect one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
    c.execute("SELECT *, oid  FROM addresses")
    records = c.fetchall()
    print(records)
    # Loop thru results
    print_records = ''
    for record in records:
         print_records += str(record[0]) +"  "+str(record[1])+"  "+ "\t" + str(record[6])+ "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=15, column=0,columnspan=2)
    conn.commit()
    conn.close()

#create text boxes
f_name = Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0))
a_name = Entry(root,width=30)
a_name.grid(row=1,column=1,padx=20)
address = Entry(root,width=30)
address.grid(row=2,column=1,padx=20)
city = Entry(root,width=30)
city.grid(row=3,column=1,padx=20)
state = Entry(root,width=30)
state.grid(row=4,column=1,padx=20)
zipcode = Entry(root,width=30)
zipcode.grid(row=5,column=1,padx=20)
delete_box = Entry(root,width=30).grid(row=11,column=1,pady=5)

#create text boxes labels
f_name_label= Label(root, text="First Name").grid(row=0,column=0,padx=20,pady=(10,0))
a_name_label= Label(root, text="Last  Name").grid(row=1,column=0,padx=20)
address_label= Label(root, text="Address").grid(row=2,column=0,padx=20)
city_label= Label(root, text="City").grid(row=3,column=0,padx=20)
state_label= Label(root, text="State").grid(row=4,column=0,padx=20)
zipcode_label= Label(root, text="Pin Code").grid(row=5,column=0,padx=20)

delete_box_label = Label(root, text= "Select ID ").grid(row=11,column=0,pady=5)

#Create Submit Button

submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0,columnspan=2,padx=10,pady=10,ipadx=100)


#create a Query Button
query_btn = Button(root, text="Show Records", command=query).grid(row=7, column=0,columnspan=2,padx=10,pady=10,ipadx=137)
#create a Delete Button
delete_btn = Button(root, text="Delete Record", command=delete).grid(row=12, column=0,columnspan=2,padx=10,pady=10,ipadx=137)
#Create an Update Button
edit_btn = Button(root, text="Edit Record", command=edit).grid(row=13, column=0,columnspan=2,padx=10,pady=10,ipadx=137)


conn.commit()
conn.close()

root.mainloop()
