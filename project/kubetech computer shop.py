from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import qrcode
from email.mime.image import MIMEImage
#引入MUltipart
from email.mime.multipart import MIMEMultipart
from pathlib import Path
from email.mime.text import MIMEText
#Python專案中的電子郵件內容完成後，接下來就要設定Gmail的SMTP伺服器來寄送
import smtplib
from PIL import Image, ImageTk
# 開啟圖片

#如果想要在電子郵件中加人圖片，則需在Python專案中引用MIMEImage類別，並且引用pathlib函式庫來讀取圖片
root= Tk()
root.title('KubeTech Shop')
root.geometry('890x650')
img = Image.open('project/img/logo_tree.png')
tk_img = ImageTk.PhotoImage(img)
root.iconphoto(True,tk_img)
userinfo2=["",""]
pdinfo=[['超老iMac',"NT.4000","0"],["Acer 廉價桌機 Intel i3/8G/256G/win11","NT.14,900","0"],["MSI 中階電競桌機 Intel i5/8G/512G/win11\n RTX2060-6G",'NT.28,900',"0"],["ROG 高階電競桌機 Intel i9/16G/1TBwin11\n RTX3090-24G","NT.69,900","0"],['chromebook',"NT.1000",'0'],['acer',"NT.30,000",'0'],['asus高階',"NT.54,000",'0'],['apple MacBook Pro 16',"NT.72,000",'0'],[' Intel 初階內顯 i5/6CPU',"NT.5,880",'0'],['AMD 中階Ryzen 5 3400G/4CPU8Threads',"NT.5,890",'0'],['NVIDIA 中高階GTX1660s','NT.6,999','0'],['NVIDIA 高階RTX3090 SUPRIM X 24G','NT.36,990','0']]
def addLimit(numlabel,pricelabel,infonum1,infonum2):
    if int(numlabel['text'])<=0:
        global pdinfo
        numlabel['text']=int(numlabel['text'])+1
        price=int(pricelabel['text'].split('.')[1].replace(',','').strip())
        pdinfo[infonum1][infonum2]=str(int(pdinfo[infonum1][infonum2])+1)
        print(pdinfo)
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

