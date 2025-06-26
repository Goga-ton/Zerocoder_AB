# Вводим имя и прога пишет Привет и имя

from tkinter import Tk, Button, Label, Entry
def hellow():
    name = inp.get()
    nadpis.config(text = f'Hellow, {name}')

window = Tk()
window.title('Домашнее занадие ОР7')

nadpis = Label(window, text="")
nadpis.pack()

inp = Entry(window)
inp.pack()

button = Button(window, text = 'Input your name', command = hellow)
button.pack()

window.mainloop()
