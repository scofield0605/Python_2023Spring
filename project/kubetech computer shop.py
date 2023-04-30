from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
from PIL import Image, ImageTk
root= Tk()
root.title('KubeTech Shop')
root.geometry('880x650')
pdinfo=[["超廉價chromebook","NT.4,287","0"],["Acer 平價swift5 i5/8G/512G/wi11","NT.24,900","0"],["Asus 中高階zenbook S 13 OLED AMD 7/16G/1TB\n/win11",'NT.39,999',"0"],["'Apple 16吋高階MacBook Pro M1 Pro/16G/512G'","'NT.74,900'","0"]]
def addLimit(numlabel,pricelabel):
    if int(numlabel['text'])<=0:
        numlabel['text']=int(numlabel['text'])+1
        price=int(pricelabel['text'].split('.')[1].replace(',','').strip())
        total=int(totalval.get().split('：')[1].replace('元','').strip())
        totalval.set('共消費：'+str(total+price)+' 元')
    else:
        messagebox.showwarning('show warn', "每人只能限購一台")
titleImage=Image.open('./project/img/logo_tree.png')
def add(numlabel,pricelabel,infonum1,infonum2):
    global pdinfo
    numlabel['text']=int(numlabel['text'])+1
    price=int(pricelabel['text'].split('.')[1].replace(',','').strip())
    pdinfo[infonum1][infonum2]=str(int(pdinfo[infonum1][infonum2])+1)
    print(pdinfo)
    total=int(totalval.get().split('：')[1].replace('元','').strip())
    totalval.set('共消費：'+str(total+price)+' 元')
def minus(numlabel,pricelabel,infonum1,infonum2):
    if int(numlabel['text'])>0:
        numlabel['text']=int(numlabel['text'])-1
        price=int(pricelabel['text'].split('.')[1].replace(',','').strip())
        pdinfo[infonum1][infonum2]=str(int(pdinfo[infonum1][infonum2])-1)
        total=int(totalval.get().split('：')[1].replace('元','').strip())
        totalval.set('共消費：'+str(total-price)+' 元')
    else:
        messagebox.showwarning('show warn', "The number of product can't below zero")




#詳細清單
def newwindow2():

    detailWindow = Toplevel(root)
    detailWindow.geometry('850x250')
    table = ttk.Treeview(detailWindow, columns=['Unit Price', 'Quantity', 'Subtotal'])
    table.heading('#0', text='Product Name')
    table.heading('#1', text='Unit Price')
    table.heading('#2', text='Quantity')
    table.heading('#3', text='Subtotal')
    table.column('#0', width=250, anchor=CENTER)
    table.column('#1', anchor=CENTER)
    table.column('#2', anchor=CENTER)
    table.column('#3', anchor=CENTER)
    # 建立内容,從total行是用淺藍色底
    table.tag_configure('totalcolor', background='#E7E2E2')
    subtotal1 = int(number1['text']) * int(productprice1['text'].split('.')[1].replace(',',''))
    table.insert('',index='end',text=productname1['text'],values=[productprice1['text'],number1['text'], subtotal1])
    subtotal2 = int(number2['text']) * int(productprice2['text'].split('.')[1].replace(',',''))
    table.insert('',index='end',text=productname2['text'],values=[productprice2['text'],number2['text'], subtotal2])
    subtotal3 = int(number3['text']) * int(productprice3['text'].split('.')[1].replace(',',''))
    table.insert('',index='end',text=productname3['text'],values=[productprice3['text'],number3['text'], subtotal3])
    subtotal4 = int(number4['text']) * int(productprice4['text'].split('.')[1].replace(',',''))
    table.insert('',index='end',text=productname4['text'],values=[productprice4['text'],number4['text'], subtotal4])
    total = subtotal1+subtotal2+subtotal3+subtotal4
    table.insert('',index='end',text='Total',values=['','', total], tags=('totalcolor'))
    table.pack()
    
    detailWindow.mainloop()