def login():
    def check(passEmail,passPassword):
        userinfo2[0] = passEmail
        userinfo2[1] = passPassword
        print(userinfo2)
    loginwindow= Toplevel(root)
    loginwindow.geometry('200x250')
    emailname=Label(loginwindow, text='enter email')
    emailname.grid(row=0, column=0)
    email=Entry(loginwindow)
    email.grid(row=1, column=0)
    passwordname=Label(loginwindow, text='enter password')
    passwordname.grid(row=2,column=0)
    password=Entry(loginwindow,)
    password.grid(row=3,column=0)
    confirm=Button(loginwindow, text="CONFIRM",command=lambda:check(passEmail=email.get(),passPassword=password.get()))
    confirm.grid(row=4,column=0) 
    loginwindow.mainloop()



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
    subtotal0 = int(pdinfo[0][2]) * int(pdinfo[0][1].split('.')[1].replace(',',''))
    table.insert('',index='end',text=pdinfo[0][0],values=[pdinfo[0][1],pdinfo[0][2], subtotal0])
    subtotal1 = int(pdinfo[1][2]) * int(pdinfo[1][1].split('.')[1].replace(',',''))
    table.insert('',index='end',text=pdinfo[1][0],values=[pdinfo[1][1],pdinfo[1][2], subtotal1])
    subtotal2 = int(pdinfo[2][2]) * int(pdinfo[2][1].split('.')[1].replace(',',''))
    table.insert('',index='end',text=pdinfo[2][0],values=[pdinfo[2][1],pdinfo[2][2], subtotal2])
    subtotal3 = int(pdinfo[3][2]) * int(pdinfo[3][1].split('.')[1].replace(',',''))
    table.insert('',index='end',text=pdinfo[3][0],values=[pdinfo[3][1],pdinfo[3][2], subtotal3])
    subtotal4 = int(pdinfo[4][2]) * int(pdinfo[4][1].split('.')[1].replace(',',''))
    table.insert('',index='end',text=pdinfo[4][0],values=[pdinfo[4][1],pdinfo[4][2], subtotal4])
    subtotal5 = int(pdinfo[5][2]) * int(pdinfo[5][1].split('.')[1].replace(',',''))
    table.insert('',index='end',text=pdinfo[5][0],values=[pdinfo[5][1],pdinfo[5][2], subtotal5])
    subtotal6 = int(pdinfo[6][2]) * int(pdinfo[6][1].split('.')[1].replace(',',''))
    table.insert('',index='end',text=pdinfo[6][0],values=[pdinfo[6][1],pdinfo[6][2], subtotal6])
    subtotal7 = int(pdinfo[7][2]) * int(pdinfo[7][1].split('.')[1].replace(',',''))
    table.insert('',index='end',text=pdinfo[7][0],values=[pdinfo[7][1],pdinfo[7][2], subtotal7])
    subtotal8 = int(pdinfo[8][2]) * int(pdinfo[8][1].split('.')[1].replace(',',''))
    table.insert('',index='end',text=pdinfo[8][0],values=[pdinfo[8][1],pdinfo[8][2], subtotal8])
    subtotal9 = int(pdinfo[9][2]) * int(pdinfo[9][1].split('.')[1].replace(',',''))
    table.insert('',index='end',text=pdinfo[9][0],values=[pdinfo[9][1],pdinfo[9][2], subtotal9])
    subtotal10 = int(pdinfo[10][2]) * int(pdinfo[10][1].split('.')[1].replace(',',''))
    table.insert('',index='end',text=pdinfo[10][0],values=[pdinfo[10][1],pdinfo[10][2], subtotal10])
    subtotal11 = int(pdinfo[11][2]) * int(pdinfo[11][1].split('.')[1].replace(',',''))
    table.insert('',index='end',text=pdinfo[11][0],values=[pdinfo[11][1],pdinfo[11][2], subtotal11])

    total = subtotal0+subtotal1+subtotal2+subtotal3+subtotal4+subtotal5+subtotal6+subtotal7+subtotal8+subtotal9+subtotal10+subtotal11
    table.insert('',index='end',text='Total',values=['','', total], tags=('totalcolor'))
    table.pack()
    
    detailWindow.mainloop()



