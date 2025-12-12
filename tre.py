# def sum_factorials(num):
#
#
#     factorial = 1
#
#
#     total = 0
#
#     for i in range(1, num + 1):
#         factorial *= i
#         total += factorial
#     return total
#
# number = int(input("Number: "))
# fac_sum = sum_factorials(number)
# print("fac sum for", number, "is:", fac_sum)
#
# def menu(s):
#     s = int(input(""))
#     if s == 1:
#         text = int(input(""))
#         nam.extend([text])
#     elif s == 2:
#         n = float(input(
#             "введите что то хотели бы добавить в список  если это целое число введите 1 если число с плаваюшей точкой то 2 если текст 3 если булево значение то 4"))
#         if n == 1:
#             n = int(input(""))
#             nam.append(n)
#         elif n == 2:
#             n = float(input(""))
#             nam.append(n)
#         elif n == 3:
#             print(" 1 true or 2 false")
#             n = int(input(""))
#             if n == 1:
#                 nam.append(True)
#             elif n == 2:
#                 nam.append(False)
#             else:
#                 print("error")
#         elif n == 4:
#             n = input("")
#             nam.append(n)
#         else:
#             print("error")
#     else:
#         print("ошибка ввода пробуйте снова ")
#
#     return nam
from itertools import count
from multiprocessing.pool import worker
from operator import index
from os.path import split
from stringprep import in_table_c9

# nam = [5,6,6,7,8 ]
# print(nam)
# print("привет что ты хочешь с списком добвить одно значение или несколько 1 если хочешь много всего 2 если что то одно ")
# s = int(input(""))
# # print(menu(s))
# if s == 1:
#     text = int(input("Введите число, которое хотите добавить: "))
#     nam.extend([text])
# elif s == 2:
#     n = float(input("введите что то хотели бы добавить в список  если это целое число введите 1 если число с плаваюшей точкой то 2 если текст 3 если булево значение то 4"))
#     if n == 1:
#         n = int(input(""))
#         nam.append(n)
#     elif n == 2:
#         n = float(input(""))
#         nam.append(n)
#     elif n == 3:
#         print(" 1 true or 2 false")
#         n = int(input(""))
#         if n == 1:
#             nam.append(True)
#         elif n == 2:
#             nam.append(False)
#         else:
#             print("error")
#     elif n == 4:
#         n = input("")
#         nam.append(n)
#     else:
#         print("error")
# else:
#     print("ошибка ввода пробуйте снова ")
#
#     s = int(input(""))
#
#
#
# # nam.append(n)
# print(nam)

#
# numbers =[ 3,7,5]
#
# while True:
#
#  number = int(input('Новое число: '))
#
#  numbers.append(number)
#
#  print('Текущий список чисел:', numbers)
#
#  for i in numbers:
#
#    print(i ** 2, i ** 3, i ** 4)
#
#  print()


# nam = []
# for i in range(0, 101, 1):
#     nam.append(i)
#
# print(nam)

# worker = []
#
# id_workers = int(input("Сколько сотрудников работает? "))
#
#
# for i in range(id_workers):
#     work = int(input("Введите ID сотрудника: "))
#     worker.append(work)
#
#
# der = int(input("Кого ищем? Введите ID сотрудника: "))
#
#
# if der in worker:
#     print("Сотрудник работает")
# else:
#     print("Сотрудник не работает")





# plaer = [5 , 65 ,56, 23, 6,7]
# print(plaer)
# user = int(input("введите в списке игрока которому нужно увеличеть очки в 2 раза "))
# plaer[user] *= 2
# print(plaer)


# nums_list = []
#
# N = int(input('Кол-во чисел в списке: '))
#
# for _ in range(N):
#     num = int(input('Очередное число: '))
#
#     nums_list.append(num)
#
# maximum = nums_list[0]
# minimum = nums_list[0]
#
#
#
# for i in nums_list:
#
#     if maximum < i:
#         maximum = i
#
#     if minimum > i:
#         minimum = i
#
# print('Максимальное число в списке:', maximum)
#
# print('Минимальное число в списке:', minimum)
#
# nums = []
# summ = 0
# n = int(input("сколько чисел будент "))
# for i in range(n):
#     ns= int(input(" чисел  "))
#     nums.append(ns)
# k = int(input("введите кратное число "))
# for index, value in enumerate(nums):
#     if  value % k == 0:
#         summ = summ + index
# print(summ)





# Ввод количества собак
# n = int(input("Введите количество собак: "))