#筆電視窗
def createNewWindow():
    global pdinfo
    new=Toplevel(root)
    new.geometry('880x650')

    adviertise=Image.open('./project/img/339ed0a22bcb95e84a3f390a039e837b.jpg')
    adviertise=ImageTk.PhotoImage(adviertise)
    adviertiselabel=Label(new, image=adviertise,width=202,height=500)
    adviertiselabel.grid(row=0,column=0,rowspan=6,sticky=W, padx=5)
    sofa1Image1=Image.open('./project/img/1.png.webp')
    sofa1Image1=sofa1Image1.resize((202,200))
    sofa1Image1=ImageTk.PhotoImage(sofa1Image1)
    sofa1label1=Label(new, image=sofa1Image1,width=202,height=200)
    sofa1label1.grid(row=0,column=2,columnspan=2,sticky=W, padx=5)

    sofa2Image1=Image.open('./project/img/seahorse-02.png')
    sofa2Image1=sofa2Image1.resize((210,210))
    sofa2Image1=ImageTk.PhotoImage(sofa2Image1)
    sofa2label1=Label(new, image=sofa2Image1,width=202,height=200)
    sofa2label1.grid(row=0,column=4,columnspan=2,sticky=W, padx=5)

    sofa3Image1=Image.open('./project/img/Screenshot 2022-12-17 at 14.39.23.png')
    sofa3Image1=sofa3Image1.resize((202,200))
    sofa3Image1=ImageTk.PhotoImage(sofa3Image1)
    sofa3label1=Label(new, image=sofa3Image1,width=202,height=200)
    sofa3label1.grid(row=2,column=6,columnspan=2,sticky=W, padx=5)

    sofa4Image1=Image.open('./project/img/mbp16-spacegray-select-202110_GEO_TW.jpeg')
    sofa4Image1=sofa4Image1.resize((202,200))
    sofa4Image1=ImageTk.PhotoImage(sofa4Image1)
    sofa4label1=Label(new, image=sofa4Image1,width=202,height=200)
    sofa4label1.grid(row=4,column=7,columnspan=2,sticky=W, padx=5)

    productname11=Label(new, text=(pdinfo[0][0]), font=('Inter',11))
    productname21=Label(new, text=(pdinfo[1][0]), font=('Inter',11))
    productname31=Label(new, text=(pdinfo[2][0]), font=('Inter',11))
    productname41=Label(new, text=(pdinfo[3][0]), font=('Inter',11))
    productname11.grid(row=1,column=2,columnspan=2,sticky=W, padx=5)
    productname21.grid(row=1,column=4,columnspan=2,sticky=W, padx=5)
    productname31.grid(row=3,column=4,columnspan=2,sticky=W, padx=5)
    productname41.grid(row=5,column=6,columnspan=2,sticky=W, padx=5)

    productprice11=Label(new, text=(pdinfo[0][1]), font=('Inter',11))
    productprice21=Label(new, text=(pdinfo[1][1]), font=('Inter',11))
    productprice31=Label(new, text=(pdinfo[2][1]), font=('Inter',11))
    productprice41=Label(new, text=(pdinfo[3][1]), font=('Inter',11))
    productprice11.grid(row=2,column=2,sticky=W)
    productprice21.grid(row=2,column=4,sticky=W)
    productprice31.grid(row=4,column=4,sticky=W)
    productprice41.grid(row=6,column=6,sticky=W)


    minusbutton11=Button(new,text='-',font=('Inter',10),command=lambda: minus(number11,productprice11),)
    number11=Label(new,text='0',font=('Inter',12))
    addbutton11=Button(new,text='+',font=('Inter',10),command=lambda: add(number11,productprice11))

    minusbutton21=Button(new,text='-',font=('Inter',10),command=lambda: minus(number21,productprice21))
    number21=Label(new,text='0',font=('Inter',12))
    addbutton21=Button(new,text='+',font=('Inter',10),command=lambda: add(number21,productprice21))

    minusbutton31=Button(new,text='-',font=('Inter',10),command=lambda: minus(number31,productprice31))
    number31=Label(new,text='0',font=('Inter',12))
    addbutton31=Button(new,text='+',font=('Inter',10),command=lambda: add(number31,productprice31))

    minusbutton41=Button(new,text='-',font=('Inter',10),command=lambda: minus(number41,productprice41))
    number41=Label(new,text='0',font=('Inter',12))
    addbutton41=Button(new,text='+',font=('Inter',10),command=lambda: add(number41,productprice41))

    minusbutton11.grid(row=2,column=3,sticky=W)
    number11.grid(row=2,column=3)
    addbutton11.grid(row=2,column=3,sticky=E)

    minusbutton21.grid(row=2,column=5,sticky=W)
    number21.grid(row=2,column=5)
    addbutton21.grid(row=2,column=5,sticky=E)

    minusbutton31.grid(row=4,column=5,sticky=W)
    number31.grid(row=4,column=5,)
    addbutton31.grid(row=4,column=5,sticky=E)

    minusbutton41.grid(row=6,column=7,sticky=W)
    number41.grid(row=6,column=7)
    addbutton41.grid(row=6,column=7,sticky=E)
    new.rowconfigure(5,weight=2)
    detailbtn2=Button(new,text='詳細清單',font=('Inter',18))
    detailbtn2.grid(row=7,column=0,sticky=W+S,padx=5,pady=1)
    chartImage2=Image.open('./project/img/Shopping Cart.png')
    chartimage2=chartImage2.resize((32,32))
    chartImage2=ImageTk.PhotoImage(chartimage2)
    chartlabel2=Label(new, image=chartImage2,width=32,height=32)
    chartlabel2.grid(row=7,column=5,sticky=W)
    # totalval2=StringVar()
    # totalval2.set('共消費：0元')
    totallabel2=Label(new, textvariable=totalval,font=('Inter',18),fg='#000000')
    totallabel2.grid(row=7,column=6,columnspan=2,sticky=W+S)
    checkout2=Button(new,text='結帳',font=('Inter',18))
    checkout2.grid(row=7,column=7,columnspan=2,sticky=E+S)
    new.mainloop()



