"""
Class method and Static method
"""
class Person(object):
    
    kind = 'human'

    def __init__(self, name):
        self.name = name

    @classmethod
    def what_is_kind(cls):
        print(cls.kind)
    
    @staticmethod
    def about():
        print('about human')

Person.what_is_kind()
Person.about()
p = Person('Mike')
p.what_is_kind()
p.about()
