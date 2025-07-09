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
        box_plan.itemconfig(tk.END, {'bg': 'VioletRed1'})

def add_plan_list():
    plan_list = lb_td_list.curselection()
    if plan_list:
        select_plan_list = lb_td_list.get(plan_list[0])
        box_plan.insert(tk.END, select_plan_list)

    # команды для кнопок к списку мероприятий
def mark_plan_list():
    select_plan = box_plan.curselection()
    if select_plan:
        box_plan.itemconfig(select_plan, bg = "pink")
def no_mark_plan_list():
    no_select_plan = box_plan.curselection()
    if no_select_plan:
        box_plan.itemconfig(no_select_plan, bg = "PaleTurquoise1")
def del_plan_list():
    select_plan = box_plan.curselection()
    if select_plan:
        box_plan.delete(select_plan)

# Блок создания покупок
def create_plan():
    root.minsize(645, 750)
    global line_buy
    line_buy = tk.Entry(root, width = 50, bg = "gold1", fg = "ForestGreen")
    global b_shop
    b_shop = tk.Button(root, text='Купить в магазине', command = add_buy_shop)
    global b_market
    b_market = tk.Button(root, text='Купить на рынке', command = add_buy_market)
    global b_online
    b_online = tk.Button(root, text='Купить в интернете', command = add_buy_online)
    global lb_shop
    lb_shop = tk.Listbox(root, height=5, width=50, bg = "snow1")
    global lb_market
    lb_market = tk.Listbox(root, height=5, width=50, bg = "snow1")
    global lb_online
    lb_online = tk.Listbox(root, height=5, width=50, bg = "snow1")
    global b_albuy
    b_albuy = tk.Button(root, text='Купил', command = mark_buy)
    b_nalbuy = tk.Button(root, text='Не нужно', command = del_buy)
    line_buy.place(x=150, y=445)
    b_shop.place(x=100, y=475)
    b_market.place(x=430, y=475)
    b_online.place(x=260, y=600)
    lb_shop.place(x=5, y=505)
    lb_market.place(x=335, y=505)
    lb_online.place(x=160, y=630)
    b_albuy.place(x=230, y=720)
    b_nalbuy.place(x=320, y=720)

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
        lb_shop.itemconfig(select_buy_shop, bg = "pink")
    elif select_buy_market:
        lb_market.itemconfig(select_buy_market, bg = "pink")
    elif select_buy_online:
        lb_online.itemconfig(select_buy_online, bg = "pink")

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
root.minsize(645, 450)
root.title("Создай свой список задач")
root.configure(background="DarkSeaGreen1")

# Заголовки окон даты и Дела
n_data = tk.Label(root, text="Создай даты для планирования", background="AliceBlue", fg = "blue4")
td_list = tk.Label(root, text='Список дел', background="yellow1", fg = "blue4")
n_data.place(x=60, y=5)
td_list.place(x=450, y=5)

# Заголовки полей ввода Даты и Дела
entry_n_data = tk.Entry(root, width = 50, bg = "gold1", fg = "ForestGreen")
entry_td_list = tk.Entry(root, width = 50, bg = "gold1", fg = "ForestGreen")
entry_n_data.place(x=5, y=30)
entry_td_list.place(x=335, y=30)

# Кнопки для полей Даты и Дела
b_add_n_data = tk.Button(root, text='Добавить дату', command = add_data)
b_del_n_data = tk.Button(root, text='Удалить дату', command = del_data)
b_add_td_list = tk.Button(root, text='Добавить задачу', command = add_list)
b_del_td_list = tk.Button(root, text='Удалить задачу', command = del_list)
b_add_n_data.place(x=15, y=55)
b_del_n_data.place(x=110, y=55)
b_add_td_list.place(x=345, y=55)
b_del_td_list.place(x=455, y=55)

# Списки Даты и Дела
lb_n_data = tk.Listbox(root, height = 5, width = 50, bg = 'AliceBlue')
lb_td_list = tk.Listbox(root, height = 5, width = 50, bg = 'yellow1')
lb_n_data.place(x=5, y=100)
lb_td_list.place(x=335, y=100)

# Выбор Даты и Задачи
b_int_n_data = tk.Button(root, text='Выбрать дату', command = add_plan_data)
b_int_td_list = tk.Button(root, text='Выбрать задачу', command =add_plan_list)
b_int_n_data.place(x=45, y=190)
b_int_td_list.place(x=510, y=190)

# Блок итоговых мероприятий
n_plan = tk.Label(root, text="План мероприятий", bg = 'PaleTurquoise1', fg = "blue4")
box_plan = tk.Listbox(root, height = 5, width = 50, bg = 'PaleTurquoise1')
b_int_plan = tk.Button(root, text='Сделано', command = mark_plan_list)
b_Nint_plan = tk.Button(root, text='Отменить выделенное', command = no_mark_plan_list)
b_del_plan = tk.Button(root, text='Удалить задачу', command = del_plan_list)
n_plan.place(x=260, y=220)
box_plan.place(x=155, y=245)
b_int_plan.place(x=155, y=340)
b_Nint_plan.place(x=220, y=340)
b_del_plan.place(x=365, y=340)

# Блок покупок
b_buy = tk.Button(root, text='Сформировать список покупок', command=create_plan)
b_buy.place(x=200, y=400)

root.mainloop()