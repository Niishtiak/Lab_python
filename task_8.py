import random

zagadka = random.randint(1, 100)

while True:
    popytka = int(input("Ваше число: "))
    if popytka < zagadka:
        print("Больше")
    elif popytka > zagadka:
        print("Меньше")
    else:
        print("Угадал!")
        break