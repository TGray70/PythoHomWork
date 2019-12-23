
str = input("Мне нужна от Вас фраза: ").split()
i = len(str)
print(i)
n = 0
nom = 1
while i !=0:
    if len(str[n]) > 10:
        a = list(str[n])
        for i in range(len(a) - 10):
            a.remove(a[10])
            mstr = ''.join(a)
        print(nom, mstr)
    else:
        print(nom, str[n])
    nom = nom + 1
    i = i - 1
    n = n + 1
#print('end')


#print(str, len(str))



