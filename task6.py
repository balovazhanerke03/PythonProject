# 6 зодание
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]

print(list1)
print(list2)
merges = []
for i in list1:
    if i not in merges:
        merges.append(i)
for j in list2:
    if j not in merges:
        merges.append(j)
merges.sort()
print(merges)
