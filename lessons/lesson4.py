# # class Test:
# #
# #     def __init__(self, value):
# #         self.value = value
#
#     # def __str__(self):
#     #     return str(self.value)
#
#
# # test_obj = Test(321456)
# # my_int = int(123)
# #
# # print(my_int)
# # print(test_obj)
#
#
#
#
# # t = 1
# # t2 = 3
# # t3 = t + t2
# # print(t3)
# class MyInt:
#     view_count = 0
#
#
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, other):
#         if type(self) == type(other):
#             return self.value + other.value
#         return print()
#
#     def __str__(self):
#         return str(self.value)
#
#     def __call__(self, *args, **kwargs):
#         self.view_count += 1
#         print(self.view_count)
#
# my_int1 = MyInt(12)
# my_int2 = MyInt(10)
# #
# # my_int1()
# # my_int1()
# # my_int1()
# # my_int1()
# # my_int1()
#
#
# # print(my_int1)
# # print(my_int2)
#
#
# # just_list =  [ 1,2,3,4,5]
# # print(just_list[2])
#
# class MyList:
#
#     def __init__(self, array):
#         self.array = array
#
#     def __getitem__(self, item):
#         return self.array[item]
#
# # my_list = MyList([1,2,34,5,6,7,])
# #
# # print(my_list[5])
# #
# # class Test2:
# #
# #     def __aenter__(self):
# #         ...
# #     def __aexit__(self, exc_type, exc_val, exc_tb):
# #         ...
#

class BankAccount:
    # Атрибуты класса
    bank_name = "Simba"

    def __init__(self, name, balance):
        # Атрибуты экземпляра класса
        self.name = name
        self.balance = balance

    def just_method(self):
        return self.name

    @staticmethod
    def static_method():
        print("Static method")

    @classmethod
    def class_method(cls):
        print(cls.bank_name)


# BankAccount.static_method()
BankAccount.class_method()