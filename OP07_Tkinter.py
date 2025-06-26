# Создаем кнопку и меням запись
import tkinter as tk
# root — это такая переменная в которой хранится все окно и с помощью
# этой переменной мы сможем обращаться к нему, то есть будем писать в этом окне.
root = tk.Tk()
# Создаем заголовок используя клманду tittle
root.title("Первый проект")
# Создаем переменную (tk.Label — функция, которая добавляет текст на экран,
# root — название окна, где все должно появляться, и text= — что тот текст, который хотим прописать.)
label = tk.Label(root, text="это первый текст в приложении")
# Помещаем переменную внутрь окна
label.pack()
# Создаем функцию которая будет менять текст внутри окна
# config — используется для изменения параметров, то есть настроек функции label. label — виджет, а не функция
def on_button_click():
    label.config(text="Кнопка была нажата")
# Создаем элемент (кнопку) указывая окно, ее текст и команду (при ее нажатии будет вызываться наша функция "on_button_click")
button = tk.Button(root, text="Нажми на меня", command=on_button_click)
# Добавляем кнопку в окно посередине это делает команда pack
button.pack()

root.mainloop() # зацикливаемокно чтобы оно оставалось на экране


# Создаем поле и по кнопке получаем сумму
import tkinter as tk

def my_summa():
    nymbers = entry.get().split()
    result = 0
    #result = []
    for namber in nymbers:
        result += int(namber)
        #  можем посчитать через сумипрвание элекментов в списке
        # namber = int(namber)
        # result.append(namber)
        # x = sum(result)
    label.config(text=f"Сумма чисел - {result}")

root = tk.Tk()
root.title('Сумма чисел')

label = tk.Label(root, text = 'Введите числа через пробел')
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text = 'Посчитать сумму', command=my_summa)
button.pack()

root.mainloop()


# Создаем две кнопки и пробуем их двигать
from tkinter import Tk, Button # активизируем две функции сразу
root1 = Tk()
button1 = Button(root1, text = 'Кнопка 1')
button2 = Button(root1, text = 'Кнопка 2')
# (row=0) — это верхний ряд, ряд 1 (row=1) — это нижний ряд.
# колонка 0 (column=0) это самая левая колонка, а дальше будут 1, 2, 3. Это как индексы в списке.
button1.grid(row = 0, column = 0)
# команда place размещает кнопку в окне по координатам
button2.place(x = 50, y = 100)

root1.mainloop()
