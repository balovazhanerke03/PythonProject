# 10 зодание
n = int(input('Сколько людей: '))
k = int(input('Какой по счёту выбывает: '))

people = list(range(1, n+1))
index_t = 0

while len(people) > 1:
    index_t = (index_t + k - 1) % len(people)
    print('Выбывает человек под номером', people[index_t])
    people.pop(index_t)

print('Остался человек под номером ',people[0])

