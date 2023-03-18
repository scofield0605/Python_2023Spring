from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.ttk as ttk
from tkscrolledframe import ScrolledFrame
from tkinter import filedialog

root= Tk()
root.title('KubeTech Shop')
root.geometry('880x650')



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

BMW=["1 Series (F40)","1 Series (F52)","2 Series Gran Coupé","2 Series","3 Series","4 Series","5 Series","6 Series","7 Series","8 Series","X1","X2","X3","X4","X5","X6","X7","Z4","2 Series Active Tourer","i3 (G28)","i4","i7","iX1","iX3","iX"]
Mercedes=["A-Class(Hatchbacks)","A-Class(Sedans)","C-Class","CLA","CLS","E-Class","EQE","EQS","S-Class","C-Class","CLA","E-Class","E-Class","EQA","EQB","EQC","G-Class","GLA","GLB","GLC","GLE","GLS","AMG GT","AMG GT 4-Door Coupé","AMG SL","AMG One","B-Class","Citan Van","Viano","EQV"]
Audi=["A1","A3","A4","A5","A6","A7","A8","e-tron GT","TT","R8","Q2","Q3","2019","Q4 e-tron","2021","Q5","Q5 e-tron","Q6","Q7","Q8","e-tron"]

listVar=StringVar()



if box.get()=='BMW':
    listVar.set(BMW)
elif box.get()=='Mercedes':
    listVar.set(Mercedes)
elif box.get()=='Audi':
    listVar.set(Audi)






listbox=Listbox(root,selectmode="extended", listvariable=listVar)
listbox.grid(row=3,column=0)
root.mainloop()