# 1 зодание
# cart = []
# new_cart = []
# max_cart = 0
# n = int(input('сколько видео карт будет '))
# for i in range(n):
#     cart.append(int(input('введите пораметры карты ')))
# max_cart = max(cart)
# for j in cart:
#     if j != max_cart:
#         new_cart.append(j)
#
# print(cart)
# print(new_cart)


# 2 зодание

# films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия',
#          'Город грехов', 'Мементо', 'Отступники', 'Деревня']
# print(films)
# n = int(input('сколько фильмов хотите добвить к себе '))
# my_films = []
# for i in range(n):
#     film = input("name films ")
#     if film in films:
#         my_films.append(film)
#     else:
#         print('такого фильма нет, попробуйте еще раз')
#
# print(my_films)


# 3 зоданиe
# liste = [1, 2, 3, 4, 5]
# new_list = []
# print(liste)
# k = int(input('сколько здвигова сделать '))
#
# new_list = liste[-k:] + liste[:-k]
#
# print(liste)
# print(new_list)
#
# 4 зодание
# n = input('введите слова ')
# n = n.lower()
# if n == n[::-1]:
#     print("good")
# else:
#     print("bad")

# 5 зодание
# your_list = []
# n = int(input('сколько будет символав '))
# for i in range(n):
#     your_list.append(int(input('name please ')))
# print(your_list)
# for j in range(len(your_list)):
#     min_index = j
#     for k in range(j + 1, len(your_list)):
#         if your_list[k] < your_list[min_index]:
#             min_index = k
#     your_list[j], your_list[min_index] = your_list[min_index], your_list[j]
#
# print(your_list)

# 6 зодание
# list1 = [1, 3, 5, 7, 9]
# list2 = [2, 4, 5, 6, 8, 10]
#
# print(list1)
# print(list2)
# merges = []
# for i in list1:
#     if i not in merges:
#         merges.append(i)
# for j in list2:
#     if j not in merges:
#         merges.append(j)
# merges.sort()
# print(merges)


# 7 зодание
# shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100],
#         ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
# detail_name = input('name ')
# count = 0
# total = 0
#
#
#
# for i in shop:
#     if i[0] == detail_name:
#         count += 1
#         total += i[1]
# if count == 0 :
#     print('error')
# else:
#     print(count, ' count')
#     print(total , 'total summ')


# 8 зодание
# violator_songs = [
#
# ['World in My Eyes', 4.86],
#
# ['Sweetest Perfection', 4.43],
#
# ['Personal Jesus', 4.56],
#
# ['Halo', 4.9],
#
# ['Waiting for the Night', 6.07],
#
# ['Enjoy the Silence', 4.20],
#
# ['Policy of Truth', 4.76],
#
# ['Blue Dress', 4.29],
#
# ['Clean', 5.83]
#
# ]
# print(violator_songs)
# total_song = 0
#
# n = int(input('сколько песень выберите '))
# for _ in range(n):
#     k = input('введите название песни ')
#     count = 0
#
#     for i in violator_songs :
#
#         if k == i[0]:
#             total_song += i[1]
#             count += 1
#     if count == 0:
#
#         print('error name ')
#
# print(total_song)

# 9 зодание

# N = int(input('количество роликов'))
# rollers = []
# for _ in range(N):
#
#     rollers.append(int(input('размеров роликов')))
#
# K = int(input('количество людей'))
# feet = []
# for _ in range(K):
#
#     feet.append(int(input('размеров ног людей')))
#
#
# count = 0
# i = 0
# j = 0
# rollers.sort()
# feet.sort()
# while i < len(rollers) and j < len(feet):
#     if rollers[i] == feet[j]:
#         count += 1
#         i += 1
#         j += 1
#     elif rollers[i] < feet[j]:
#         i += 1
#     else:
#         j += 1
# print(count)

# 10 зодание
# n = int(input('Сколько людей: '))
# k = int(input('Какой по счёту выбывает: '))
#
# people = list(range(1, n+1))
# index_t = 0
#
# while len(people) > 1:
#     index_t = (index_t + k - 1) % len(people)
#     print('Выбывает человек под номером', people[index_t])
#     people.pop(index_t)
#
# print('Остался человек под номером ',people[0])



#11 зодание
#
# n = int(input('Количество чисел: '))
# seq = []
# for _ in range(n):
#     seq.append(int(input('Число: ')))
#
#
# add = []
#
#
# while seq != seq[::-1]:
#
#     add.insert(0, seq.pop())
#
#
# print('Последовательность:', seq + add)
# print('Нужно приписать чисел:', len(add))
# print('Сами числа:', add)

