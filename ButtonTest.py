from tkinter import *


def hi():
    print('Hello! Nice to see you')


tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
btn = Button(tk, text="Push me!", command=hi)
btn.pack()
canvas.create_line(0, 0, 500, 500)
