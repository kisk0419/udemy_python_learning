# list generator

g = (i for i in range(10))
print(type(g))

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# list tupple

g = tuple(i for i in range(10))
print(type(g))
print(g)