"""
Abstruct class
"""

import abc

class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age
    
    @abc.abstractmethod
    def drive(self):
        pass

class Baby(Person):
    def drive(self):
        raise Exception('No drive')

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError()
    
    def drive(self):
        print('Ok')
    
baby= Baby()
adult = Adult()
