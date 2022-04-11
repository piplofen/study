count = int(input('Введите кол - во экспертов: '))
k = 0
k1 = 0
for x in range(count):
    k += 1
    q = input('Введите Qi для ' + str(k) + ' эксперта: ')
    T = 0
    k1 = 0
    for i in range(int(q)):
        k1 += 1
        t = int(input('Введите t' + str(k1) + 'i: '))
        C = t ** 3 - t
        T += C
    print('Ti = ' + str(T))
