import tkinter as tk
from tkinter import ttk

# 定義三個清單
BMW=["1 Series (F40)","1 Series (F52)","2 Series Gran Coupé","2 Series","3 Series","4 Series","5 Series","6 Series","7 Series","8 Series","X1","X2","X3","X4","X5","X6","X7","Z4","2 Series Active Tourer","i3 (G28)","i4","i7","iX1","iX3","iX"]
Mercedes=["A-Class(Hatchbacks)","A-Class(Sedans)","C-Class","CLA","CLS","E-Class","EQE","EQS","S-Class","C-Class","CLA","E-Class","E-Class","EQA","EQB","EQC","G-Class","GLA","GLB","GLC","GLE","GLS","AMG GT","AMG GT 4-Door Coupé","AMG SL","AMG One","B-Class","Citan Van","Viano","EQV"]
Audi=["A1","A3","A4","A5","A6","A7","A8","e-tron GT","TT","R8","Q2","Q3","2019","Q4 e-tron","2021","Q5","Q5 e-tron","Q6","Q7","Q8","e-tron"]

# 建立主視窗
root = tk.Tk()
root.title("Combobox and Listbox Example")

# 建立 Combobox
combo = ttk.Combobox(root, values=["BMW", "Mercedes", "Audi"])
combo.pack()

# 建立 Listbox
listbox = tk.Listbox(root)
listbox.pack()

# 定義函式，在選取 Combobox 的選項後更新 Listbox 的內容
def update_listbox():
    selection = combo.get()
    if selection == "BMW":
        listbox.delete(0, tk.END)
        for item in BMW:
            listbox.insert(tk.END, item)
    elif selection == "Mercedes":
        listbox.delete(0, tk.END)
        for item in Mercedes:
            listbox.insert(tk.END, item)
    elif selection == "Audi":
        listbox.delete(0, tk.END)
        for item in Audi:
            listbox.insert(tk.END, item)


# 開始運行主程式迴圈
root.mainloop()
