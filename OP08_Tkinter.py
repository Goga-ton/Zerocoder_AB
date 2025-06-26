import tkinter as tk

def add_task():
    task = task_entry.get()  # здесь мы получаем слова из поля для ввода
    if task: # если task существует тогда
        task_listbox.insert(tk.END, task) # здесь с помощью константы END вставляем полученное слово в конец списка
        task_entry.delete(0, tk.END) # здесь очищаем поле для ввода, от нулевого индекса и до конца

def del_task():
    # с помощью функции **curselection** элемент, на который мы нажмём, будет передавать свой ID, индекс, в переменную  selected_task
    selekt_task = task_listbox.curselection()
    if selekt_task:
        task_listbox.delete(selekt_task) # удаляем выбранный элемент из списка

def mark_task():
    selekt_task = task_listbox.curselection()
    if selekt_task:
        selekt_task = task_listbox.itemconfig(selekt_task, bg = "red")


root = tk.Tk()
root.title('Task list')
root.configure(background = "deep sky blue")

text1 = tk.Label(root, text = "Inter your task", bg = "yellow1", fg = "MediumBlue")
text1.pack(pady=5)

task_entry = tk.Entry(root, width = 50, bg = "gold1", fg = "ForestGreen")
task_entry.pack(pady=5, padx=15)

add_task_button = tk.Button(root, text='Add task', command=add_task)
add_task_button.pack(pady=5)

del_task_button = tk.Button(root, text='Delet task', command = del_task)
del_task_button.pack(pady=5)
del_task_button.pack(pady=5)

mark_task_button = tk.Button(root, text='Mark a completed task', command=mark_task)
mark_task_button.pack(pady=5)

text2 = tk.Label(root, text = "Inter your task", bg = "LightYellow2", fg = "red")
text2.pack(pady=15)

task_listbox = tk.Listbox(root, height=10, width=50, bg="LightPink1")
task_listbox.pack(pady=5)

close_button = tk.Button(root, text="Close", command=root.destroy).pack(pady=5)

root.mainloop()
