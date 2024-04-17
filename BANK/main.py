
from Client import Client
from Bank import Bank, BankManager, AccountType
from Account import DebitAcc, CreditAcc











bm = BankManager()
bm.create_bank('VTB')
print(bm.banks)

user_one = Client.fill()

print(user_one)









 