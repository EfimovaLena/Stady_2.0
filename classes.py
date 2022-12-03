import re
import sys
import os
import asyncio
from abc import ABC, abstractmethod
import random

class Nucleic_acids(ABC):
    '''Этот класс описывает объекты, относящиеся к нуклеиновым кислотам.
       Attributes
       ----------

       Abstract Methods
       ----------------
       check()
            Проверяет, что можно создать запрашиваемую нуклеиновую кислоту
       Methods
       -------
       compliment()
            Строит цепочку, комплиментарную переданной

    '''
    @abstractmethod
    def __getitem__(self, item):
        pass
    @abstractmethod
    def __add__(self, other):
        pass
    @abstractmethod
    def __iter__(self):
        pass
    @abstractmethod
    def __len__(self):
        pass
    @abstractmethod
    def check(self, amino_acids):
        ''' Метод проверяет, что в переданная последовательность аминокислот является допустимой для данного типа нуклеиновых кислот. '''
        try:
            for i in self:
                if i not in amino_acids:
                    raise ValueError
        except ValueError:
            print(f'Во веденной цепочке: {self} присутсвует недопустимый символ')
            exit(1)
    def compliment(self):
        ''' Метод осуществляет выбор комплиментарного "звена цепочки" (одна аминоклислота) к переданной аминокислоте из ДНК'''
        compl = ''
        for i in self:
            compl += 'A' if i == 'T' else ('T' if i == 'A' else ('C' if i == 'G' else 'G'))
        return compl
    def __eq__(self, other):
        '''Метод осуществляет проверку равенства двух кислот одного типа. '''
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True


class RNK(Nucleic_acids):
    '''Этот класс описывает объект типа РНК. (Допустимые аминокислоты:  'A', 'U', 'G', 'C')
       Attributes
       ----------
       subs : str
            Последовательность аминокислот
       Methods
       -------
       check()
            Проверяет, что переданные строки описывают цепочку РНК
       build_dnk()
            Строит по текущей цепочке РНК соответствующую ей цепочку ДНК
    '''
    def check(self):
        '''Этот метод перегружает родительский метод проверки'''
        super().check(['A', 'U', 'G', 'C'])
    def __iter__(self):
        for x in self.subs:
            yield x
    def __getitem__(self, i):
        return self.subs[i]
    def __len__(self):
        return len(self.subs)
    def __add__(self, other):
        try:
            return str(self) + str(other)
        except:
            print('Такое складывать нельзя')
            exit(2)
    def __str__(self):
        return self.subs
    def __mul__(self, other):
        multiplication = ''
        for i in range(min(len(self), len(other))):
            multiplication += random.choice([self[i], other[i]])
        multiplication += str(self)[i+1::] if len(self) > len(other) else str(other)[i+1::]
        return RNK(multiplication)
    def build_dnk(self):
        '''Этот метод строит по цепочке РНК двух цепочек, составляющих один объект ДНК'''
        first_chain = self.compliment()
        second_chain = ''
        for i in first_chain:
            second_chain += 'A' if i == 'T' else ('T' if i == 'A' else ('C' if i == 'G' else 'G'))
        return DNK([first_chain, second_chain])
    def __init__(self, chain):
        self.subs = chain
        self.check()
        print('Создана одна цепочка РНК: ', str(self))


class DNK(Nucleic_acids):
    '''Этот класс описывает объект типа ДНК. (Допустимые  аминокислоты:  'A', 'T', 'G', 'C')
       Attributes
       ----------
       sub1 : str
            Последовательность аминокислот
       sub1 : str
            Последовательность аминокислот
       Methods
       -------
       check()
            Проверяет, что переданные строки описывают цепочку ДНK
    '''
    def check(self):
        '''Этот метод переопределяет родительский метод проверки. '''
        if len(self.sub1) != len(self.sub2):
            print('В ДНК аминокислоты должны быть парными')
            exit(1)
        super().check([(a, b) for a in ['A', 'T', 'G', 'C'] for b in ['A', 'T', 'G', 'C']])

    def __str__(self):
        return str(self.sub1) + ', ' + str(self.sub2)
    def __add__(self, other):
        return DNK([str(self.sub1)+str(other.sub1), str(self.sub2)+str(other.sub2)])
    def __len__(self):
        if len(self.sub1) == len(self.sub2):
            return len(self.sub2)
    def __mul__(self, other):
        first_self = self.sub1
        first_other = other.sub1
        multiplication = ''
        for i in range(min(len(first_self), len(first_other))):
            multiplication += random.choice([first_self[i], first_other[i]])
        multiplication += str(first_self)[i::] if len(first_self) > len(first_other) else str(first_other)[i::]
        compl = ''
        for i in multiplication:
            compl += 'A' if i == 'T' else ('T' if i == 'A' else ('C' if i == 'G' else 'G'))
        return DNK([multiplication, compl])
    def __getitem__(self, item):
        return (self.sub1[item], self.sub2[item])
    def __iter__(self):
        for x in self.sub1:
            for y in self.sub2:
                yield x, y
        return str(self.sub1), str(self.sub1)
    def __init__(self, chains):
        self.sub1 = chains[0]
        self.sub2 = chains[1]
        self.check()
        print('Создана одна цепочка ДНК: ', self.sub1, self.sub2)
