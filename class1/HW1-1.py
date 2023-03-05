import tkinter as tk

# create window and widgets
root = tk.Tk()
#create var
status_var = tk.StringVar()
status_var.set("初始化")

status_label = tk.Label(root, textvariable=status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_label.pack(side=tk.BOTTOM, fill=tk.X)

def start():
    status_var.set("start")

def stop():
    status_var.set("stop")

start_button = tk.Button(root, text="Start", command=start)
start_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop)
stop_button.pack()

# start 
root.mainloop()
