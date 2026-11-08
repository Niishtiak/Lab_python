import datetime

def log_calls(filename):
    def decorator(func):
        def wrapper(*args): 
            vremya = datetime.datetime.now()
            with open(filename, "a") as f:
                f.write(f"{vremya} - {func.__name__} - args: {args}\n")
            return func(*args)  
        return wrapper
    return decorator

@log_calls("test.txt")
def test(a, b):
    return a + b

print(f"Результат функции: {test(2, 3)}")