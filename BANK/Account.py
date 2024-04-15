from enum import Enum


class AccountType(Enum):
    DEPOZIT : 0
    DEBIT: 0
    CREDIT: 0



class Account:
    
    __account_amout = 0


    def __init__(self) -> None:
    
        self.id = hash(self)
        self.__debit = 0


    


class DebitAcc(Account):
    
    def __init__(self, 
                 __debit = 0) -> None:
        super().__init__()

        self.__debit = __debit




class CreditAcc(Account):

    def __init__(self,
                 default_credit = 100000) -> None:
        super().__init__()

        self.__credit = default_credit