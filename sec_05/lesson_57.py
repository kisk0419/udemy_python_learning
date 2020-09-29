# decolator
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        r = func(*args, **kwargs)
        print('end')
        return r
    return wrapper

def print_more(func):
    def wrapper(*args, **kwargs):
        print('name:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        r = func(*args, **kwargs)
        print('result:', r)
        return r
    return wrapper

@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(2, 3)
print(r)