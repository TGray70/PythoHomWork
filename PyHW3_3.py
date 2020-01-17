

def my_func(a, b, c):
    lst = [a, b, c]
    print(lst)
    frst = int(max(lst))
    print(frst)
    i = lst.index(frst)
    del lst[i]

    print(lst)
    scnd = max(lst)
    print(scnd)

    return frst + scnd

print(my_func(4, 9, 3))

