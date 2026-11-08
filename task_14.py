nabor1 = input("Первый набор: ").split()
nabor2 = input("Второй набор: ").split()

obshchie = []
for x in nabor1:
    if x in nabor2 and x not in obshchie:
        obshchie.append(x)

tolko_v_1 = []
for x in nabor1:
    if x not in nabor2 and x not in tolko_v_1:
        tolko_v_1.append(x)

tolko_v_2 = []
for x in nabor2:
    if x not in nabor1 and x not in tolko_v_2:
        tolko_v_2.append(x)

raznitsa = []
for x in tolko_v_1:
    raznitsa.append(x)
for x in tolko_v_2:
    raznitsa.append(x)

print(f"В обоих одновременно: {obshchie}")
print(f"Из 1-го отсутствуют во 2-м: {tolko_v_1}")
print(f"Из 2-го отсутствуют в 1-м: {tolko_v_2}")
print(f"Исключая общий набор: {raznitsa}")