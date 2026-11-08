amount = int(input("Введите сумму в рублях (целое число): "))

p100 = amount // 100
amount %= 100

p50 = amount // 50
amount %= 50

p10 = amount // 10
amount %= 10

p5 = amount // 5
amount %= 5

p2 = amount // 2
p1 = amount % 2

print("Для размена потребуется:")
print(f"Купюр по 100 руб: {p100}")
print(f"Купюр по 50 руб: {p50}")
print(f"Купюр по 10 руб: {p10}")
print(f"Монет по 5 руб: {p5}")
print(f"Монет по 2 руб: {p2}")
print(f"Монет по 1 руб: {p1}")