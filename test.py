from tkinter import *
import time
import os
root = Tk()

frameCnt = 12
frames = [PhotoImage(file='D:\\uni\\python\\Lab-3\\gc_skyrim_header.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)
label = Label(root)
label.pack()
root.after(0, update, 0)
root.mainloop()