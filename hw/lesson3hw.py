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


#account = UserAccount("nuraiym", "nuraiym", 1234, 5000)

#account.check_access("nuraiym", 1234)
#account.change_password("nuraiym")
#print(account.get_balance())

#try:
    #print(account.__password)
#except AttributeError:
    #print("No access to private attribute")

from abc import ABC, abstractmethod
class NotificationService(ABC):
    @abstractmethod
    def send_to_phone(self, phone, text):
        pass
    @abstractmethod
    def send_to_email(self, email, text):
        pass

class SMSService(NotificationService):
    def send_to_phone(self, phone, text):
        print(f"Sending SMS to {phone}")
    
    def send_to_email(self, email, text):
        print("SMS can't be sent to email")

class EmailService(NotificationService):
    def send_to_phone(self, phone, text):
        print("Email can't be sent to phone")
    
    def send_to_email(self, email, text):
        print(f"Sending email to {email}")

sms = SMSService()
email = EmailService()

sms.send_to_phone("+996700000000", "Your code: 1234")
sms.send_to_email("test@gmail.com", "Your code: 1234")

email.send_to_phone("+996700000000", "Your code: 1234")
email.send_to_email("test@gmail.com", "Your code: 1234")

