

str = input('Программа суммирует ваши числа. Введите цифры через пробел, нажав "Enter" получите их сумму, затем можете вводить ещё. Для остановки программы нажмите "q": ')
s = 0
a = True
while a == True:
    str = str.split()
    #num = []
    for i in str:
        if i == 'q':
            print('сумма = ', s)
            break
        s = s + float(i)
        #num.append(int(i))
    #s = s + sum(num)
    if i == 'q':
        break
    print('сумма = ', s)
    str = input('Вводим дальше, "q" - если надо закончить: ')
print("end")