#筆電視窗
def createNewWindow():
    global pdinfo
    new=Toplevel(root)
    new.geometry('880x650')

    adviertise2=Image.open('project/img/截圖 2023-05-14 10.18.03.png')
    adviertise2=adviertise2.resize((202,500))
    adviertise2=ImageTk.PhotoImage(adviertise2)
    adviertiselabel2=Label(new, image=adviertise2,width=202,height=500)
    adviertiselabel2.grid(row=0,column=7,rowspan=6,sticky=W, padx=5)

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
    sofa3label1.grid(row=4,column=2,columnspan=2,sticky=W, padx=5)

    sofa4Image1=Image.open('./project/img/mbp16-spacegray-select-202110_GEO_TW.jpeg')
    sofa4Image1=sofa4Image1.resize((202,200))
    sofa4Image1=ImageTk.PhotoImage(sofa4Image1)
    sofa4label1=Label(new, image=sofa4Image1,width=202,height=200)
    sofa4label1.grid(row=4,column=4,columnspan=2,sticky=W, padx=5)

    productname11=Label(new, text=(pdinfo[4][0]), font=('Inter',11))
    productname21=Label(new, text=(pdinfo[5][0]), font=('Inter',11))
    productname31=Label(new, text=(pdinfo[6][0]), font=('Inter',11))
    productname41=Label(new, text=(pdinfo[7][0]), font=('Inter',11))
    productname11.grid(row=1,column=2,columnspan=2,sticky=W, padx=5)
    productname21.grid(row=1,column=4,columnspan=2,sticky=W, padx=5)
    productname31.grid(row=5,column=2,columnspan=2,sticky=W, padx=5)
    productname41.grid(row=5,column=4,columnspan=2,sticky=W, padx=5)

    productprice11=Label(new, text=(pdinfo[4][1]), font=('Inter',11))
    productprice21=Label(new, text=(pdinfo[5][1]), font=('Inter',11))
    productprice31=Label(new, text=(pdinfo[6][1]), font=('Inter',11))
    productprice41=Label(new, text=(pdinfo[7][1]), font=('Inter',11))
    productprice11.grid(row=2,column=2,sticky=W)
    productprice21.grid(row=2,column=4,sticky=W)
    productprice31.grid(row=6,column=2,sticky=W)
    productprice41.grid(row=6,column=4,sticky=W)


    minusbutton11=Button(new,text='-',font=('Inter',10),command=lambda: minus(number11,productprice11,4,2))
    number11=Label(new,text='0',font=('Inter',12))
    addbutton11=Button(new,text='+',font=('Inter',10),command=lambda: add(number11,productprice11,4,2))

    minusbutton21=Button(new,text='-',font=('Inter',10),command=lambda: minus(number21,productprice21,5,2))
    number21=Label(new,text='0',font=('Inter',12))
    addbutton21=Button(new,text='+',font=('Inter',10),command=lambda: add(number21,productprice21,5,2))

    minusbutton31=Button(new,text='-',font=('Inter',10),command=lambda: minus(number31,productprice31,6,2))
    number31=Label(new,text='0',font=('Inter',12))
    addbutton31=Button(new,text='+',font=('Inter',10),command=lambda: add(number31,productprice31,6,2))

    minusbutton41=Button(new,text='-',font=('Inter',10),command=lambda: minus(number41,productprice41,7,2))
    number41=Label(new,text='0',font=('Inter',12))
    addbutton41=Button(new,text='+',font=('Inter',10),command=lambda: add(number41,productprice41,7,2))

    minusbutton11.grid(row=2,column=3,sticky=W)
    number11.grid(row=2,column=3)
    addbutton11.grid(row=2,column=3,sticky=E)

    minusbutton21.grid(row=2,column=5,sticky=W)
    number21.grid(row=2,column=5)
    addbutton21.grid(row=2,column=5,sticky=E)

    minusbutton31.grid(row=6,column=3,sticky=W)
    number31.grid(row=6,column=3)
    addbutton31.grid(row=6,column=3,sticky=E)

    minusbutton41.grid(row=6,column=5,sticky=W)
    number41.grid(row=6,column=5)
    addbutton41.grid(row=6,column=5,sticky=E)
    new.rowconfigure(5,weight=2)

    # totalval2.set('共消費：0元')
    totallabel2=Label(new, textvariable=totalval,font=('Inter',18),fg='#000000')
    totallabel2.grid(row=7,column=6,columnspan=2,sticky=W+S)
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

    productname22=Label(new1, text=(pdinfo[8][0]), font=('Inter',11))
    productname32=Label(new1, text=(pdinfo[9][0]), font=('Inter',11))
    productname12=Label(new1, text=(pdinfo[10][0]), font=('Inter',11))
    productname42=Label(new1, text=(pdinfo[11][0]), font=('Inter',11))
    productname12.grid(row=3,column=0,columnspan=2,sticky=W, padx=5)
    productname22.grid(row=3,column=2,columnspan=2,sticky=W, padx=5)
    productname32.grid(row=3,column=4,columnspan=2,sticky=W, padx=5)
    productname42.grid(row=3,column=6,columnspan=2,sticky=W, padx=5)

    productprice12=Label(new1, text=(pdinfo[8][1]), font=('Inter',11))
    productprice22=Label(new1, text=(pdinfo[9][1]), font=('Inter',11))
    productprice32=Label(new1, text=(pdinfo[10][1]), font=('Inter',11))
    productprice42=Label(new1, text=(pdinfo[11][1]), font=('Inter',11))
    productprice12.grid(row=4,column=0,sticky=W)
    productprice22.grid(row=4,column=2,sticky=W)
    productprice32.grid(row=4,column=4,sticky=W)
    productprice42.grid(row=4,column=6,sticky=W)

    minusbutton12=Button(new1,text='-',font=('Inter',10),command=lambda: minus(number12,productprice12,8,2))
    number12=Label(new1,text='0',font=('Inter',12))
    addbutton12=Button(new1,text='+',font=('Inter',10),command=lambda: add(number12,productprice12,8,2))

    minusbutton22=Button(new1,text='-',font=('Inter',10),command=lambda: minus(number22,productprice22,9,2))
    number22=Label(new1,text='0',font=('Inter',12))
    addbutton22=Button(new1,text='+',font=('Inter',10),command=lambda: add(number22,productprice22,9,2))

    minusbutton32=Button(new1,text='-',font=('Inter',10),command=lambda: minus(number32,productprice32,10,2))
    number32=Label(new1,text='0',font=('Inter',12))
    addbutton32=Button(new1,text='+',font=('Inter',10),command=lambda: add(number32,productprice32,10,2))

    minusbutton42=Button(new1,text='-',font=('Inter',10),command=lambda: minus(number42,productprice42,11,2))
    number42=Label(new1,text='0',font=('Inter',12))
    addbutton42=Button(new1,text='+',font=('Inter',10),command=lambda: add(number42,productprice42,11,2))

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

