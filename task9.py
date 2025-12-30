 # 9 зодание

N = int(input('количество роликов'))
rollers = []
for _ in range(N):

    rollers.append(int(input('размеров роликов')))

K = int(input('количество людей'))
feet = []
for _ in range(K):

    feet.append(int(input('размеров ног людей')))


count = 0
i = 0
j = 0
rollers.sort()
feet.sort()
while i < len(rollers) and j < len(feet):
    if rollers[i] == feet[j]:
        count += 1
        i += 1
        j += 1
    elif rollers[i] < feet[j]:
        i += 1
    else:
        j += 1
print(count)
