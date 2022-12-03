import re
import sys
import os
import asyncio
from classes import *
from chatterbox import *
if __name__ == "__main__":
    corutina = instruction()
    print('Работаю с файлом input.txt. \n'
          'Я прочитаю из него входные данные и запишу их в файл output.txt \n'
          'А еще я выведу результаты на экран. \n')
    input_way = open('input.txt', 'r')
    output_way =  open('output.txt', 'w')
    for line in input_way:
        print(f'''Введено: {line} \n Результат: {one_step(line.strip())}''')
        result = one_step(line.strip())
        output_way.write(str(result)+'\n')
    print('Справка по классам')
    documentation()
    input_way.close()
    output_way.close()
