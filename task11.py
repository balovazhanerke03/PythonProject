
#11 зодание

n = int(input('Количество чисел: '))
seq = []
for _ in range(n):
    seq.append(int(input('Число: ')))


add = []


while seq != seq[::-1]:

    add.insert(0, seq.pop())


print('Последовательность:', seq + add)
print('Нужно приписать чисел:', len(add))
print('Сами числа:', add)
