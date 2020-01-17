
def delit(n, m):
    return n / m

a = int(input('First number: '))
b = int(input('Second number: '))
while b == 0:
    b = int(input('Second number, no zero: '))

print(round(delit(a, b), 3))
