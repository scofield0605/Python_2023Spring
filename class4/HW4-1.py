from tkinter import *

root= Tk()
root.title('KubeTech Shop')
root.geometry('880x650')



value=StringVar()

#建立下getValue function
def getValue(a):
#取得RGB
    r = int(R.get ())
    g = int(G.get ())
    b = int(B.get ())
# 數值轉換為16進位
    hex ="#{:02x}{:02x}{:02x}".format(r, g, b)
#分別設定 Label 文字內容
    Rlabel["text"]="R:"+str(R.get ())
    Glabel["text"]="G:"+str(G.get ())
    Blabel["text"]="B: "+str(B.get ())
#分別設定 statusBar1 背景
    color["bg"]=hex 
    color["text"]=hex



Rlabel=Label(root,text='R:')
Rlabel.grid(row=0,column=0,sticky=W)

number= Label(root,textvariable=value, fg='black',anchor=W,bd=2)
number.grid(row=0,column=1,sticky=W)



R=Scale(root, from_=0, to=255,orient="horizontal",length=300,showvalue=True,command=getValue)
R.grid(row=1,column=0,columnspan=3)


value2=StringVar()

def Gnumber(e):
    value2.set(str(G.get()))

Glabel=Label(root,text='G:')
Glabel.grid(row=2,column=0,sticky=W)

number2= Label(root,textvariable=value2, fg='black',anchor=W,bd=2)
number2.grid(row=2,column=1,sticky=W)



G=Scale(root, from_=0, to=255,orient="horizontal",length=300,showvalue=True,command=getValue)
G.grid(row=3,column=0,columnspan=3)



value3=StringVar()

def Bnumber(e):
    value3.set(str(B.get()))

Blabel=Label(root,text='B:')
Blabel.grid(row=5,column=0,sticky=W)

number3= Label(root,textvariable=value3, fg='black',anchor=W,bd=2)
number3.grid(row=5,column=1,sticky=W)



B=Scale(root, from_=0, to=255,orient="horizontal",length=300,showvalue=True,command=getValue)
B.grid(row=6,column=0,columnspan=3)

color=Label(root,text='',fg='white',bg='white',bd=2,font=(20),relief="sunken")
color.grid(row=7,column=0,columnspan=3,sticky=W+E+S)









root.mainloop()
