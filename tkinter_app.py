import tkinter as tk
from tkinter import messagebox

todos = []

def add_task():
    task = entry.get()
    if task:
        todos.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        todos.pop(selected)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete!")

root = tk.Tk()
root.title("Todo App")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Todo", command=add_task)
add_btn.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

del_btn = tk.Button(root, text="Delete Selected", command=delete_task)
del_btn.pack()

root.mainloop()
