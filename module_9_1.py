def apply_all_func(int_list: (int, float), *functions):

    results = {}

    for item in functions:
        new = item(int_list)
        results[item.__name__] = new
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))