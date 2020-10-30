from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
root=Tk()
root.title('wellcome to Thanusri crmdatabase')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
root.geometry("600x400")

mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "1234",
        database = "anjidatabase",
        )
#Check to see if connection to mysql was created

#print(mydb)

#Create a cursor and intiliaze it
my_cursor = mydb.cursor()

#Create Database
#my_cursor.execute("CREATE DATABASE thanudb")
#Test to see if database was created
#my_cursor.execute("SHOW DATABASES")
#print(my_cursor)
#for db in my_cursor:
 #      print(db)
#create a table
my_cursor.execute("CREATE TABLE IF NOT EXISTS custemers (\
        first_name VARCHAR(255),\
        last_name VARCHAR(255),\
        zipcode INT(10),\
        price_paid DECIMAL(10,2),\
        user_id INT AUTO_INCREMENT PRIMARY KEY)")
'''
#Alter table
my_cursor.execute("ALTER TABLE custemers ADD (\
        email VARCHAR(255),\
        address_1 VARCHAR(255),\
        address_2 VARCHAR(255),\
        city VARCHAR(50),\
        state VARCHAR(50),\
        country VARCHAR(255),\
        phone VARCHAR(255),\
        payment_method VARCHAR(50),\
        discount_code VARCHAR(255))")
        '''

#show table
my_cursor.execute("SELECT * FROM custemers")
#print(my_cursor.description)
for thing in my_cursor.description:
        print(thing)

root.mainloop()
