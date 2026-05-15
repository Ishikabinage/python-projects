import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")

tasks = []


def add_task():
    task = task_entry.get()

    if task != "":
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks.pop(selected_task_index)
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Please select a task!")

def mark_done():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks[selected_task_index] = "✓ " + tasks[selected_task_index]
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Please select a task!")

def update_listbox():
    task_listbox.delete(0, tk.END)

    for task in tasks:
        task_listbox.insert(tk.END, task)


title_label = tk.Label(root, text="TO-DO LIST", font=("Arial", 20, "bold"))
title_label.pack(pady=10)


task_entry = tk.Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)


add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", width=15, command=remove_task)
remove_button.pack(pady=5)

done_button = tk.Button(root, text="Mark Done", width=15, command=mark_done)
done_button.pack(pady=5)


task_listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12))
task_listbox.pack(pady=20)


root.mainloop()