# 8 зодание
violator_songs = [

['World in My Eyes', 4.86],

['Sweetest Perfection', 4.43],

['Personal Jesus', 4.56],

['Halo', 4.9],

['Waiting for the Night', 6.07],

['Enjoy the Silence', 4.20],

['Policy of Truth', 4.76],

['Blue Dress', 4.29],

['Clean', 5.83]

]
print(violator_songs)
total_song = 0

n = int(input('сколько песень выберите '))
for _ in range(n):
    k = input('введите название песни ')
    count = 0

    for i in violator_songs :

        if k == i[0]:
            total_song += i[1]
            count += 1
    if count == 0:

        print('error name ')

print(total_song)