#結帳
def pay():
    def emailcode():
        sum = 0
        content = "----------------------------\n"
        for i in pdinfo:
            sum = sum+int(i[2]) * int(i[1].split('.')[1].replace(',',''))
            if i[2] == '0':
                continue
            else:
                for j in i:
                    content = content+ str(j) + "\n"
                content = content
                content = content + "----------------------------\n"
        content = content + "============================\n總金額:"+str(sum)

        print(content)
        temp = '您已完成付款\n'+content
        text=MIMEText(temp)

        image=MIMEImage(Path('/Users/scofield/Documents/Python_2023Spring/giganigga.jpg').read_bytes())
        content=MIMEMultipart()
        content['subject']='2023 Pthon App 春季班DEmo'
        content['from']='scofieldtsai@gmail.com'
        content['to']=userinfo2[0]

        content.attach(text)
        content.attach(image)

        smtp=smtplib.SMTP(host='smtp.gmail.com', port='587')

        f=open('class5/password.txt','r')
        mailToken=f.read()
        f.close()

        #利用 with 來自動釋放資源
        with open('class5/password.txt','r')  as f:
            mailToken=f.read()


        with smtp:#利用 with 來白動釋放資源
            try:
                smtp.ehlo() #驗證SMTP伺服器
                smtp.starttls() #建立加密傳輸
                smtp.login("scofieldtsai@gmail.com", mailToken)
                smtp.send_message ( content) #寄送郵件
                print ("Email is Sended completely!")
                smtp.quit ()
            except Exception as e:
                print ("Error message: ", e)

    def cardpaypage():
        cardpay=Toplevel(paypage)
        cardpay.geometry('300x400')
        cardEntry=Entry(cardpay,text='輸入卡號',font=('Inter',18))
        cardEntry.grid(row=0,column=0)
        cardEnter=Button(cardpay,text='確認付款',font=('Inter',18),command=emailcode)
        cardEnter.grid(row=1,column=0)
        cardpay.mainloop()
    def linepaypage():
        sum = 0
        global pdinfo
        line=Toplevel(paypage)
        line.geometry('500x500')
        # 製作qrcode 
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2
        )
        content = "----------------------------\n"
        for i in pdinfo:
            sum = sum+int(i[2]) * int(i[1].split('.')[1].replace(',',''))
            if i[2] == '0':
                continue
            else:
                for j in i:
                    content = content+ str(j) + "\n"
                content = content
                content = content + "----------------------------\n"
        content = content + "============================\n總金額:"+str(sum)
        print(content)

        qr.add_data(content)
        qr.make(fit=True) # 將參數塞進物件中，根據參數製作為 QRCode 物件
        img = qr.make_image(fill_color="yellow", back_color="black") # 產生 QRCode 圖片
        img.save('project/img/qrcode.png')
        lineimage=Image.open('project/img/qrcode.png')
        resized_image1=lineimage.resize((500,500))
        lineimage=ImageTk.PhotoImage(resized_image1)
        linelabel=Label(line, image=lineimage,width=500,height=500)
        linelabel.grid(row=0,column=0)
        line.mainloop()

    paypage=Toplevel(root)
    paypage.geometry('200x300')
    card=Button(paypage, text='刷卡',width=5,pady=2,font=('Inter',18),command=cardpaypage)
    card.grid(row=5,column=4)
    linePay=Button(paypage, text='line pay',width=5,pady=2,font=('Inter',18), command=linepaypage)
    linePay.grid(row=4,column=4)

    paypage.mainloop()


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
member=Button(root,text='會員登入',width=12,pady=2,font=('Inter',18),command=login)

