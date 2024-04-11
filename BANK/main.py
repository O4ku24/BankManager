""" самостоятельная работа """

""" Есть несколько Банков, которые предоставляют финансовые услуги по операциям с деньгами.
В банке есть Счета и Клиенты. У клиента есть имя, фамилия, адрес и номер паспорта 
(имя и фамилия обязательны, остальное – опционально)"""

from Client import Client
from Bank import Bank




class Bank:
    def __init__(self, __name) -> None:
        self.__name = __name
        self.__client = []


    def add_client(self,__name):
        client = Client.fill()
        self.__client.append(client)








bank = Bank('VTB')

vova = bank.add_client('vova')

print(vova)




 