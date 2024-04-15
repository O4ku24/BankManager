from Client import Client






class Bank:
    def __init__(self, __name) -> None:
        self.__name = __name
        self.__client = []


    def add_client(self):
        client = Client.fill()
        self.__client.append(client)
        print (f'Add client {self.add_client}')

    def create_account(self):
        pass