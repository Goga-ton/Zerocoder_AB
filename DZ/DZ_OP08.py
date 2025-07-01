import tkinter as tk

# Блок создания списков дата и дела
def add_data():
    data = entry_n_data.get()
    if data:
        lb_n_data.insert(tk.END, data)
        entry_n_data.delete(0, tk.END)
def add_list():
    list = entry_td_list.get()
    if list:
        lb_td_list.insert(tk.END, list)
        entry_td_list.delete(0, tk.END)
def del_data():
    select_data = lb_n_data.curselection()
    if select_data:
        lb_n_data.delete(select_data)
def del_list():
    select_list = lb_td_list.curselection()
    if select_list:
        lb_td_list.delete(select_list)

# Блок создания списка мероприятий
def add_plan_data():
    plan_data = lb_n_data.curselection()
    if plan_data:
        select_plan_data = lb_n_data.get(plan_data[0])
        box_plan.insert(tk.END, select_plan_data)

def add_plan_list():
    plan_list = lb_td_list.curselection()
    if plan_list:
        select_plan_list = lb_td_list.get(plan_list[0])
        box_plan.insert(tk.END, select_plan_list)

    # команды для кнопок к списку мероприятий
def mark_plan_list():
    select_plan = box_plan.curselection()
    if select_plan:
        box_plan.itemconfig(select_plan, bg = "blue")
def no_mark_plan_list():
    no_select_plan = box_plan.curselection()
    if no_select_plan:
        box_plan.itemconfig(no_select_plan, bg = "white")
def del_plan_list():
    select_plan = box_plan.curselection()
    if select_plan:
        box_plan.delete(select_plan)

# Блок создания покупок
def create_plan():
    global line_buy
    line_buy = tk.Entry(root, width = 50, bg = "gold1", fg = "ForestGreen")
    global b_shop
    b_shop = tk.Button(root, text='Купить в магазине', command = add_buy_shop)
    global b_market
    b_market = tk.Button(root, text='Купить на рынке', command = add_buy_market)
    global b_online
    b_online = tk.Button(root, text='Купить в интернете', command = add_buy_online)
    global lb_shop
    lb_shop = tk.Listbox(root, height=5, width=50)
    global lb_market
    lb_market = tk.Listbox(root, height=5, width=50)
    global lb_online
    lb_online = tk.Listbox(root, height=5, width=50)
    global b_albuy
    b_albuy = tk.Button(root, text='Купил', command = mark_buy)
    b_nalbuy = tk.Button(root, text='Не нужно', command = del_buy)
    line_buy.grid(row=9, column=0, padx=5, pady=5)
    b_shop.grid(row=10, column=0, padx=5, pady=5)
    b_market.grid(row=10, column=1, padx=5, pady=5)
    b_online.grid(row=10, column=2, padx=5, pady=5)
    lb_shop.grid(row = 11, column=0, padx=5, pady=5)
    lb_market.grid(row=11, column=1, padx=5, pady=5)
    lb_online.grid(row=11, column=2,)
    b_albuy.grid(row=12, column=0, padx=5, pady=5)
    b_nalbuy.grid(row=12, column=1, padx=5, pady=5)

    # Команды для кнопок покупок
def add_buy_shop():
    buy = line_buy.get()
    if buy:
        lb_shop.insert(tk.END, buy)
        line_buy.delete(0, tk.END)
def add_buy_market():
    buy = line_buy.get()
    if buy:
        lb_market.insert(tk.END, buy)
        line_buy.delete(0, tk.END)
def add_buy_online():
    buy = line_buy.get()
    if buy:
        lb_online.insert(tk.END, buy)
        line_buy.delete(0, tk.END)

def mark_buy():
    select_buy_shop = lb_shop.curselection()
    select_buy_market = lb_market.curselection()
    select_buy_online = lb_online.curselection()
    if select_buy_shop:
        lb_shop.itemconfig(select_buy_shop, bg = "red")
    elif select_buy_market:
        lb_market.itemconfig(select_buy_market, bg = "red")
    elif select_buy_online:
        lb_online.itemconfig(select_buy_online, bg = "red")

def del_buy():
    del_buy_shop = lb_shop.curselection()
    del_buy_market = lb_market.curselection()
    del_buy_online = lb_online.curselection()
    if del_buy_shop:
        lb_shop.delete(del_buy_shop)
    elif del_buy_market:
        lb_market.delete(del_buy_market)
    elif del_buy_online:
        lb_online.delete(del_buy_online)

root = tk.Tk()
root.minsize(500, 400)
root.title("Создай свой список задач")
root.configure(background="DarkSeaGreen1")

# Заголовки окон даты и Дела
n_data = tk.Label(root, text="Создай даты для планирования",
                  background="DarkSeaGreen3")
td_list = tk.Label(root, text='Список дел')
n_data.place(x=60, y=5)
td_list.place(x=660, y=5)

# Заголовки полей ввода Даты и Дела
entry_n_data = tk.Entry(root, width = 50, bg = "gold1", fg = "ForestGreen")
entry_td_list = tk.Entry(root, width = 50, bg = "gold1", fg = "ForestGreen")
entry_n_data.place(x=5, y=30)
entry_td_list.place(x=5, y=30)

# Кнопки для полей Даты и Дела
b_add_n_data = tk.Button(root, text='Добавить дату', command = add_data)
b_del_n_data = tk.Button(root, text='Удалить дату', command = del_data)
b_add_td_list = tk.Button(root, text='Добавить задачу', command = add_list)
b_del_td_list = tk.Button(root, text='Удалить задачу', command = del_list)
b_add_n_data.place(x=5, y=60)
b_del_n_data.place(x=5, y=60)
b_add_td_list.place(x=5, y=60)
b_del_td_list.place(x=5, y=60)

# Списки Даты и Дела
lb_n_data = tk.Listbox(root, height = 5, width = 50)
lb_td_list = tk.Listbox(root, height = 5, width = 50)
lb_n_data.place(x=5, y=100)
lb_td_list.place(x=380, y=100)

# Выбор Даты и Задачи
b_int_n_data = tk.Button(root, text='Выбрать дату', command = add_plan_data)
b_int_td_list = tk.Button(root, text='Выбрать задачу', command =add_plan_list)
b_int_n_data.place(x=105, y=150)
b_int_td_list.place(x=415, y=150)

# Блок итоговых мероприятий
n_plan = tk.Label(root, text="План мероприятий")
box_plan = tk.Listbox(root, height = 5, width = 50)
b_int_plan = tk.Button(root, text='Сделано', command = mark_plan_list)
b_Nint_plan = tk.Button(root, text='Отменить выделенное', command = no_mark_plan_list)
b_del_plan = tk.Button(root, text='Удалить задачу', command = del_plan_list)
n_plan.place(x=260, y=190)
box_plan.place(x=155, y=215)
b_int_plan.place(x=155, y=320)
b_Nint_plan.place(x=220, y=320)
b_del_plan.place(x=365, y=320)

# Блок покупок
b_buy = tk.Button(root, text='Сформировать список покупок', command=create_plan)
b_buy.place(x=220, y=365)



root.mainloop()