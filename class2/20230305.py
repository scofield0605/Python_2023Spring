
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.ttk as ttk
from tkscrolledframe import ScrolledFrame
root= Tk()
root.title('KubeTech Shop')
root.geometry('880x650')
#create scrolled
sframe1=ScrolledFrame(root,width=300,height=300)
sframe1.pack()
#bind arrow key
sframe1.bind_arrow_keys(root)
sframe1.bind_scroll_wheel(root)
#create a frame
inner_frame=sframe1.display_widget(Frame)
# Bind the arrow keys and scroll wheel
sframe1.bind_arrow_keys (root)
sframe1.bind_scroll_wheel(root)
# Create a frame within the ScrolledFrame
inner_frame = sframe1.display_widget (Frame )
btn1=Button(inner_frame, text="1", height=5) 
btn2=Button (inner_frame, text="2", height=5)
btn3=Button(inner_frame, text="3", height=5)
btn4=Button (inner_frame, text ="4", height=5)
btn5=Button(inner_frame, text="5",height=5)
btn1.grid(row=0) 
btn2.grid(row=1)
btn3.grid (row=2) 
btn4.grid(row=3) 
btn5.grid(row=4)
# def show():
#     text=(checkbtnVal1.get())+" "+(checkbtnVal3.get())

# #宣告3用於radio Btn的文字變數
# checkbtnVal1=StringVar()
# checkbtnVal2=StringVar()
# checkbtnVal3=StringVar()
# #建label
# title2label=Label(root, text='轉機次數')
# title2label.grid(row=0, column=0, sticky=W)
# #放1按鈕
# checkbtn1=Checkbutton(root,text='直飛',variable=checkbtnVal1,onvalue='直飛',offvalue="",fg='Pink',command=show)
# checkbtn1.grid(row=1,column=0, sticky=W)
# #放2按鈕
# checkbtn2=Checkbutton(root,text='轉機一次',variable=checkbtnVal2,onvalue='轉機一次',offvalue="",fg='Pink',command=show)
# checkbtn2.grid(row=1,column=1, sticky=W)

# #放3按鈕
# checkbtn3=Checkbutton(root,text='轉機2次以上',variable=checkbtnVal3,onvalue='轉機2次以上',offvalue="",fg='Pink',command=show)
# checkbtn3.grid(row=1,column=2, sticky=W)
# #建立label
# statusBar2=Label(root, text='',fg='black',bg='white', anchor=W, relief='sunken',bd=2)
# #加入視窗
# statusBar2.grid(row=10,column=0,columnspan=3,sticky=W+E+S)

root.mainloop()