
num_1:int = int(input('Enter num 1: '))
num_2:int = int(input('Enter num 2: '))

class GovnoCodeError(Exception):
    pass

try:
    if num_1 == 0:
        raise GovnoCodeError('Num_1 = 0')
    print('деление')

finally:
    print('finalli')








