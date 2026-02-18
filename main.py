# import module_1
# # from module_1 import say_hello, add
#
# print(module_1.add(12,12))
# module_1.say_hello()
#
# print(module_1.random.randint(1, 2))

# from my_package import add, say_hello, test
#
# print(add(12, 12))


from colorama import Fore, Back, Style


print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')