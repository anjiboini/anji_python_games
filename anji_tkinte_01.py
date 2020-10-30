from tkinter import *

#..............................................
#root=Tk()

#theLable=Label(root,text="Hi anji how r u")
#theLable.pack()
#root.mainloop()
#............................................


#one=Label(root, text="One", bg="red",fg="white")
#one.pack()
#two=Label(root, text="Two", bg="yellow",fg="black")
#two.pack(fill=X)
#three=Label(root, text="Three", bg="blue",fg="white")
#three.pack(side=LEFT,fill=Y)

#topFrame=Frame(root)
#topFrame.pack()
#bottomFrame=Frame(root)
#bottomFrame.pack(side=BOTTOM)
#.......................................


#button1 = Button(topFrame, text="Thanu sri",fg="red",bg="green",padx=50,pady=50,font=300)
#button2 = Button(topFrame, text="Yesha sri",fg="blue",bg="green",padx=50,pady=50,font=300)
#button3 = Button(topFrame, text="Yesha sri",fg="blue",bg="green",padx=50,pady=50,font=300)
#button4 = Button(topFrame, text="Yesha sri",fg="blue",bg="green",padx=50,pady=50,font=300)
#button5 = Button(bottomFrame, text="Yesha sri",fg="blue",bg="green",padx=50,pady=50,font=300)
#button6 = Button(bottomFrame, text="Yesha sri",fg="blue",bg="green",padx=50,pady=50,font=300)

#button1.pack(side=LEFT)
#button2.pack(side=LEFT)
#button3.pack(side=LEFT)
#button4.pack(side=LEFT)
#button5.pack(side=BOTTOM)
#button6.pack(side=BOTTOM)
#root.mainloop()
#.........................................
#lable1=Label(root, text="Name")
#lable2=Label(root, text="Password")
#entry1=Entry(root)
#entry2=Entry(root)
#lable1.grid(row=0,column=1)
#lable2.grid(row=1,column=1)
#entry1.grid(row=0,column=2)
#entry2.grid(row=1,column=2)

#c = Checkbutton(root, text="Keep me logged in")
#c.grid(columnspan=2)

#root.mainloop()

#.............................................................

#def printName():
 #   print("Hello thanu sri whate are you doing")
#button1=Button(root, text="Click here", command=printName)
#button1.pack()
#root.mainloop()
#.................................................


class PressButtons:
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()

        self.printButton=Button(frame, text="print message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        open("wow it is working")

root= Tk()
b = PressButtons(root)
root.mainloop()


#.........................................................................




