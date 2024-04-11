from enum import Enum


class AccountType(Enum):
    DEBIT: 0
    CREDIT: 0



class Account:
    
    __account_amout = 0


    def __init__(self) -> None:
        Account.__account_amout += 1 
        self.id = Account.get_current_id()
        #self.id = hash(self)






    @staticmethod
    def get_current_id():
        Account.__account_amout += 1
        return Account.__account_amout
    


class DebitAcc(Account):
    
    def __init__(self, 
                 debit = 0) -> None:
        super().__init__()

        self.debit = debit




class CreditAcc(Account):

    def __init__(self,
                 default_credit = 1000) -> None:
        super().__init__()

        self.__client = default_credit