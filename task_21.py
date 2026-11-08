import time

def timing(func):
    def wrapper(*args, **kwargs):
        nachalo = time.time()
        rez = func(*args, **kwargs)
        konec = time.time()
        print(f"Время работы {func.__name__}: {(konec - nachalo) * 1000} ms")
        return rez
    return wrapper

@timing
def calc():
    s = 0
    for i in range(100000):
        s += i
    return s

calc()