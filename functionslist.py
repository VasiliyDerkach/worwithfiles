def apply_all_func(int_list, *functions):
    result = {}
    for calc in functions:
        result[calc.__name__] = calc(int_list)
    return result

if __name__ == '__main__':
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))