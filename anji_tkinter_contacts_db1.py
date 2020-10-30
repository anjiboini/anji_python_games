from tkinter import *
import sqlite3

root = Tk()
root.title('Wellcomt to thanusri')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
root.geometry('500x400')
createDb = sqlite3.connect('anji_contacts_book')
db = createDb.cursor()
'''
db.execute(""" Create Table Addresses   (
                     first_name     text,
                     last_name       text,
                     m_number        integer  )""")
'''
#Create edit button to update record
def edit():
    editor = Tk()
    editor.title('Update record yeshasri')
    editor.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
    editor.geometry('600x400')
    createDb = sqlite3.connect('anji_contacts_book')

    db = createDb.cursor()
    record_id = delete_box.get()

    db.execute("DELETE  FROM addresses WHERE oid = " + record_id)
    records = db.fetchall()

    # Create Entry Text Boxes

    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=2, padx=20, pady=10)
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=2, padx=20, pady=10)
    m_number_editor = Entry(editor, width=30)
    m_number_editor.grid(row=2, column=2, padx=20, pady=10)


    # Cteate Text Labels
    f_name_labels = Label(editor, text="First Name", font=20)
    f_name_labels.grid(row=0, column=1, padx=20, pady=10)
    l_name_labels = Label(editor, text="Last Name", font=20)
    l_name_labels.grid(row=1, column=1, padx=20, pady=10)
    m_number_labels = Label(editor, text="Mobile Number", font=20)
    m_number_labels.grid(row=2, column=1, padx=20, pady=10)

    # Loop thru results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        m_number_editor.insert(0, record[2])


    # Create Save Button
    edit_btn = Button(editor, text="Save", command=edit)
    edit_btn.grid(row=3, column=1, padx=30, pady=10, columnspan=2,ipadx=100)
    #show_editor_btn = Button(editor, text="Show", command=show).grid(row=4, column=1, padx=30, pady=10, columnspan=2, ipadx=100)





def submit():
    createDb = sqlite3.connect('anji_contacts_book')
    db = createDb.cursor()
    db.execute("INSERT INTO addresses VALUES ( :f_name, :l_name, :m_number)",
               {  'f_name' : f_name.get(),
                  'l_name' : l_name.get(),
                  'm_number' : m_number.get()})

    #clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    m_number.delete(0, END)

    createDb.commit()
    createDb.close()

def show():
    createDb = sqlite3.connect('anji_contacts_book')
    db = createDb.cursor()
    db.execute("SELECT *, oid FROM addresses")
    records = db.fetchall()
    print(records)
    #Loop thru results
    print_records= '_'
    for record in records:
        print_records += str(record[0]) + "    "+str(record[3])+ "\n\n"

    show_label = Label(root, text=print_records)
    show_label.grid(row=7, column=2,columnspan=2)

    createDb.commit()
    createDb.close()

def delete():
    createDb = sqlite3.connect('anji_contacts_book')
    db = createDb.cursor()
    #delete a record
    db.execute("DELETE  FROM addresses WHERE oid = " + delete_box.get())
    delete_box.delete(0, END)

    createDb.commit()
    createDb.close()

#Create Entry Text Boxes
f_name = Entry(root,width=30)
f_name.grid(row=0,column=2,padx=20,pady=10)
l_name = Entry(root,width=30)
l_name.grid(row=1,column=2,padx=20,pady=10)
m_number = Entry(root,width=30)
m_number.grid(row=2,column=2,padx=20,pady=10)
delete_box = Entry(root,width=30)
delete_box.grid(row=5,column=2,padx=20,pady=10)

#Cteate Text Labels
f_name_labels=Label(root,text="First Name",font=20)
f_name_labels.grid(row=0,column=1,padx=20,pady=10)
l_name_labels=Label(root,text="Last Name",font=20)
l_name_labels.grid(row=1,column=1,padx=20,pady=10)
m_number_labels=Label(root,text="Mobile Number",font=20)
m_number_labels.grid(row=2,column=1,padx=20,pady=10)
delete_box_labels=Label(root,text="Select ID",font=20)
delete_box_labels.grid(row=5,column=1,padx=20,pady=10)

#Create Buttons
submit_btn = Button(root,text="Submit",command=submit).grid(row=3,column=1,padx=30,pady=10,columnspan=2,ipadx=100)
show_btn = Button(root,text="Show",command=show).grid(row=4,column=1,padx=30,pady=10,columnspan=2,ipadx=100)
delete_btn = Button(root,text="Delete",command=delete).grid(row=6,column=1,padx=30,pady=10,columnspan=2,ipadx=100)
edit_btn = Button(root,text="Update Record",command=edit).grid(row=7,column=1,padx=30,pady=10,columnspan=2,ipadx=100)


createDb.commit()
createDb.close()

root.mainloop()


