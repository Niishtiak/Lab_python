vozrast = int(input("Возраст: "))
dohod = float(input("Доход: "))
kredit = float(input("Сумма кредита: "))
srok = int(input("Срок: "))
istoriya = input("История (отличная/хорошая/удовлетворительная/плохая): ")
poruchiteli = input("Поручители (да/нет): ") == "да"
zalog = input("Залог (да/нет): ") == "да"

koeff = kredit / (dohod * srok)

print(f"Соотношение: {koeff:.2f}")

if istoriya == "плохая" or koeff > 0.5:
    print("Риск: критический")
    print("Ставка: -")
    print("Рекомендация: Отклонить")
elif koeff > 0.3:
    print("Риск: высокий")
    print("Ставка: 20%")
    print("Рекомендация: Одобрить с залогом")
elif koeff > 0.15:
    print("Риск: средний")
    print("Ставка: 15%")
    print("Рекомендация: Одобрить")
else:
    print("Риск: низкий")
    print("Ставка: 10%")
    print("Рекомендация: Одобрить")