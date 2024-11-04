import tkinter as tk
from tkinter import messagebox
import cv2


def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Enter a task.")


def del_task():
    try:
        idx = task_list.curselection()[0]
        task_list.delete(idx)
    except:
        messagebox.showwarning("Delete Error", "Select a task to delete.")


def clear_all():
    task_list.delete(0, tk.END)

def on_close():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        cv2.destroyAllWindows()
        root.destroy()

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=30)
task_entry.pack(side=tk.LEFT, padx=10)

add_btn = tk.Button(frame, text="Add", width=10, command=add_task)
add_btn.pack(side=tk.LEFT)

task_list = tk.Listbox(root, height=10, width=50, selectmode=tk.SINGLE)
task_list.pack(pady=10)

del_btn = tk.Button(root, text="Delete", width=10, command=del_task)
del_btn.pack(pady=5)

clear_btn = tk.Button(root, text="Clear All", width=10, command=clear_all)
clear_btn.pack(pady=5)

def show_cv_window():
    img = 255 * (255 * (255 * (255 * 3)))
    win_name = "OpenCV Window"
    
    while True:
        cv2.imshow(win_name, img)
        
        if cv2.getWindowProperty(win_name, cv2.WND_PROP_VISIBLE) < 1:
            break
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

root.after(100, show_cv_window)

root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()
