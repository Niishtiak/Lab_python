tekst = input("Введите текст: ")
slova = tekst.split()

print(f"Всего слов: {len(slova)}")

chastota = {}
for slovo in slova:
    chastota[slovo] = chastota.get(slovo, 0) + 1

print(f"Частота слов: {chastota}")

samoe_chastoe = slova[0] if slova else ""
for slovo in chastota:
    if chastota[slovo] > chastota[samoe_chastoe]:
        samoe_chastoe = slovo
print(f"Самое частое слово: {samoe_chastoe}")

korotkoe = slova[0]
dlinnoe = slova[0]
for slovo in slova:
    if len(slovo) < len(korotkoe):
        korotkoe = slovo
    if len(slovo) > len(dlinnoe):
        dlinnoe = slovo

print(f"Самое короткое: {korotkoe}")
print(f"Самое длинное: {dlinnoe}")

filtr = []
for slovo in slova:
    if len(slovo) >= 3:
        filtr.append(slovo)

print(f"Слова от 3 символов: {filtr}")