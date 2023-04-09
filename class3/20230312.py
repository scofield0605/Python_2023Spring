from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.ttk as ttk
from tkscrolledframe import ScrolledFrame
from tkinter import filedialog

root= Tk()
root.title('KubeTech Shop')
root.geometry('880x650')


# sframe1=ScrolledFrame(root,width=300,height=300, bg="yellow")
# sframe1.pack()
# #bind arrow key
# sframe1.bind_arrow_keys(root)
# sframe1.bind_scroll_wheel(root)
# # Bind the arrow keys and scroll wheel
# sframe1.bind_arrow_keys (root)
# sframe1.bind_scroll_wheel(root)
# # Create a frame within the ScrolledFrame
# inner_frame = sframe1.display_widget (Frame )
# btn1=Button(inner_frame, text="1", height=5) 
# btn2=Button (inner_frame, text="2", height=5)
# btn3=Button(inner_frame, text="3", height=5)
# btn4=Button (inner_frame, text ="4", height=5)
# btn5=Button(inner_frame, text="5",height=5)
# btn1.grid(row=0) 
# btn2.grid(row=1)
# btn3.grid (row=2) 
# btn4.grid(row=3) 
# btn5.grid(row=4)

def choose():
    titleVar.set('廠牌：'+str(box.current()+1)+"."+box.get())


titleVar=StringVar()
titleVar.set('廠牌：')

title1label=Label(root,textvariable=titleVar)
title1label.grid(row=0,column=0,columnspan=2, sticky=W)
box=ttk.Combobox(root,values=['BMW','Mercedes Benz', "Audi"])
box.grid(row=1,column=0,sticky=W)
box.current(0)

choose=Button(text='OK',command=choose)
choose.grid(row=2,column=0,sticky=W)

# #crate listbox
listVar=StringVar()
listbox=Listbox(root,selectmode='extended')
# listbox.insert(1,"A1")
# listbox.insert(2,"A3")
# listbox.insert(3,"A4")
# listbox.grid()

#create ListBox
BMW=["1 Series (F40)","1 Series (F52)","2 Series Gran Coupé","2 Series","3 Series","4 Series","5 Series","6 Series","7 Series","8 Series","X1","X2","X3","X4","X5","X6","X7","Z4","2 Series Active Tourer","i3 (G28)","i4","i7","iX1","iX3","iX"]
Mercedes=["A-Class(Hatchbacks)","A-Class(Sedans)","C-Class","CLA","CLS","E-Class","EQE","EQS","S-Class","C-Class","CLA","E-Class","E-Class","EQA","EQB","EQC","G-Class","GLA","GLB","GLC","GLE","GLS","AMG GT","AMG GT 4-Door Coupé","AMG SL","AMG One","B-Class","Citan Van","Viano","EQV"]
Audi=["A1","A3","A4","A5","A6","A7","A8","e-tron GT","TT","R8","Q2","Q3","2019","Q4 e-tron","2021","Q5","Q5 e-tron","Q6","Q7","Q8","e-tron"]

listVar.set()
listbox=Listbox(root,selectmode="extended",listvariable=listVar)
listbox.grid(row=3,column=0)
#單選檔案
# filePath=filedialog.askopenfilename()

# filePath=filedialog.askopenfilename(title='選取照片',initialdir='/Users/scofield/Documents/Python_2023Spring/class2',multiple=TRUE)
# print(filePath)
root.mainloop()