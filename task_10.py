sum = int(input("Введите сумму (число): "))
age = int(input("Введите ваш возраст: "))
hb = input("У вас день рождения? (да/нет): ")
vip = input("У вас вип?(да/нет): ")
skidka = 0

if vip == "да":
    skidka = 15
else:
    if sum > 1000:
        skidka += 10
    if age >= 63:
        skidka += 5
    if hb == "да":
        skidka += 5

if skidka > 25:
    skidka = 25

print(skidka)