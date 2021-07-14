import random
from tkinter import *

root = Tk()
root.geometry('500x300')

l1 = Label(root,font=('times',200))


def roll():
    numbers = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(numbers)}')
    l1.pack()


b1 = Button(root,text='Lets roll...',command=roll)
b1.place(x=230,y=20)

root.mainloop()