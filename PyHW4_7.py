

def fact(n):
    f = 1
    for el in range(n):
        f = f * el
    yield f

for el in fact(4):
    print(el)
