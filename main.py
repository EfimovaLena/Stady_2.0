import re
import sys
import os
import asyncio
from classes import *
from chatterbox import *
if __name__ == "__main__":
    corutina = instruction()
    corutina.send(None)
    @settings_of_input_and_output
    def main():
        corutina.send(None)
        input_value = input()
        while input_value != '0':
            print('Результат: ', one_step(input_value.strip()))
            input_value = input()
    main()
