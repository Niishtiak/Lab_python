prodazhi = [
    {"name": "яблоко", "price": 10, "count": 5},
    {"name": "банан", "price": 15, "count": 3},
    {"name": "яблоко", "price": 10, "count": 2}
]

vyruchka = {}
for tovar in prodazhi:
    imya = tovar["name"]
    summa_tovara = tovar["price"] * tovar["count"]
    vyruchka[imya] = vyruchka.get(imya, 0) + summa_tovara

print(f"Выручка по товарам: {vyruchka}")

luchshiy = None
max_vyruchka = -1
for imya in vyruchka:
    if vyruchka[imya] > max_vyruchka:
        max_vyruchka = vyruchka[imya]
        luchshiy = imya

print(f"Самый прибыльный товар: {luchshiy}")
print(f"Уникальных товаров: {len(vyruchka)}")