#card
def thenew():
    new1=Toplevel(root)
    new1.geometry('880x650')
    sofa2=Button(new1, text='主機',width=5,pady=2, font=('Inter',18))
    bed2=Button(new1, text='筆電',width=5,pady=2,font=('Inter',18))
    kit2=Button(new1, text='顯卡',width=5,pady=2,font=('Inter',18))
    member2=Button(new1,text='會員登入',width=12,pady=2,font=('Inter',18))
    sofa2.grid(row=0,column=1,sticky=W)
    bed2.grid(row=0,column=2,sticky=W)
    kit2.grid(row=0,column=3,sticky=E+W)
    member2.grid(row=0,column=7,sticky=E+W, padx=5)
    bannerImage2=Image.open('./project/img/Orange Modern Special Offer Big Sale Facebook Ad.png')
    bannerImage2=bannerImage2.resize((852,298))
    bannerImage2=ImageTk.PhotoImage(bannerImage2)
    bannerlabel2=Label(new1, image=bannerImage2,width=852,height=298)
    bannerlabel2.grid(row=1,column=0,columnspan=8,padx=5)

    sofa1Image2=Image.open('./project/img/Screenshot 2022-12-17 at 15.10.05.png')
    sofa1Image2=sofa1Image2.resize((202,200))
    sofa1Image2=ImageTk.PhotoImage(sofa1Image2)
    sofa1label2=Label(new1, image=sofa1Image2,width=202,height=200)
    sofa1label2.grid(row=2,column=0,columnspan=2,sticky=W, padx=5)

    sofa2Image2=Image.open('./project/img/Screenshot 2022-12-17 at 15.11.00.png')
    sofa2Image2=sofa2Image2.resize((202,200))
    sofa2Image2=ImageTk.PhotoImage(sofa2Image2)
    sofa2label2=Label(new1, image=sofa2Image2,width=202,height=200)
    sofa2label2.grid(row=2,column=2,columnspan=2,sticky=W, padx=5)

    sofa3Image2=Image.open('./project/img/Screenshot 2022-12-17 at 15.11.38.png')
    sofa3Image2=sofa3Image2.resize((202,200))
    sofa3Image2=ImageTk.PhotoImage(sofa3Image2)
    sofa3label2=Label(new1, image=sofa3Image2,width=202,height=200)
    sofa3label2.grid(row=2,column=4,columnspan=2,sticky=W, padx=5)

    sofa4Image2=Image.open('./project/img/Screenshot 2022-12-17 at 15.12.49.png')
    sofa4Image2=sofa4Image2.resize((202,200))
    sofa4Image2=ImageTk.PhotoImage(sofa4Image2)
    sofa4label2=Label(new1, image=sofa4Image2,width=202,height=200)
    sofa4label2.grid(row=2,column=6,columnspan=2,sticky=W, padx=5)

    productname22=Label(new1, text='Intel 初階內顯 i5/6CPU', font=('Inter',11))
    productname32=Label(new1, text='AMD 中階Ryzen 5 3400G/4CPU8Threads', font=('Inter',11))
    productname12=Label(new1, text='NVIDIA 中高階GTX1660s', font=('Inter',11))
    productname42=Label(new1, text='NVIDIA 高階RTX3090 SUPRIM X 24G', font=('Inter',11))
    productname12.grid(row=3,column=0,columnspan=2,sticky=W, padx=5)
    productname22.grid(row=3,column=2,columnspan=2,sticky=W, padx=5)
    productname32.grid(row=3,column=4,columnspan=2,sticky=W, padx=5)
    productname42.grid(row=3,column=6,columnspan=2,sticky=W, padx=5)

    productprice12=Label(new1, text='NT.5,880', font=('Inter',11))
    productprice22=Label(new1, text='NT.5,890', font=('Inter',11))
    productprice32=Label(new1, text='NT.6,999', font=('Inter',11))
    productprice42=Label(new1, text='NT.36,990', font=('Inter',11))
    productprice12.grid(row=4,column=0,sticky=W)
    productprice22.grid(row=4,column=2,sticky=W)
    productprice32.grid(row=4,column=4,sticky=W)
    productprice42.grid(row=4,column=6,sticky=W)

    minusbutton12=Button(new1,text='-',font=('Inter',10),command=lambda: minus(number12,productprice12))
    number12=Label(new1,text='0',font=('Inter',12))
    addbutton12=Button(new1,text='+',font=('Inter',10),command=lambda: add(number12,productprice12))

    minusbutton22=Button(new1,text='-',font=('Inter',10),command=lambda: minus(number22,productprice22))
    number22=Label(new1,text='0',font=('Inter',12))
    addbutton22=Button(new1,text='+',font=('Inter',10),command=lambda: add(number22,productprice22))

    minusbutton32=Button(new1,text='-',font=('Inter',10),command=lambda: minus(number32,productprice32))
    number32=Label(new1,text='0',font=('Inter',12))
    addbutton32=Button(new1,text='+',font=('Inter',10),command=lambda: add(number32,productprice32))

    minusbutton42=Button(new1,text='-',font=('Inter',10),command=lambda: minus(number42,productprice42))
    number42=Label(new1,text='0',font=('Inter',12))
    addbutton42=Button(new1,text='+',font=('Inter',10),command=lambda: add(number42,productprice42))

    minusbutton12.grid(row=4,column=1,sticky=W)
    number12.grid(row=4,column=1)
    addbutton12.grid(row=4,column=1,sticky=E)

    minusbutton22.grid(row=4,column=3,sticky=W)
    number22.grid(row=4,column=3)
    addbutton22.grid(row=4,column=3,sticky=E)

    minusbutton32.grid(row=4,column=5,sticky=W)
    number32.grid(row=4,column=5)
    addbutton32.grid(row=4,column=5,sticky=E)

    minusbutton42.grid(row=4,column=7,sticky=W)
    number42.grid(row=4,column=7)
    addbutton42.grid(row=4,column=7,sticky=E)
    new1.rowconfigure(5,weight=2)
    detailbtn1=Button(new1,text='詳細清單',font=('Inter',18))
    detailbtn1.grid(row=5,column=0,sticky=W+S,padx=5,pady=1)
    chartImage1=Image.open('./project/img/Shopping Cart.png')
    chartimage1=chartImage1.resize((32,32))
    chartImage1=ImageTk.PhotoImage(chartimage1)
    chartlabel1=Label(new1, image=chartImage1,width=32,height=32)
    chartlabel1.grid(row=5,column=5,sticky=W)
    totalval1=StringVar()
    totalval1.set('共消費：0元')
    totallabel1=Label(new1, textvariable=totalval,font=('Inter',18),fg='#000000')
    totallabel1.grid(row=5,column=6,columnspan=2,sticky=W+S)
    checkout1=Button(new1,text='結帳',font=('Inter',18))
    checkout1.grid(row=5,column=7,columnspan=2,sticky=E+S)
    new1.mainloop()


