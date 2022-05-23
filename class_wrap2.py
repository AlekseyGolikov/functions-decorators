# Декорирование функции классом

# Как это работает:

# __init__ вызывается при оформлении some_function. 
# Опять же, помните, что декорирование — это то же самое, что 
# some_function = MyDecorator(some_function).

# __call__ вызывается, когда используется экземпляр класса, 
# например, при вызове функции. Поскольку some_function теперь 
# является экземпляром моего декоратора, 
# но мы все еще хотим использовать ее как функцию, 
# нам понадобится специальный метод __call__ .

class MyDecorator:
    def __init__(self,function):
        self.function = function
        self.counter = 0
    def __call__(self, *args, **kwargs):
        self.function(*args, **kwargs)
        self.counter += 1
        print(f"Called {self.counter} times")

@MyDecorator
def func():
    return 42

func()
func()
func()