# Ввод очков каждой собаки
# scores = []
# for i in range(n):
#     points = int(input("Сколько очков у собаки ? "))
#     scores.append(points)
#
# print("Исходные очки:", scores)
#
# # Находим максимальное и минимальное значения
# max_value = max(scores)
# min_value = min(scores)
#
# # Находим их позиции в списке
# index_max = scores.index(max_value)
# index_min = scores.index(min_value)
#
# # Меняем местами минимальное и максимальное значение
# scores[index_min], scores[index_max] = scores[index_max], scores[index_min]
#
# print("Исправленные очки:", scores)


# word = input("Введите слово: ")
# sera = int(input("Введите номер символа для замены: "))
# num = input("Введите замену: ")
#
# s = ""
# count = 0
#
# for sym in word:
#     count += 1
#     if count != sera:
#         s += sym
#     else:
#         s += num
#
# print(s)

# word = input("Введите слово: ")
# sera = int(input("Введите номер символа для замены: "))
# num = input("Введите замену: ")
#
#
# sym_list = list(word)
# sym_list[sera - 1] = num
# for i in sym_list:
#     print(i, end=" ")
#






# words=[]
# counts = [0,0,0]
#
#
# for i in range(3):
#     print(i+1,'-',end='')
#     words.append(input())
# text = input()
# while text != 'end':
#     for index in range(3):
#         if words[index] == text:
#             counts[index] += 1
#     text = input()
# for i in range(3):
#     print(words[i] ,counts[i])



# text = "orrorrorororororororrorororor"
# print(text.replace("o","r"))

# n = 'hello world'
# print(n[0:5])

#
# s = input("Введите строку: ")
# new_s = ""
# count = 0
# for sym in s:
#     if sym == ':':
#         new_s += ";"
#
#         count += 1
#     else:
#         new_s += sym
# print(new_s, 'количество замен' , count)




# s = input('please text: ')
# num = int(input('please num in text: '))
#
# index = num - 1
# symbol = s[index]
#
# if index > 0:
#     left = s[index - 1]
# else:
#     left = None
#
# if index < len(s) - 1:
#     right = s[index + 1]
# else:
#     right = None
#
#
# count = 0
# if left == symbol:
#     count += 1
# if right == symbol:
#     count += 1
#
#
# print('Символ слева:', left if left else 'нет')
# print('Символ справа:', right if right else 'нет')
#
#
# if count == 0:
#     print('Таких же символов нет.')
# elif count == 1:
#     print('Есть ровно один такой же символ.')
# elif count == 2:
#     print('Есть два таких же символа.')


#
# text = input('Введите числа через запятую: ')  # например: 56,78,90
# text_list = text.split(',')  # разделяем строку по запятой
# text_list = [int(x) for x in text_list]  # превращаем строки в числа
# print(text_list)

#
#
# text = input('Введите слова через запятую: ')  # например: ty,hello,world
# text_list = text.split(',')  # ['ty', 'hello', 'world']
# print(text_list)



#
# text = []
# while True:
#     s = input('Введите число (или "end" для окончания): ')
#     if s == 'end':
#         break
#     text.append(int(s))
# print(text)


# text = []
# n = int(input('Сколько чисел добавить? '))
# for i in range(n):
#     num = int(input('Введите число: '))
#     text.append(num)
# print(text)


#
# text = []
# numbers = input("Введите числа через запятую: "),split(',')
# text.extend(numbers)
# print(text)
#
# #
# text = 'fdfbdifbdnfibdb'
# print(text[-1])

# top_re = ['python' , 'java' , 'js ' , 'sql']
# nam = int(input('nam c++'))
# top_re.insert(nam, 'c++')
# print(top_re)
#
# top_re = ['python' , 'java' , 'js ' , 'sql']
# nam = input('please name sleep c++')
# i_land = top_re.index(nam)
# top_re.insert(i_land+1 , 'c++')
# print(top_re)