titleImage=Image.open('./project/img/logo_tree.png')
resized_image=titleImage.resize((32,32))
titleImage=ImageTk.PhotoImage(resized_image)
titlelabel=Label(root, image=titleImage,width=32,height=32)
titlelabel.grid(row=0,column=0,sticky=W)

bannerImage=Image.open('./project/img/Orange Modern Special Offer Big Sale Facebook Ad.png')
bannerImage=bannerImage.resize((852,298))
bannerImage=ImageTk.PhotoImage(bannerImage)
bannerlabel=Label(root, image=bannerImage,width=852,height=298)
bannerlabel.grid(row=1,column=0,columnspan=8,padx=5)

sofa1Image=Image.open('./project/img/Screenshot 2022-12-17 at 13.04.27.png')
sofa1Image=sofa1Image.resize((202,200))
sofa1Image=ImageTk.PhotoImage(sofa1Image)
sofa1label=Label(root, image=sofa1Image,width=202,height=200)
sofa1label.grid(row=2,column=0,columnspan=2,sticky=W, padx=5)

sofa2Image=Image.open('./project/img/Screenshot 2022-12-17 at 12.54.20.png')
sofa2Image=sofa2Image.resize((202,200))
sofa2Image=ImageTk.PhotoImage(sofa2Image)
sofa2label=Label(root, image=sofa2Image,width=202,height=200)
sofa2label.grid(row=2,column=2,columnspan=2,sticky=W, padx=5)