productname1=Label(root, text=(pdinfo[0][0]), font=('Inter',11))
productname2=Label(root, text=(pdinfo[1][0]), font=('Inter',11))
productname3=Label(root, text=(pdinfo[2][0]), font=('Inter',11))
productname4=Label(root, text=(pdinfo[3][0]), font=('Inter',11))
productname1.grid(row=3,column=0,columnspan=2,sticky=W, padx=5)
productname2.grid(row=3,column=2,columnspan=2,sticky=W, padx=5)
productname3.grid(row=3,column=4,columnspan=2,sticky=W, padx=5)
productname4.grid(row=3,column=6,columnspan=2,sticky=W, padx=5)
sofa.grid(row=0,column=1,sticky=W)
bed.grid(row=0,column=2,sticky=W)
kit.grid(row=0,column=3,sticky=E+W)
member.grid(row=0,column=7,sticky=E+W, padx=5)
productprice1=Label(root, text=(pdinfo[0][1]), font=('Inter',11))
productprice2=Label(root, text=(pdinfo[1][1]), font=('Inter',11))
productprice3=Label(root, text=(pdinfo[2][1]), font=('Inter',11))
productprice4=Label(root, text=(pdinfo[3][1]), font=('Inter',11))
productprice1.grid(row=4,column=0,sticky=W)
productprice2.grid(row=4,column=2,sticky=W)
productprice3.grid(row=4,column=4,sticky=W)
productprice4.grid(row=4,column=6,sticky=W)


minusbutton1=Button(root,text='-',font=('Inter',10),command=lambda: minus(number1,productprice1,0,2))
number1=Label(root,text='0',font=('Inter',12))
addbutton1=Button(root,text='+',font=('Inter',10),command=lambda: add(number1,productprice1,0,2))

minusbutton2=Button(root,text='-',font=('Inter',10),command=lambda: minus(number2,productprice2,1,2))
number2=Label(root,text='0',font=('Inter',12))
addbutton2=Button(root,text='+',font=('Inter',10),command=lambda: add(number2,productprice2,1,2))

minusbutton3=Button(root,text='-',font=('Inter',10),command=lambda: minus(number3,productprice3,2,2))
number3=Label(root,text='0',font=('Inter',12))
addbutton3=Button(root,text='+',font=('Inter',10),command=lambda: add(number3,productprice3,2,2))

minusbutton4=Button(root,text='-',font=('Inter',10),command=lambda: minus(number4,productprice4,3,2))
number4=Label(root,text='0',font=('Inter',12))
addbutton4=Button(root,text='+',font=('Inter',10),command=lambda: addLimit(number4,productprice4,3,2))

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
checkout=Button(root,text='結帳',font=('Inter',18),command=pay)
checkout.grid(row=5,column=7,columnspan=2,sticky=E+S) 


root.mainloop()





