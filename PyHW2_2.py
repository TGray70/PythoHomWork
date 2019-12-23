mylist1 = []
a = 0
while a != "n":
    a = input('Введите что-нибудь в список. Когда надоест введите "n": ')
    mylist1.append(a)
mylist1.remove('n')

print("Ваш лист: ", mylist1)
n = len(mylist1)
i = n // 2
while i !=  0:
    x = mylist1[i * 2 - 1]
    #print(x)
    mylist1.remove(mylist1[i * 2 - 1])
    #print(mylist1)
    mylist1.insert(i * 2 - 2, x)
    #print(mylist1)
    i = i - 1

print("end")
print("Ваш лист после моей работы: ", mylist1)

