# Child class
from User import *


class Bank(User):

    def __init__(self, name, password, age, checking, saving):
        # Inherent attributes from user
        super().__init__(name, password, age)
        self.checking = checking
        self.saving = saving

    def deposit(self, amount, account):
        # Checking account
        if account == 0:
            self.checking += amount
            print(f'${self.checking} remaining in checking')
        # Saving account
        elif account == 1:
            self.saving += amount
            print(f'${self.saving} remaining in saving')
        else:
            print(f'Error')

    def withdraw(self, amount, account):
        # Checking account
        if account == 0:
            self.checking -= amount
            print(f'${self.checking} remaining in checking')
        # Saving account
        elif account == 1:
            self.saving -= amount
            print(f'${self.saving} remaining in saving')
        else:
            print(f'Error')

    def show_bal(self, account):
        # Checking account
        if account == 0:
            print(f'${self.checking} in checking')
            return self.checking
        # Saving account
        elif account == 1:
            print(f'${self.saving} in saving')
            return self.saving
        else:
            return -1
