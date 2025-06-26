# Первая часть
true_password = "123a45"
email_true = 'zerocode@gmail.com'

password = input('Введите пароль - ')

if password == true_password:
    print('Верный пароль')
    print('Введите почту')

    email = input('email - ')
    if email == email_true:
        print('Вы вошли в аккаунт')
    else:
        print('Вы ввели неправильную почту')

else:
    print('Пароль не верный')

# Вторая чась
print("Добро пожаловать в волшебный лес!")

choice1 = input("Вы находитесь на развилке. Куда вы пойдете? (лево/прямо): ").lower()

if choice1 == "лево":
    print("Вы встретили волшебника! Он предлагает вам зелье.")
    choice2 = input("Выпьете ли вы зелье? (да/нет): ").lower()
    if choice2 == "да":
        print("Зелье оказалось зельем мудрости. Вы стали умнее! Поздравляем, вы выиграли!")
    else:
        print("Волшебник обиделся и превратил вас в лягушку. Конец игры!")
elif choice1 == "прямо":
    print("Вы нашли сокровище! Но рядом стоит дракон.")
    choice3 = input("Попытаетесь ли вы украсть сокровище? (да/нет): ").lower()
    if choice3 == "да":
        print("Дракон заметил вас и превратил в золу своим дыханием. Конец игры!")
    else:
        print("Вы решили не рисковать. Вдруг дракон предложил вам часть сокровища за доброту. Вы выиграли!")
else:
    print("Вы выбрали неизведанное направление и заблудились. Конец игры!")

print("Спасибо за игру!")

#Третья часть
temp = 26
weather = "sunny"
if temp == 26 or weather == "sunny":
    print('можно одевать шорты')

print(not(8<2))

#Четвертая часть
command = input('Введите команду: ')
match command:
    case "start":
        print("Начинаем работу")
    case "stop":
        print("Стоп")
    case "exit":
        print("Выход")


# Инициализация переменных
summa = 0
number = None
print("Введите числа для подсчёта их суммы. Для завершения введите 0.")

# Цикл while продолжается до ввода числа 0
while number != 0:
    number = int(input("Введите число: "))
    summa += number

print("Сумма введённых чисел:", summa)

# Про деньги
money = 500

print(f"Ваш баланс - {money}")

while money > 0:
    money -= 50
    print(f"Ваш баланс - {money}")

# else
i=0
while i <= 10:
    print(i)
    i += 1
else:
    print(f"цикл окончен, i = {i}")


#Оератор if в операторе while
num = int(input("Enter a number: "))

while num != 0:
    if num < 0:
        print("The number is negative")
        break
    num = int(input("Enter a number: "))
else:
    print("Мы не встретили ни одного отрицательного числа")

# Бесконечный цикл
x = 0
while True:
        x += 1
        print(x)
        if x >= 5:
                break

# Проверка на четность
print("Введите числа для проверки на нечётность. Для завершения введите 0.")
while True:  # Бесконечный цикл, который будет прерван только при определенном условии
    number = int(input("Введите число: "))
    if number == 0:  # Условие для выхода из цикла
        break
    if number % 2 == 0:  # Проверка на четность
        continue  # Пропускаем четные числа
    print("Нечетное число:", number)  # Выводим нечетное число

print("Программа завершена.")