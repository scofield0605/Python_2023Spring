
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.ttk as ttk
root= Tk()
root.title('KubeTech Shop')
root.geometry('880x650')

def show():
    text=(checkbtnVal1.get())+" "+(checkbtnVal3.get())

#宣告3用於radio Btn的文字變數
checkbtnVal1=StringVar()
checkbtnVal2=StringVar()
checkbtnVal3=StringVar()
#建label
title2label=Label(root, text='轉機次數')
title2label.grid(row=0, column=0, sticky=W)
#放1按鈕
checkbtn1=Checkbutton(root,text='直飛',variable=checkbtnVal1,onvalue='直飛',offvalue="",fg='Pink',command=show)
checkbtn1.grid(row=1,column=0, sticky=W)
#放2按鈕
checkbtn2=Checkbutton(root,text='轉機一次',variable=checkbtnVal2,onvalue='轉機一次',offvalue="",fg='Pink',command=show)
checkbtn2.grid(row=1,column=1, sticky=W)

#放3按鈕
checkbtn3=Checkbutton(root,text='轉機2次以上',variable=checkbtnVal3,onvalue='轉機2次以上',offvalue="",fg='Pink',command=show)
checkbtn3.grid(row=1,column=2, sticky=W)
#建立label
statusBar2=Label(root, text='',fg='black',bg='white', anchor=W, relief='sunken',bd=2)
#加入視窗
statusBar2.grid(row=10,column=0,columnspan=3,sticky=W+E+S)

root.mainloop()