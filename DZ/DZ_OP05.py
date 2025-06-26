#Задание №1
print('Функция деления, при делении на 0 вызывает "None"')

def delenie():
    try:
        a = float(input('Введите делимое: '))
        b = float(input("Введите делитель: "))
        return a/b
    except ZeroDivisionError:
        return None
    except ValueError:
        return ('Введено не число ')

print(delenie())


#Задание №2
print()
print('Обработка множества видов исключений')

def celochis():
    while True:
        try:
            a = float(input('Введите число: '))
            print(int(a // 1))
            break

        except ValueError:
            print('Невозможно преобразовать в целое число')

celochis()


#Задание №3
print()
print('Суммирование всех целых чисел в диапозоне')

def sum_range():
    try:
        start = int(input("Введите начальное число: "))
        end = int(input("Введите конечное число: "))
        spisok = list(range(start, end + 1))
        spisok_cel = sum(spisok)
        print(spisok_cel)
        return start, end
    except (ValueError):
        print('Введен неверный формат данных')

try:
    start, end = sum_range()
except TypeError:
    print('Опять ошибка')



