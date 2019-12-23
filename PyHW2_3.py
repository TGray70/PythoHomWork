

n = int(input("Введите номер месяца, который вы любите: "))
wntr = [12, 1, 2]
sprn = [3, 4, 5]
smmr = [6, 7, 8]
otmn = [9, 10, 11]

if n in wntr:
    print("Вы любите зиму!")
elif n in sprn:
    print("Вы любите весну!")
elif n in smmr:
    print("Вы любите лето!")
else:
    print('Вы любите осень!')

print('end')



