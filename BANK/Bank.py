from typing import Any
from Client import Client
from Account import DebitAcc, CreditAcc
from enum import Enum



class AccountType(Enum):
    CREDIT = 'credit'
    DEBIT = 'debit'



class Bank:
    def __init__(self, __name) -> None:
        self.__name = __name
        self.__client = []


    def add_client(self):
        client = Client.fill()
        self.__client.append(client)
        print (f'Add client {self.add_client}')
        return client

    def create_account(self):
        pass


class Singleton(type):
    _instances = {}

    def __call__(cls, *args,**kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class BankManager(metaclass=Singleton):
    def __init__(self) -> None:
        super().__init__()
        self.banks = []
        self.client_pool = {}

    def create_bank(self, name):
        self.banks.append(name)

    def create_client(self, client):
        self.client_pool[client.get_phone()] = client











        