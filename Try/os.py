
import os

""" path = "D:\Андреев Роман\BankManager\BANK"


for path, dirname, filenames in os.walk(path):
    print(f" path - {path}")
    print(f" dirname - {dirname}")
    print(f" filename - {filenames}") """



path_one = os.getcwd()
path_lesson = os.path.join(path_one, r'lesson OS')

""" for i in range(1, 10):
    os.mkdir(path_lesson + f'\dir_{i}') """

for path in os.walk(path_lesson):
    print(f" path - {path}")