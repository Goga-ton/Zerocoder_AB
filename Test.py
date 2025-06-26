import tkinter as tk

def create_plan():
    plan = tk.Listbox(root, height=5, width=50)
    plan.pack(pady=5, padx=15)

root = tk.Tk()
button = tk.Button(root, text = "Create Plan", command = create_plan)
button.pack()

root.mainloop()