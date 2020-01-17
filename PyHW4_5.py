from functools import reduce

def m(el1, el2):
    return el1 * el2

l = [el for el in range(100, 1001) if el % 2 ==  0]

print(reduce(m, l))