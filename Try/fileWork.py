import os
import mimetypes










class KakayaToHyeta(Exception):
    pass

def file_red(file_name:str) -> None:
    try:

        file = open(file_name, 'r')
        min_type, _ = mimetypes.guess_type(file_name)
        print(min_type)
        if min_type == 'application/json':
            raise KakayaToHyeta(f'не тот формат файла {file_name}')
        data = file.read()

    



    except FileNotFoundError:
        print(f'фаил {file_name} не найден')
    
    except UnicodeDecodeError:
        print('писец')
    




    except:
        pass

    finally:
        if "file" in locals(): #если файл есть и открылся, то он в финале ее закроет
            file.close()


if __name__ == '__main__':
   file_red('qwe.json')
