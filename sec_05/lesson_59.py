# generator

def greeting():
    print('##')
    yield 'Good morning'
    print('###')
    yield 'Good afternoot'
    print('####')
    yield 'Good night'
    print('#####')

g = greeting()
print(next(g))
print(next(g))
print(next(g))
