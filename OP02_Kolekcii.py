#Списки
numbers = [1,10,3,12,5,-5,56,2]
names = ['Nina', 'Andrej', 'Sergej', 'Andrej', 'Igor']
a = [1, 56, -90, 6.7, True, None, 'Text']
print(names)
names.append('Kiril')
print(names)
#print(a[2])
names.extend([1,2,3])
print(names)
names.insert(2, 'Anna')
print(names)
#names.remove('Andrej')
print(names)
delet = numbers.pop(2)
print(numbers)
print(delet)
#clear(a)
b = names.index('Andrej')
print(b)
print(names.count('Andrej'))
#print(names.revers())
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(len(a))
print (f"минимальное число - {min(numbers)}")
print(f"максимальное число - {max(numbers)}")

print(min(numbers))
numbers.extend(a)
print(numbers)
del names[2]
print(names)

#Кортежи
my_tuple =(1, 2,3,4,5,6,7,8,9, 10,2,2)
my_list = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 88]
my_list.append(-465)
print(my_tuple.index(2,2))
#print(my_tuple)

#Словари
my_dict = {
    "name": "имя",
    "car": "машина",
    "apple": "яблоко",
    "book": "книга"
}
#a = my_dict.popitem()
print(my_dict)
#print(a)
my_dict.update({'book':'Чтиво','cat':"кот"})
print(my_dict)

#Множества

set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {11,12,13,14,16,5,9}

data1 = [21,22,23,24,25,26,27,28,29,30]
data2 = [111,112,113,114,116]
#print(set1)
#set1.add(15)
#print(set1)
#set1.remove(4)
#print(set1)
#set1.discard(11)
#print(set1)
# Работа со множеством
print(set1.union(set2))
print(set1)
a=set1.union(set2)
print(a)
b = set1.intersection(set2)
print(b)
c = set1.difference(set2)
print(c)
d = set2.difference(set1)
print(d)

# Работа  со списками
data1.extend(data2)
print(data1)
print(data1.extend(data2)) # не рабочая конструкция

