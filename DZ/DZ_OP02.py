# ДЗ ОР02 Задание №1 (Сложение значений списка)
print ('Сложение значений списка')
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print("Сумма чисел в списке:", total)

# ДЗ ОР02 Задание №2 (Работа со списками)
print('\nРабота со списками')
spisok = []
spisok.append(22)
spisok.append(54)
spisok.append(2)
spisok.insert(0,10)
spisok.insert(0,8)
spisok.sort()
spisok.reverse()
print(spisok)

# ДЗ ОР02 Задание №3 (Объеденение множеств)
print('\nОбъеденение множеств')
set_1 = {1, 2, 3, 4, 5}
set_2 = {11, 12, 13, 14}
set_avan = set_1.union(set_2)
print(set_avan)
print(set_1.union(set_2))

# ДЗ ОР02 Задание №4 (Пересечение множеств)
print('\nПересечение множеств')
set_1 = {1, 2, 3, 4, 5, 11, 14}
set_2 = {11, 12, 13, 14, 2, 3}
set_avan = set_1.intersection(set_2)
print(set_avan)
print(set_1.intersection(set_2))

# ДЗ ОР02 Задание №5 (Наполнение списка)
print('\nНаполнение списка')
print ('Вам предстоит ввести 10 значений, начнемс:')
spisok = []
for i in range(10):
    i = input(f'Введите число {i+1} - ')
    spisok.append(i)
print('Вы справелись, вот результат:')
print(spisok)