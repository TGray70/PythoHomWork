from collections import Counter

lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
lst1 = []
for el in lst:
    if lst.count(el) > 1:
        lst1 = lst1.append(el)

print(lst1)