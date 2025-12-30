# 3 зоданиe
liste = [1, 2, 3, 4, 5]
new_list = []
print(liste)
k = int(input('сколько здвигова сделать '))

new_list = liste[-k:] + liste[:-k]

print(liste)
print(new_list)