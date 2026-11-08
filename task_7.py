minuty = float(input("Минуты: "))
sms = float(input("СМС: "))
gigabajty = float(input("Инет (ГБ): "))

baza = 24.99
dop_min = max(0.0, minuty - 60) * 0.89
dop_sms = max(0.0, sms - 30) * 0.59

mb = max(0.0, gigabajty - 1.0) * 1024
dop_net = mb * 0.79

vsego_dop = dop_min + dop_sms + dop_net
nalog = (baza + vsego_dop) * 0.02
itogo = baza + vsego_dop + nalog

print(f"Базовая сумма: {baza:.2f}")

if dop_min > 0:
    print(f"Доп. минуты: {dop_min:.2f}")
if dop_sms > 0:
    print(f"Доп. СМС: {dop_sms:.2f}")
if dop_net > 0:
    print(f"Доп. интернет: {dop_net:.2f}")

print(f"Налог: {nalog:.2f}")
print(f"Итого к оплате: {itogo:.2f}")