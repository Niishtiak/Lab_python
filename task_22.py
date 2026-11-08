def type_check(*tipy):
    def decorator(func):
        def wrapper(*args):
            for i in range(len(args)):
                if not isinstance(args[i], tipy[i]):
                    raise TypeError(f"Аргумент {i+1} должен быть типа {tipy[i].__name__}, а получен {type(args[i]).__name__}")
            return func(*args)
        return wrapper
    return decorator

@type_check(int, int)
def add(a, b):
    return a + b

print(f"Результат: {add(5.5, 10)}")