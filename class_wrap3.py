# Декорирование класса в Python работает как изменение класса извне (т.е. из декоратора)

# Опять же, вспомним определение декоратора, ведь все, 
# что здесь происходит, следует той же логике:
# my_obj = MyClass() сначала вызывает декоратор,
# Декоратор add_calc добавляет метод calc к классу
# В итоге класс создается с помощью конструктора.

def add_calc(target):

    def calc(self):
        return 42

    target.calc = calc
    return target

@add_calc
class MyClass:
    def __init__(self):
        print("MyClass __init__")

my_obj = MyClass()
print(my_obj.calc())
