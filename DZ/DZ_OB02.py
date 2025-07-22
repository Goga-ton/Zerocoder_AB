class User:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__access = "user"
#Функция repr позволяет выводить информацию в нормальном виде
    # def __repr__(self):
    #     return f"User(id={self.id}, name={self._name}, access={self.__access})"

#Данный блок позволяет выводить информационное сообщение о добавлении и удалении
# пользователя, иначе будет ошибка и информационное сообщение нужно удалить
    @property
    def name(self):  # Геттер для name
        return self.__name

    def fun_all(self):
        return self.__id, self.__name, self.__access
    # def fun_id(self):
    #     return self.__id
    # def fun_name(self):
    #    return self.__name
    # def fun_access(self):
    #    return self.__access

class ManUser:
    def __init__(self):
        self.users = []

    def add(self, user):
        self.users.append(user)
        print(f"Пользователь {user.name} добавлен в список.")

    def remove(self, user):
        self.users.remove(user)
        print(f"Пользователь {user.name} удален из списка.")

class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.__access = "admin"
    def fun_all (self):
        return self._User__id, self._User__name, self.__access

user1 = User(11, "Andrej")
user2 = User(22, "Sergej")
user3 = User(33, "Sasha")
admin1 = Admin(1001, "Lusja")
print(f"Выводим параметры в абракатабра: \n{user1}") #если активировать функцию repr
#то информация будет выводиться в читаеммо виде

#Данная строка может выводить только публичные и защищенные параметры
# print(f"Выводим параметры в читаемом виде: "
#       f"\n{user1._id}, {user1._name}, {user1._access}")
print(f"Выводим параметры в читаемом виде: "
      f"\n{admin1.fun_all()}") #, {user1.fun_name()}, {user1.fun_access()}")

manager = ManUser()
manager.add(user1)
manager.add(user2)
manager.add(user3)
manager.add(admin1)
print(f"Выводим СПИСОК в абракатабра: \n{manager.users}")
print(f"Выводим СПИСОК в читаемом виде: ")
for i in manager.users:
    # print(i._id, i._name, i._access)
    print(i.fun_all())

manager.remove(user2)
print(f"Выводим СПИСОК в читаемом виде: ")
for i in manager.users:
    print(i.fun_all())

