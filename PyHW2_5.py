
my_lst = [7,5,3,3,2]
num = int(input("Введите число: "))

i = 0
while i != 5:
    if num >= my_lst[i]:
        my_lst.insert(i, num)
        break
    elif i == 3:
        my_lst.append(num)
        break
    else:
        i = i + 1

print(my_lst)



