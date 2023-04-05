
# ХОРОШАЯ ФУНКЦИЯ:
# читаемое название информацию получает в аргументах \ инф о возврате (->:str)
# короткая и читаемая макс 15 строк
#  Возвращение результата ( NO print \  Yes return )
#  Не зависима ( NO Global ) И не меняет ничего вне себя
#  Функция делает что-то одно

import random

def gener_pin(lenght:int)->str:
    return ''.join(str(random.randint(0, 9)) for _ in range(lenght))

def replace_five(a_list: list, value: str) -> list[str]:
    return [element.replace('5', value) for element in a_list]

def write_file(file_name: str, data: str):
    with open(file_name, 'w') as file:
        file.write(data)


if __name__ == '__main__':
    pins = [gener_pin(8) for _ in range(5)]
    pins_without_five = replace_five(pins, '6')
    str_list = '\n'.join(pins_without_five)
    print(pins_without_five)
    write_file('test_n.txt', str_list)
#  В результате получили более гибкую программу с возможностью изменять переменные