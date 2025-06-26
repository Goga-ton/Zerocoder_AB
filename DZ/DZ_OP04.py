#Задание 1 (Суммирование всех целых чисел в диапозоне)
print('Суммирование всех целых чисел в диапозоне')

def sum_range(start, end):
    spisok = list(range(start, end + 1))
    spisok_cel = sum(spisok)
    #list(filter(lambda x: x%1 == 0, spisok))
    print(spisok_cel)
sum_range(1, 10)

#Задание 2 (Получаем в кортежи три значения через запятую)
print('Получаем в кортежи три значения через запятую')

def square(a):
    return a * a, a * 4, (a**2+a**2)**0.5
result = square(6)
print(result)

#Задание 3 (Посчитать вклад)
print('Расчет суммы вклада при 10% годовыхэ')

def bank(vklad, years):

    for year in range(1, years+1):
        vklad += vklad * 10/100
        #print(vklad)
    return vklad, years

total_sum, user_years = bank(100,5)

print('Сумма на Вашем счете через ',user_years, 'лет будет составлять', total_sum)