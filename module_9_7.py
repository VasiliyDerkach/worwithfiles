def sum_three(*args):
    s = 0
    for a in args:
        s+= a
    return s
def Is_Prime(fnc):
    def wrapper(*args):
        n = fnc(*args)
        d = 2
        while n % d != 0:
            d += 1
        if d == n:
            print('Простое')
        else:
            print('Составное')
        return n
    return wrapper

print(sum_three(3,80,9))
sum_three_dec = Is_Prime(sum_three)
print(sum_three_dec(2,3,6))