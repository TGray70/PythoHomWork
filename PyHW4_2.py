

lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
n = len(lst) - 1
i = 1
lst1 = []
while n > 0:
    if lst[i] > lst[i-1]:
        lst1.append(lst[i])
    n = n - 1
    i = i + 1
print(lst1)


