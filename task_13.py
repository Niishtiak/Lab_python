vvod = input("Введите числа: ").split()
chisla = []
for x in vvod:
    if "." in x:
        chisla.append(float(x))
    else:
        chisla.append(int(x))

schet = {}
for n in chisla:
    schet[n] = schet.get(n, 0) + 1

unikalnye = []
povtoryayushchiesya = []
for n in schet:
    if schet[n] == 1:
        unikalnye.append(n)
    else:
        povtoryayushchiesya.append(n)

print(f"Уникальные: {unikalnye}")
print(f"Повторяющиеся: {povtoryayushchiesya}")

chetnye = []
nechetnye = []
for n in chisla:
    if int(n) % 2 == 0:
        chetnye.append(n)
    else:
        nechetnye.append(n)

print(f"Четные: {chetnye}, Нечетные: {nechetnye}")

otr = []
for n in chisla:
    if n < 0:
        otr.append(n)
print(f"Отрицательные: {otr}")

drobi = []
for n in chisla:
    if isinstance(n, float):
        drobi.append(n)
print(f"С плавающей точкой: {drobi}")

summa_5 = 0
for n in chisla:
    if n % 5 == 0:
        summa_5 += n
print(f"Сумма кратных 5: {summa_5}")

max_chislo = chisla[0]
min_chislo = chisla[0]
for n in chisla:
    if n > max_chislo:
        max_chislo = n
    if n < min_chislo:
        min_chislo = n

print(f"Максимальное: {max_chislo}")
print(f"Минимальное: {min_chislo}")