sofa3Image=Image.open('./project/img/Screenshot 2022-12-17 at 13.08.00.png')
sofa3Image=sofa3Image.resize((202,200))
sofa3Image=ImageTk.PhotoImage(sofa3Image)
sofa3label=Label(root, image=sofa3Image,width=202,height=200)
sofa3label.grid(row=2,column=4,columnspan=2,sticky=W, padx=5)

sofa4Image=Image.open('./project/img/Screenshot 2022-12-17 at 13.13.35.png')
sofa4Image=sofa4Image.resize((202,200))
sofa4Image=ImageTk.PhotoImage(sofa4Image)
sofa4label=Label(root, image=sofa4Image,width=202,height=200)
sofa4label.grid(row=2,column=6,columnspan=2,sticky=W, padx=5)

bed=Button(root, text='筆電',width=5,pady=2,font=('Inter',18),command=createNewWindow)
sofa=Button(root, text='主機',width=5,pady=2, font=('Inter',18))
kit=Button(root, text='顯卡',width=5,pady=2,font=('Inter',18),command=thenew)
member=Button(root,text='會員登入',width=12,pady=2,font=('Inter',18))

productname1=Label(root, text='超老iMac', font=('Inter',11))
productname2=Label(root, text='Acer 廉價桌機 Intel i3/8G/256G/win11', font=('Inter',11))
productname3=Label(root, text='MSI 中階電競桌機 Intel i5/8G/512G/win11\n RTX2060-6G', font=('Inter',11))
productname4=Label(root, text='ROG 高階電競桌機 Intel i9/16G/1TBwin11\n RTX3090-24G', font=('Inter',11))
productname1.grid(row=3,column=0,columnspan=2,sticky=W, padx=5)
productname2.grid(row=3,column=2,columnspan=2,sticky=W, padx=5)
productname3.grid(row=3,column=4,columnspan=2,sticky=W, padx=5)
productname4.grid(row=3,column=6,columnspan=2,sticky=W, padx=5)
sofa.grid(row=0,column=1,sticky=W)
bed.grid(row=0,column=2,sticky=W)
kit.grid(row=0,column=3,sticky=E+W)
member.grid(row=0,column=7,sticky=E+W, padx=5)
productprice1=Label(root, text='NT.4000', font=('Inter',11))
productprice2=Label(root, text='NT.14,900', font=('Inter',11))
productprice3=Label(root, text='NT.28,900', font=('Inter',11))
productprice4=Label(root, text='NT.69,900', font=('Inter',11))
productprice1.grid(row=4,column=0,sticky=W)
productprice2.grid(row=4,column=2,sticky=W)
productprice3.grid(row=4,column=4,sticky=W)
productprice4.grid(row=4,column=6,sticky=W)


