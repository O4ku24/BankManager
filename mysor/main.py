""" 
ООП - Обьектно орентированое програмирование.

 """
import time
class car():
    def drive(self):
        pass

    def stop(self):
        pass

class animal():
    def __init__(self, name, age, color) -> None:
        self.name = name
        self.age = age
        self.color = color

    def eat(self):
        pass

    def sleep(self):
        time.sleep(2)
        print(f'{self.name} поспал')

dog = animal("Roman", 33, "white")

class Marker():
    def __init__(self, color) -> None:
        self.color = color

    def write(self, word):
        return f'Маркер написал {word} {self.color} цветом'
    
marker_red = Marker('Red')
marker_blue = Marker('Blue')

class User():
    def __init__(self, login, password) -> None: #дандар метов
        self.__login = login
        self.__password = password

    def get_login(self): #метод
        return f'User {self.__login} = {self.__login}'
    
    def get_password(self):#метод
        return f'User {self.__login} passwprd = {self.__password}'
    
    def create_login(self, login):#метод
        self.__login = login
        return f'New Login {self.__login}'
    
    def create_password(self, password):#метод
        self.login = password
        return f'New Password {self.__password}'
    

user1 = User('Roman', 'Password')

class Human:
    def __init__(self, name, age, phone, siti, country, address) -> None:
        self.name = name
        self.age = age
        self.phone = phone
        self.siti = siti
        self.country = country
        self.adress = address

    def get_human(name, age, phone, siti, country, address):
        pass




    def create_human(name, age, phone, siti, country, address):
        pass



class Drob:
    def __init__(self, numerator, denominator) -> None:
        self.__numerator = numerator
        self.__denominator = denominator

    def output_fanc(self):
        return f'{self.__numerator}/{self.__denominator}'
    
    def get_numerator(self):
        return self.__numerator
    
    def get_denominator(self):
        return self.__denominator
    
    def sum(self, other_fanc):
        pass
















