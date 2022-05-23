import time

def decorator(func):
    def wrapper():
        tik = time.perf_counter()
        func()
        tok = time.perf_counter()
        print(f"Функция была выполнена за {tok-tik:0.4f} секунд")
    return wrapper

@decorator
def basic():
    s = input("Введите строку: ")

print('старт программы')
basic()
print('конец программы')