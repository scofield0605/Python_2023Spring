import tkinter.ttk as ttk
from tkinter import *
from PIL import Image , ImageTk
root= Tk()


root.title('hello world')
root.geometry('1000x300+500+150')
img=Image.open('/Users/scofield/Documents/Python_2023Spring/class1/logo_tree.png')
tk_img=ImageTk.PhotoImage(img)

root.iconphoto(True,tk_img)
#設定Icon
# label1=Label(root, text='flat', relief='flat')
#建label
# label1.pack()
# label2=Label(root, text='flat', relief='groove')
# label2.pack()
# label3=Label(root, text='flat', relief='raised')
# label3.pack()
# label4=Label(root, text='flat', relief='ridge')
# label4.pack()
# label5=Label(root, text='flat', relief='solid')
# label5.pack()
# label6=Label(root, text='flat', relief='sunken')
# label6.pack()

#create var
status_var = StringVar()
status_var.set("初始化。")

status_label = Label(root, textvariable=status_var, bd=1, relief=SUNKEN, anchor=W)
status_label.pack(side=BOTTOM, fill=X)

def start():
    status_var.set("start")

def stop():
    status_var.set("stop")


#create buttom
button1=Button(root, text='Start',command=start)
button1.pack()
button2=Button(root,text='Stop',command=stop)
button2.pack()
statusBar= Label(root,text='processing', fg='black', bg='white' ,anchor=W,relief='sunken',bd=2)
statusBar.pack(side='bottom',fill='x')
table=ttk.Treeview(root,columns=['product name', 'Unit Price','Quantity'])
table.heading('#0', text='Product Name')
table.heading('#1', text='Unit Price')
table.heading('#2', text='Quantily')
table.heading('#3', text='Subtotal') 
table.column('#0',width=250, anchor=CENTER)
table.column('#1', anchor=CENTER)
table.column('#2', anchor=CENTER)
table.column('#3', anchor=CENTER)
table.tag_configure('totalcolor', background='#E7E2E2')
table.insert('',index='end',text='sofa', values=('20000','2','40000'))
table.pack()
root.mainloop()
