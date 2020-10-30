from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt


root=Tk()
root.title('wellcome to Thanusri Matplotlib')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
root.geometry("600x400")

def graph():
    house_prices = np.random.normal(200000,25000,5000)
    plt.polar(house_prices)
    plt.show()

my_button = Button(root, text="Graph It", command=graph).pack()



root.mainloop()
