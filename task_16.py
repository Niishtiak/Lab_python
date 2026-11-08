def flatten_list(spisok):
    i = 0
    while i < len(spisok):
        if isinstance(spisok[i], list):
            sub = spisok.pop(i)
            flatten_list(sub)
            for item in reversed(sub):
                spisok.insert(i, item)
        else:
            i += 1

spisok_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
flatten_list(spisok_a)
print(f"Результат: {spisok_a}")