# def zhek(muvi, list_films):
#     for i_muvi in list_films:
#         if i_muvi == muvi:
#             return True
#     return False
#
#
# films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
#          'Леон', 'Богемская рапсодия', 'Город грехов',
#          'Мементо', 'Отступники', 'Деревня',
#          'Проклятый остров', 'Начало', 'Матрица']
#
# my_films = []
#
#
# while True:
#     print('ваш текущий лист фильмов', my_films)
#     new_muvi = input('name films: ')
#
#     if zhek(new_muvi, films):
#         print('что хотите сделать: "добавить" "удалить" "вставить"')
#         comt = input('please command: ')
#
#         if comt == 'добавить':
#             my_films.append(new_muvi)
#
#         elif comt == 'удалить':
#             if zhek(new_muvi, my_films):
#                 my_films.remove(new_muvi)
#             else:
#                 print('error: нет такого фильма в вашем списке')
#
#         elif comt == 'вставить':
#             index = int(input('please index: '))
#             my_films.insert(index - 1, new_muvi)
#
#         else:
#             print('неизвестная команда')
#
#     else:
#         print('нет такого фильма в списке доступных, попробуйте снова')
#
#




# zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
# bear = input('new zoo ')
#
# zoo.insert(1 ,bear)
# zoo.remove('elephant')
# print(zoo)
# print('Лев сидит в клетке номер', zoo.index('lion') + 1)
# print('Обезьяна сидит в клетке номер', zoo.index('monkey') + 1)

# n = int(input('сколько сотрудников '))
# zp = []
# for _ in range(n):
#     zp.append(int(input('сколько они получают')))
#     print(zp)
# while 0 in zp:
#     zp.remove(0)
# print(zp)
# print('количество сотрудников  ',len(zp))
# print('максимум ',max(zp))
# print('минемум ' ,min(zp))
# #





#
# your = ['gbfgbfg', 'brtbrtbtr' , 'rtbrtbbrb']
# my = ['rtynrtn' , 'rtbrtbtb' , 'rtbtrtbrb']
# my.extend(your)
# print(my)

#
# error = []
# mydew = []
# countt = 0
#
#
# n = int(input(''))
# for i in range(n):
#     print('pacet nam ' , i+1)
#     for j in range(4):
#         print(j+1, end=' ')
#         nam = int(input(''))
#         error.append(nam)
#     if error.count(-1) <=1:
#         mydew.extend(error)
#     else:
#         print('max error')
#         countt += 1
#     error = []
# print(mydew)
# print(mydew.count(-1))
# print(countt)

# pack = []
# decode = []
# bad_packs = 0
#
# packs_amt = int(input('Кол-во пакетов: '))
#
# for i_pack_num in range(packs_amt):
#     print('\nПакет номер', i_pack_num + 1)
#
#     for i_bit in range(4):
#         print(i_bit + 1, 'бит:', end=' ')
#         num = int(input())
#         pack.append(num)
#
#     if pack.count(-1) <= 1:
#         decode.extend(pack)
#     else:
#         print('Много ошибок в пакете')
#         bad_packs += 1
#
#     pack = []
#
# print('\nПолученное сообщение:', decode)
# print('Кол-во ошибок в сообщении:', decode.count(-1))
# print('Кол-во потерянных пакетов:', bad_packs)



# main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
# first_company = [0, 0, 0]
# second_company = [1, 0, 0, 1, 1]
# third_company = [1, 1, 1, 0, 1]
# main.extend(first_company)
# main.extend(second_company)
# main.extend(third_company)
# print(main.count(0) , 'не выполненых задач ')


# n = input('one sms ')
# s = input('two sms ' )
# a = n.count('!') + n.count('?')
# b = s.count('!') + s.count('?')
#
# if a > b:
#     print(n,s)
# elif b > a:
#      print(s,n)
# else:
#     print('ойй')


error = []
prover = []
counter = 0
n = int(input('сколько будет покетов '))
for i in range(n):
    print(i+1 , end=' ')
    for bit in range(4):
        nam = int(input("введите бит "))
        error.append(nam)
        if error.count(-1) <=1:

            prover.extend(error)
        else:
            print("max error bit")
            counter += 1
        error = []
print(prover)
print(prover.count(-1))
print(counter)

# pack = []
# decode = []
# bad_packs = 0
#
# packs_amt = int(input('Кол-во пакетов: '))
#
# for i_pack_num in range(packs_amt):
#     print('\nПакет номер', i_pack_num + 1)
#
#     for i_bit in range(4):
#         print(i_bit + 1, 'бит:', end=' ')
#         num = int(input())
#         pack.append(num)
#
#     if pack.count(-1) <= 1:
#         decode.extend(pack)
#     else:
#         print('Много ошибок в пакете')
#         bad_packs += 1
#
#     pack = []
#
# print('\nПолученное сообщение:', decode)
# print('Кол-во ошибок в сообщении:', decode.count(-1))
# print('Кол-во потерянных пакетов:', bad_packs)




