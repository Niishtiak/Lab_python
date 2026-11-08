def cache(func):
    kesh = {}
    def wrapper(*args):
        if args not in kesh:
            kesh[args] = func(*args)
        return kesh[args]
    return wrapper

@cache
def add(a, b):
    return a + b

print(f"Результат 1: {add(2, 3)}")
print(f"Результат 2: {add(2, 3)}")