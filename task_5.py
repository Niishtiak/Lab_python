a = float(input("Число a: "))
b = float(input("Число b: "))

print(f"Сумма: {a + b}")
print(f"Разность: {a - b}")
print(f"Произведение: {a * b}")

if b != 0:
    print(f"Частное: {a / b}")
    print(f"Остаток: {a % b}")
else:
    print("Деление на ноль невозможно")

print(f"Степень: {a ** b}")