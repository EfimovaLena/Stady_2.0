import re
import sys
import os
import asyncio
from classes import *
def documentation():
    ''' Эта функция рассказывает про созданные классы и их методы'''
    list_for_documentation = [DNK(['AAA', 'CCC']), RNK('AAAAAAAA'), Nucleic_acids]
    for i in list_for_documentation:
        type_of_object = re.findall(r'\w+', str(type(i)))[2]
        print(f'Класс {type_of_object}. \nОписание класса: {i.__doc__}')
        new_method_list = [attribute for attribute in dir(i) if callable(getattr(i, attribute)) and attribute.startswith('__') is False]
        # attribute.startswith отфильтрует перегруженные методы
        # callable(getattr(i, attribute)) проверяет, что можно использовать как метод, чтобы отфильтровать поля
        print('Спсисок всех методов, включая наследуемые: ')
        for j in new_method_list:
            print(j, ' : ') #, j.__doc__
        print()
    return '--------end--------__'


async def instruction():
    print(f''' Здравствуй, {os.getlogin()}.
    Чтобы я записывал данные в файл, напишите полный путь к файлу.
    Чтобы я выводил результаты действий, напишите: keyboard.''')
    await asyncio.sleep(0)
    print('Чтобы сложить две цепочки РНК или две цепочки ДНК, напишите две цепочки через знак +. '
          '\nАналогично для произведения или равенства. '
          '\nЧтобы построить цепочку, комплиментарную цепочке РНК, напишите compliment(цепочка). '
          '\nЧтобы прочитать про классы и методы напишите "doc"')
    await asyncio.sleep(0)


def settings_of_input_and_output(function_for_work):
    def chto_to():
        try:
            output_way = input('Введите способ вывода: ')
            # Перенаправляем потоки, если надо работать с файлами
            flag_for_output = False
            if output_way != 'keyboard':
                flag_for_output = True
                stdout_fileno = sys.stdout
                sys.stdout = open(output_way, 'w')

            function_for_work()

            # Закрываем файлы, если открывали
            if flag_for_output:
                sys.stdout.close()
                sys.stdout = stdout_fileno

        except:
            print('Что-то пошло не так. Перезапустите программу.')
            exit(3)

    return chto_to


def one_step(vvod):
    try:
        if '+' in vvod:
            array = vvod.split('+')
            for i in range(len(array)):
                array[i] = array[i].strip()
            return convert(array[0]) + convert(array[1])
        if '*' in vvod:
            array = vvod.split('*')
            for i in range(len(array)):
                array[i] = array[i].strip()
            return convert(array[0]) * convert(array[1])
        if 'compliment(' in vvod:
            array = vvod[11:-1]
            return convert(array).build_dnk()
        if '=' in vvod:
            array = vvod.split('=')
            for i in range(len(array)):
                array[i] = array[i].strip()
            return convert(array[0]) == convert(array[1])
        if 'doc' in vvod:
            return documentation()
        else:
            print('Я вас не понимаю')
            exit(4)
    except:
        print('Я не смог обработать')
        exit(4)


def convert(vvod):
    try:
        if ',' in vvod:
            array = vvod.split(',')
            for i in range(len(array)):
                array[i] = array[i].strip()
            return DNK(array)
        else:
            return RNK(vvod)
    except:
        print('Я не смог конвертировать')
        exit(4)
