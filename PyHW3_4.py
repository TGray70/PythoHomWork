#print(2**-2)

def my_func(a, b):
    c = a ** b
    return c

def my_func2(a, b):
    b = b * -1
    a1 = 1
    while b != 0:
        a1 = a1 * a
        b = b - 1
        c = 1 / a1
    return c

fr = float(input('введите любое положительное число: '))
sc = int(input('введите любое целое отрицательное число: '))

print(round(my_func(fr, sc), 6))

print(round(my_func2(fr, sc), 6))
