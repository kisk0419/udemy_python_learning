"""
Special methods
"""
class Word(object):
    def __init__(self, word):
        self.word = word
    
    def __str__(self):
        return f'Word. {self.word}'
    
    def __len__(self):
        return len(self.word)
    
    def __eq__(self, word):
        return self.word.lower() == word.word.lower()

a = Word('aaa')
b = Word('bbb')
a2 = Word('aaa')

print(a, b, a2)
print(len(a))
print(a == b)
print(a == a2)