# 🔒 1. Инкапсуляция (Encapsulation)
# 📌 Что это такое?
# Инкапсуляция — это:
# скрытие внутренней реализации объекта и управление доступом к данным
# Проще:
# данные нельзя менять напрямую
# работать с ними можно только через методы

# Уровень     Запись     Значение

# Public     attr     доступен везде
# Protected     _attr     «для наследников»
# Private     __attr     скрыт внутри класса
import random
class BankAccount:

    def __init__(self, login, balance, password):
        self.login = login
        self._balance = balance
        self.__password = password

    def m_login(self, login, password):
        if self.login == login and self.__password == password:
            return print("ОК!!")
        else:
            return print("Неверный логин или пароль!!")

    def __random_pass(self):
        return random.randint(1, 10)

    def reset_pass(self, login):
        if login == self.login:
            self.__password = self.__random_pass()
        else:
            print("Ошибка!!")

    def get_balance(self):
        return self._balance

# ardager = BankAccount("Ardager", 1000, "123321")
# print(ardager.get_balance())
# print(ardager.__password)
# ardager.reset_pass("Ardager")
# print(ardager.__password)





# Абстракция


from abc import ABC, abstractmethod

# Абстрактный класс
class SendOTP(ABC):
    @abstractmethod
    def send_otp_to_phone(self):
        pass
    @abstractmethod
    def send_otp_to_email(self):
        pass

class SendOTPKG(SendOTP):

    def send_otp_to_phone(self):
        send = ''''
        <Phone>+996779280699</Phone>
        <Text>Ваш временный пароль 5555</Text>
        '''
        print(send)

    def send_otp_to_email(self):
        print('OTP send to email')

class SendOTPRU(SendOTP):
    def send_otp_to_phone(self):
        send = {
            "phone": "+79652101537",
            "text": "Ваш временный пароль 5555"
        }
        print(send)

    def send_otp_to_email(self):
        print('OTP send to email')


otp_kg = SendOTPKG()
otp_ru = SendOTPRU()