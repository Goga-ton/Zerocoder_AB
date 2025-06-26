import tkinter as tk
# Блок создания покупок
def create_plan():
    line_buy = tk.Entry(root, width = 50, bg = "gold1", fg = "ForestGreen")
    b_shop = tk.Button(root, text='Купить в магазине')
    b_market = tk.Button(root, text='Купить на рынке')
    b_online = tk.Button(root, text='Купить в интернете')
    lb_shop = tk.Listbox(root, height=5, width=50)
    lb_market = tk.Listbox(root, height=5, width=50)
    lb_online = tk.Listbox(root, height=5, width=50)
    b_albuy = tk.Button(root, text='Купил')
    b_nalbuy = tk.Button(root, text='Не нужно')
    line_buy.grid(row=9, column=0, padx=5, pady=5)
    b_shop.grid(row=10, column=0, padx=5, pady=5)
    b_market.grid(row=10, column=1, padx=5, pady=5)
    b_online.grid(row=10, column=2, padx=5, pady=5)
    lb_shop.grid(row = 11, column=0, padx=5, pady=5)
    lb_market.grid(row=11, column=1, padx=5, pady=5)
    lb_online.grid(row=11, column=2,)
    b_albuy.grid(row=12, column=0, padx=5, pady=5)
    b_nalbuy.grid(row=12, column=1, padx=5, pady=5)

root = tk.Tk()
root.minsize(500, 400)
root.title("Создай свой список задач")
root.configure(background="DarkSeaGreen1")

# Заголовки окон даты и Дела
n_data = tk.Label(root, text="Создай даты для планирования",
                  background="DarkSeaGreen3")
td_list = tk.Label(root, text='Список дел')
n_data.grid(row = 0, column = 0, sticky="", padx=5, pady=5)
td_list.grid(row=0, column=1, sticky="e", padx=5, pady=5)

# Заголовки полей ввода Даты и Дела
entry_n_data = tk.Entry(root, width = 50, bg = "gold1", fg = "ForestGreen")
entry_td_list = tk.Entry(root, width = 50, bg = "gold1", fg = "ForestGreen")
entry_n_data.grid(row=1, column=0, padx=5, pady=5)
entry_td_list.grid(row=1, column=1, padx=5, pady=5)

# Кнопки для полей Даты и Дела
b_add_n_data = tk.Button(root, text='Добавить дату')
b_del_n_data = tk.Button(root, text='Удалить дату')
b_add_td_list = tk.Button(root, text='Добавить задачу')
b_del_td_list = tk.Button(root, text='Удалить задачу')
b_add_n_data.grid(row = 2, column = 0)
b_del_n_data.grid(row = 2, column = 1)
b_add_td_list.grid(row = 2, column = 2)
b_del_td_list.grid(row = 2, column = 3)

# Списки Даты и Дела
lb_n_data = tk.Listbox(root, height = 5, width = 50)
lb_td_list = tk.Listbox(root, height = 5, width = 50)
lb_n_data.grid(row = 3, column = 0, padx=5, pady=5)
lb_td_list.grid(row=3, column=1, padx=5, pady=5)

# Выбор Даты и Задачи
b_int_n_data = tk.Button(root, text='Выбрать дату')
b_int_n_data.grid(row = 4, column = 0)
b_int_td_list = tk.Button(root, text='Выбрать задачу')
b_int_n_data.grid(row=4, column=0, padx=5, pady=5)
b_int_td_list.grid(row=4, column=1, padx=5, pady=5)

# Блок итоговых мероприятий
n_plan = tk.Label(root, text="План мероприятий")
box_plan = tk.Listbox(root, height = 5, width = 50)
b_int_plan = tk.Button(root, text='Сделано')
b_Nint_plan = tk.Button(root, text='Отменить выделенное')
b_del_plan = tk.Button(root, text='Удалить задачу')
n_plan.grid(row = 5, column = 0, padx=5, pady=5)
box_plan.grid(row = 6, column = 0, padx=5, pady=5)
b_int_plan.grid(row = 7, column = 0, padx=5, pady=5)
b_Nint_plan.grid(row = 7, column = 1, padx=5, pady=5)
b_del_plan.grid(row = 7, column = 2, padx=5, pady=5)

# Блок покупок
b_buy = tk.Button(root, text='Сформировать список покупок', command=create_plan)
b_buy.grid(row = 8, column = 0, padx=5, pady=5)



#n_data.pack(pady=5)





root.mainloop()