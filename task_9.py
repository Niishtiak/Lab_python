tip = input("Тип (длина/масса): ")
ot_kuda = input("Из единицы (м/км/см/кг/г): ")
kuda = input("В единицу (м/км/см/кг/г): ")
znach = float(input("Значение: "))

rez = znach

if tip == "длина":
    if ot_kuda == "км":
        metry = znach * 1000
    elif ot_kuda == "см":
        metry = znach / 100
    else:
        metry = znach

    if kuda == "км":
        rez = metry / 1000
    elif kuda == "см":
        rez = metry * 100
    else:
        rez = metry
elif tip == "масса":
    if ot_kuda == "кг":
        grammy = znach * 1000
    else:
        grammy = znach

    if kuda == "кг":
        rez = grammy / 1000
    else:
        rez = grammy

print(f"Результат: {rez}")