minusbutton1=Button(root,text='-',font=('Inter',10),command=lambda: minus(number1,productprice1))
number1=Label(root,text='0',font=('Inter',12))
addbutton1=Button(root,text='+',font=('Inter',10),command=lambda: add(number1,productprice1))

minusbutton2=Button(root,text='-',font=('Inter',10),command=lambda: minus(number2,productprice2))
number2=Label(root,text='0',font=('Inter',12))
addbutton2=Button(root,text='+',font=('Inter',10),command=lambda: add(number2,productprice2))

minusbutton3=Button(root,text='-',font=('Inter',10),command=lambda: minus(number3,productprice3))
number3=Label(root,text='0',font=('Inter',12))
addbutton3=Button(root,text='+',font=('Inter',10),command=lambda: add(number3,productprice3))

minusbutton4=Button(root,text='-',font=('Inter',10),command=lambda: minus(number4,productprice4))
number4=Label(root,text='0',font=('Inter',12))
addbutton4=Button(root,text='+',font=('Inter',10),command=lambda: addLimit(number4,productprice4))

minusbutton1.grid(row=4,column=1,sticky=W)
number1.grid(row=4,column=1)
addbutton1.grid(row=4,column=1,sticky=E)

minusbutton2.grid(row=4,column=3,sticky=W)
number2.grid(row=4,column=3)
addbutton2.grid(row=4,column=3,sticky=E)

minusbutton3.grid(row=4,column=5,sticky=W)
number3.grid(row=4,column=5)
addbutton3.grid(row=4,column=5,sticky=E)

minusbutton4.grid(row=4,column=7,sticky=W)
number4.grid(row=4,column=7)
addbutton4.grid(row=4,column=7,sticky=E)


root.rowconfigure(5,weight=2)
detailbtn=Button(root,text='詳細清單',font=('Inter',18), command=newwindow2)
detailbtn.grid(row=5,column=0,sticky=W+S,padx=5,pady=1)
chartImage=Image.open('./project/img/Shopping Cart.png')
chartimage=chartImage.resize((32,32))
chartImage=ImageTk.PhotoImage(chartimage)
chartlabel=Label(root, image=chartImage,width=32,height=32)
chartlabel.grid(row=5,column=5,sticky=W)
totalval=StringVar()
totalval.set('共消費：0元')
totallabel=Label(root, textvariable=totalval,font=('Inter',18),fg='#000000')
totallabel.grid(row=5,column=6,columnspan=2,sticky=W+S)
checkout=Button(root,text='結帳',font=('Inter',18))
checkout.grid(row=5,column=7,columnspan=2,sticky=E+S) 



root.mainloop()


