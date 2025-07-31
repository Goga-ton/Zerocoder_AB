# Определите класс Account имитирующий банковский счет
# Клас должен включать Атрибуты для хранения идентификатора владельца, баланс счета
# и методы депозита (пополнение), снятие средств, если на счету достаточно средств

class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money>0:
            self.balance += money
            print(f"Вы успешно пополнили счет. Сумма на счету - {self.balance}")

    def withraw(self, money):
        if money > self.balance:
            print(f"Недостаточно средств на счету. Вы сможете снять только - {self.balance}")
        elif money <= self.balance:
            self.balance -= money
            print(f"Вы успешно сняли - {money} рублей. Остаток средств на счете: {self.balance}")

    def all_balance(self):
        print(f"Текущий баланс - {self.balance}")

man = Account(230379, 600)
man.all_balance()
man.withraw(int(input("Введите сумму которую хотите снять - ")))
man.deposit(8000)














