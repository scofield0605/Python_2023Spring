from tkinter import *

root= Tk()
root.title('KubeTech Shop')
root.geometry('880x650')



value=StringVar()


def Rnumber(e):
    value.set(str(R.get()))

Rlabel=Label(root,text='R:')
Rlabel.grid(row=0,column=0,sticky=W)

number= Label(root,textvariable=value, fg='black',anchor=W,bd=2)
number.grid(row=0,column=1,sticky=W)



R=Scale(root, from_=0, to=255,orient="horizontal",length=300,showvalue=True,command=Rnumber)
R.grid(row=1,column=0,columnspan=3)


value2=StringVar()

def Gnumber(e):
    value2.set(str(G.get()))

Rlabel=Label(root,text='G:')
Rlabel.grid(row=2,column=0,sticky=W)

number2= Label(root,textvariable=value2, fg='black',anchor=W,bd=2)
number2.grid(row=2,column=1,sticky=W)



G=Scale(root, from_=0, to=255,orient="horizontal",length=300,showvalue=True,command=Gnumber)
G.grid(row=3,column=0,columnspan=3)



value3=StringVar()

def Bnumber(e):
    value3.set(str(B.get()))

Blabel=Label(root,text='B:')
Blabel.grid(row=5,column=0,sticky=W)

number3= Label(root,textvariable=value3, fg='black',anchor=W,bd=2)
number3.grid(row=5,column=1,sticky=W)



B=Scale(root, from_=0, to=255,orient="horizontal",length=300,showvalue=True,command=Bnumber)
B.grid(row=6,column=0,columnspan=3)

color=Label(root,background='black',bd=2)
color.grid(row=7,column=0,columnspan=3)








root.mainloop()