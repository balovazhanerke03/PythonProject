
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


