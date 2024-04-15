

class Client:
    def __init__(self,
                 last_name,
                 first_name,
                 phone,
                 addres=None,
                 passport=None, 
                 
                ) -> None:
        self.__last_name = last_name
        self.__first_name = first_name
        self.__addres = addres
        self.__passport = passport
        self.__phone = phone
        self.__account = []


    @staticmethod
    def fill():
        first_name = input('Enter fisrt name: ')
        last_name = input('Enter last name: ')
        addres = input('Enter addres: ')
        passport = input('Enter passport: ')
        phone = input('Enter phone: ')
        return Client(first_name, last_name, addres, passport, phone)
    


