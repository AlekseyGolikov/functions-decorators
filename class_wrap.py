# Декорирование функцией класса

# @нотация - это просто эквивалент записи MyClass = timer(MyClass), 
# т.е. декоратор будет вызван только тогда, когда «вызывается» класс,
# только для строки my_obj = MyClass().

# Методы класса не декорируются автоматически при декорации класса. 
# Проще говоря, при использовании декоратора для обычного класса декорируется 
# только его конструктор (метод __init__).

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"{func.__name__} took {runtime} sec.")
        return r
    return wrapper

@timer
class MyClass:
    def complex_calculation(self):
        time.sleep(1)
        return 42

my_obj = MyClass()
my_obj.complex_calculation()
