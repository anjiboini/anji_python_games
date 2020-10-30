from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
root = Tk()
root.title('Wellcome to India')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')

def open():
    global my_image
    root.filename= filedialog.askopenfilename(initialdir="D:/anji_python software/python/anji tkinter projects/resources", title="Select A File",filetypes=(("jpg files","*.jpg"),("all files","*.*")))
    label=Label(root, text=root.filename).pack()
    my_image=ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

my_btn= Button(root, text="Open File", command=open).pack()

root.mainloop()