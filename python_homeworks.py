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














# def sort_s(my_list):
#     for i_mn in range(len(my_list)):
#         for corr in range(i_mn, len(my_list)):
#             if my_list[corr] < my_list[i_mn]:
#                 my_list[corr], my_list[i_mn] = my_list[i_mn], my_list[corr]
# n = [3,4,5,7,9,2]
# sort_s(n)
#
# print(n)




#ЭТО ВАЖНО
# nam = [1, 2, 3, 4, 5]
#
# added = []
#
# for i in range(len(nam)):
#     left = nam[i:]
#     right = left[::-1]
#
#     if left == right:
#         added = nam[:i][::-1]
#         break
#
# result = nam + added
#
# print("Исходный список:", nam)
# print("Сколько добавили:", len(added))
# print("Добавили:", added)
# print("Результат:", result)


# n = int(input('введите начало '))
# b = int(input('введите конец '))
# list_top = [x **2 for x in range(n,b+1)]
# print(list_top)
# list_r = [x **3 for x in range(n,b+1)]
# print(list_r)




# n = input('Введите слово: ')
# b = input('вотрое ')
#
# ler = [x*2 for x in n]
#
#
# bers = [x*2 + b for x in n]
#
# print("ler:", ler)
# print("bers:", bers)
#




# def priced(percent, price):
#     return round(price * (1 + percent / 100), 2)
#
# shop = [1.09, 23.56, 57.84, 4.56, 6.78]
# one = int(input('повышение за первый год: '))
# two = int(input('за второй год повышение: '))
#
# one_t = [priced(one, price) for price in shop]
# two_t = [priced(two, price) for price in shop]
#
#
# print("Суммы:", round(sum(shop),2), round(sum(one_t),2), round(sum(two_t),2))


# a = int(input('введите первое число '))
# b = int(input('введите вотрое число '))
# list_s = [x for x in range(a, b+1) if x % 2 != 0]
#
# print(list_s)


#
# shopers = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# new_nams = [x if x > 0 else 0 for x in shopers]
# print(new_nams)


#
# import random
# taem_1 =[random.randint(50, 80)  for _ in range(10)]
# taem_2 = [random.randint(30, 60) for _ in range(10)]
#
# taem_3 = [("defid" if taem_1[i_demoge] + taem_2[i_demoge] > 100
#            else 'viktory' )
#           for i_demoge in range(10)]
# print('demoge 1: ', taem_1)
# print('demoge 2: ', taem_2)
# print('teams 3: ', taem_3)


# original_prices = [-12, 3, 5, -2, 1]
#
#
#
# new_prices = [x if x > 0 else 0 for x in original_prices]
#
#
#
# print("Мы потеряли: ",  sum(new_prices) - sum(original_prices))

#
# nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
# print(nums[:5])
# print(nums[:-2])
#
# print(nums[::2])
# print(nums[1::2])
# print(nums[::-1])
# print(nums[::-2])


# import random
#
# nums = [random.randint(1, 100) for _ in range(10)]
# print(nums)
# a = int(input('введите а '))
# b = int(input('введите б '))
# nums[a:b+1] = []
#
# print(nums)



# a = [1,2,3,4,5]
# b = [b * 2 for b in a ]
# print(b)



# a = [2,65,7,98,34,5,8,2,39]
# b = [b *2 for b in a if b < 10]
# print(b)


# words = ['welloy','happy','toper','bazilov' ,'hay']
# words_filters = [word for word in words if len(word) <= 3]
#
# print(words_filters)


 #
 # nam = int(input('введите число с которго начнем и будем убовлять по 0 '))
#
# for x in range(nam ,0 ,-1):
#     if x % 2 == 0:
#         print(x)

# nam = int(input('name please '))
# result = [x for x in range(nam , -1, -1) if x % 2 == 0]
# print(result)
#



#Зодание 1
# Список русских гласных
# vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
#
# # Запрос текста у пользователя
# text = input('Введите текст: ')
#
# # Генерация списка гласных
# vowels_in_text = [letter for letter in text.lower() if letter in vowels]
#
# # Вывод результатов
# print('Список гласных букв:', vowels_in_text)
# print('Длина списка:', len(vowels_in_text))
#




# 2 Задание
# k =  int(input('введите диапазон '))
#
#
# n = [1 if x % 2 == 0 else x % 5 for x in range(k)]
# print(n)
#


# 3 Задание
# import random
# taem_1 = [round(random.uniform(1, 20), 2) for _ in range(20)]
# taem_2 = [round(random.uniform(1, 20), 2) for _ in range(20)]
# team_viktoy = [taem_1[x] if taem_1[x] > taem_2[x] else taem_2[x] for x in range(20)]
# print(taem_1, 'первая команда')
# print(taem_2,'вторая команда ')
# print(team_viktoy , ' победители с обейх команд')

# 4 Задание
# alphabet = 'abcdefg'
# print(alphabet[:])
# print(alphabet[::-1])
# print(alphabet[::2])
# print(alphabet[1::2])
# print(alphabet[:1])
# print(alphabet[:-2:-1])
# print(alphabet[3:4])
# print(alphabet[-3:])
# print(alphabet[3:5])
# print(alphabet[-3:-5:-1])

# 5 Задание
# text = input('Введите строку:')
# first_h = text.index('h')
# last_h = text.rindex('h')
# finish = text[first_h+1:last_h]
# revers = finish[::-1]
# print(revers)
#
#6 Задание

# lister = []
# for row_index in range( 4):
#     dilerts = []
#     for column_index in range(3):
#         eliments = row_index + 1 + 4 * column_index
#         dilerts.append(eliments)
#     lister.append(dilerts)
# print(lister)

# 7 задание
# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# nice_list = [ w for row in nice_list for h in row for w in h]
# print(nice_list)

# 8 задание
# russian_alphabet = [
#     'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
#     'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ',
#     'ъ', 'ы', 'ь', 'э', 'ю', 'я'
# ]
#
# text = input('введите текст который хотите защывравать ')
# step = int(input('сколько здвигав '))
# encrypted_text = ""
#
# for char in text:
#     if char in russian_alphabet:
#         idx = russian_alphabet.index(char)
#         new_idx = (idx + step) % len(russian_alphabet)
#         new_char = russian_alphabet[new_idx]
#         encrypted_text += new_char
#     else:
#         encrypted_text += char
# print("Зашифрованное сообщение:", encrypted_text)


