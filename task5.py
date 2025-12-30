# 5 зодание
your_list = []
n = int(input('сколько будет символав '))
for i in range(n):
    your_list.append(int(input('name please ')))
print(your_list)
for j in range(len(your_list)):
    min_index = j
    for k in range(j + 1, len(your_list)):
        if your_list[k] < your_list[min_index]:
            min_index = k
    your_list[j], your_list[min_index] = your_list[min_index], your_list[j]

print(your_list)
