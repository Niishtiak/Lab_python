def unique_elements(vlozhenny_spisok):
    ploskiy = []
    def helper(l):
        for item in l:
            if isinstance(item, list):
                helper(item)
            else:
                ploskiy.append(item)
    helper(vlozhenny_spisok)

    rez = []
    for x in ploskiy:
        if x not in rez:
            rez.append(x)
    return rez

list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print(f"Результат: {unique_elements(list_a)}")