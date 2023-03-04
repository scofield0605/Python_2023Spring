import tkinter as tk

# create window and widgets
root = tk.Tk()

status_var = tk.StringVar()
status_var.set("初始化。")

status_label = tk.Label(root, textvariable=status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_label.pack(side=tk.BOTTOM, fill=tk.X)

def start():
    status_var.set("運行中")

def stop():
    status_var.set("已停化")

start_button = tk.Button(root, text="Start", command=start)
start_button.pack(side=tk.LEFT)

stop_button = tk.Button(root, text="Stop", command=stop)
stop_button.pack(side=tk.LEFT)

# start 
root.mainloop()
