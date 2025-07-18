class User:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__access = "user"
    # def __repr__(self):
    #     return f"User(id={self.__id}, name={self.__name}, access={self.__access})"

    # def fun_id(self):
    #     return self.__id, self.__name, self.__access
    #def fun_name(self):
       # return self.__name
    #def fun_access(self):
       # return self.__access

class ManUser:
    def __init__(self):
        self.users = []

    def add(self, user):
        self.users.append(user)
       # print(f"Пользователь {user.name} добавлен в список.")

    def remove(self, user):
        self.users.remove(user)
        print(f"Пользователь {user.name} удален из списка.")

# class Admin(User):
#     def __init__(self, id, name):
#         super().__init__(id, name)
#         self.__access = "admin"

user1 = User(11, "Andrej")
user2 = User(22, "Sergej")
user3 = User(33, "Sasha")
#admin1 = Admin(256, "Lusja")

#print(f"{user1.fun_id()}")#, user1.fun_name(), user1.fun_access())

manager = ManUser()
manager.add(user1)
manager.add(user2)
manager.add(user3)
#manager.add(admin1)
# manager.remove(user2)
print(manager.users)
# for i in manager.users:
#     print(f"ID = {i.__id}, Name = {i.__name}, Access = {i.__access}")







class Admin(User):
    pass