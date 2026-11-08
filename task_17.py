def merge_dicts(slovar1, slovar2):
    for k, v in slovar2.items():
        if k in slovar1 and isinstance(slovar1[k], dict) and isinstance(v, dict):
            merge_dicts(slovar1[k], v)
        else:
            slovar1[k] = v

dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}}
merge_dicts(dict_a, dict_b)
print(f"Результат: {dict_a}")