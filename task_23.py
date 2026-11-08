dohod = float(input("Доход: "))
zhile = float(input("Жилье: "))
eda = float(input("Еда: "))
transport = float(input("Транспорт: "))
razvlek = float(input("Развлечения: "))
drugoe = float(input("Другое: "))
vsego = zhile + eda + transport + razvlek + drugoe
ostatok = dohod - vsego
print(f"Доход: {dohod}")
print(f"Траты: {vsego}")
print(f"Остаток: {ostatok}")
if ostatok < 0:
    print("Минус! Сокращай расходы.")
elif ostatok < dohod * 0.1:
    print("Мало откладываешь.")
else:
    print("Норм бюджет!")

if razvlek > dohod * 0.3:
    print("Много на развлечения.")
if zhile > dohod * 0.5:
    print("Много за жилье.")