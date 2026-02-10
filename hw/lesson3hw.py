import random


class UserAccount:
    def __init__(self, username, login, password, balance):
        self.username = username          # public
        self._login = login               # protected
        self._balance = balance           # protected
        self.__password = password        # private

    # access check
    def check_access(self, login, password):
        if self._login == login and self.__password == password:
            print("OK!!")
        else:
            print("Invalid login or password!!")

    # private method
    def __generate_password(self):
        return random.randint(1000, 9999)

    # change private attribute
    def change_password(self, login):
        if login == self._login:
            self.__password = self.__generate_password()
        else:
            print("Error!!")

    # getter
    def get_balance(self):
        return self._balance


account = UserAccount("nuraiym", "nuraiym", 1234, 5000)

account.check_access("nuraiym", 1234)
account.change_password("nuraiym")
print(account.get_balance())

try:
    print(account.__password)
except AttributeError:
    print("No access to private attribute")

