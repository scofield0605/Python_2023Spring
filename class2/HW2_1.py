from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.ttk as ttk
root= Tk()
root.title('午餐系統')
root.geometry('300x100')


def show():
    text = (checkbtnVal1.get())+" "+(checkbtnVal2.get())+" "+(checkbtnVal3.get())+" "+(checkbtnVal4.get())+" "+(checkbtnVal5.get())+" "+(checkbtnVal6.get())
    statusBar2["text"]=text
# 宣告3個用於Radio Btn的文字變數
checkbtnVal1 = StringVar()
checkbtnVal2 = StringVar()
checkbtnVal3 = StringVar()
checkbtnVal4 = StringVar()
checkbtnVal5 = StringVar()
checkbtnVal6 = StringVar()
# 建立標題Label
title2label = Label(root, text='主餐:')
title2label.grid(row=0,column=0, sticky=W)
# 放入第一個單選按鈕
checkbtn1 = Checkbutton(root, text='和牛',variable=checkbtnVal1, onvalue="和牛", offvalue="", fg='black', command=show)
checkbtn1.grid(row=1,column=0, sticky=W)
# 放入第二個單選按鈕
checkbtn2 = Checkbutton(root, text='伊比利豬',variable=checkbtnVal2, onvalue="伊比利豬", offvalue="", fg='black', command=show)
checkbtn2.grid(row=1,column=1, sticky=W)
# 放入第三個單選按鈕
checkbtn3 = Checkbutton(root, text='海鮮',variable=checkbtnVal3, onvalue="海鮮", offvalue="", fg='black', command=show)
checkbtn3.grid(row=1,column=2, sticky=W)
# 建立標題Label2
title3label = Label(root, text='飲料:')
title3label.grid(row=4,column=0, sticky=W)
# 放入第四個單選按鈕
checkbtn4 = Checkbutton(root, text='莊園咖啡',variable=checkbtnVal4, onvalue="莊園咖啡", offvalue="", fg='black', command=show)
checkbtn4.grid(row=5,column=0, sticky=W)
# 放入第五個單選按鈕
checkbtn5 = Checkbutton(root, text='日月潭蜜香紅茶',variable=checkbtnVal5, onvalue="日月潭蜜香紅茶", offvalue="", fg='black', command=show)
checkbtn5.grid(row=5,column=1, sticky=W)
# 放入第六個單選按鈕
checkbtn6 = Checkbutton(root, text='伯爵奶茶',variable=checkbtnVal6, onvalue="伯爵奶茶", offvalue="", fg='black', command=show)
checkbtn6.grid(row=5,column=2, sticky=W)

# 建立 Label
statusBar2 = Label(root, text="", fg="black", bg="white", anchor=W, relief="sunken",bd=2)
#加入視窗
statusBar2.grid(row=10,column=0, columnspan=3, sticky=W+E+S)

root.mainloop()