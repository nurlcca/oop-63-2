from abc import ABC, abstractmethod

class User:

    def __init__(self, first_name, last_name, balance, bonus):
        self.first_name = first_name
        self.last_name = last_name
        self._balance = balance
        self.bonus = bonus

    def get_balance(self):
        return self.balance

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
    @property
    def total_balance(self):
        return self._balance + self.bonus

    @property
    def user_balance(self):
        return self._balance

    @user_balance.setter
    def user_balance(self, value):
        if value < 0:
            return print('ошибка!!')
        self._balance = value



ardager = User('Ardager', 'Kartanbekov', 100, 50)

# print(ardager.first_name)
# print(ardager.user_balance)
#
# ardager.user_balance = 200
# print(ardager.user_balance)
# print(adrager.get_balance())
# print(adrager.full_name)
# print(adrager.total_balance)


# def simple_decorator(func):
#     def wrapper():
#         print('До выполнеия!!')
#         func()
#         print('после выполнеия!!')
#     return wrapper
#
# @simple_decorator
# def say_hello():
#     print('Hello world!!')
#
# say_hello()

# def how(func):
#     def wrapper(imya):
#         func(imya)
#         print(f'How are you {imya}?')
#     return wrapper
#
# @how
# def greeting(name):
#     print(f"{name} hello!!")
#
# greeting("Ardager")


def repeat_decorator(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator

@repeat_decorator(5)
def say_hello():
    print('Hello world!!')


# say_hello()


def class_decorator(cls):
    class NewClass(cls):
        def method(self):
            print("New method!!")
    return NewClass

@class_decorator
class OldClass:
    def method(self):
        print("Old method!!")


obj_1 = OldClass()

print(type(obj_1))
