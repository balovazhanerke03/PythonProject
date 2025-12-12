# matrix = [[1, 2 ,3], [4, 5, 6], [7, 8, 9]]
# for row in matrix:
#     for col in row:
#         print(col, end=" ")
#     print()

# mun = 1
# martix = []
# nam = int(input('количество команд '))
# for _ in range(nam // 3):
#     martix.append(list(range(mun,mun+3)))
#     mun += 3
# print(martix)
# for i in mem:
#     for b in i:
#         print(b , end=" ")
# mem = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in mem:
#     for b in i:
#         print(b, end=" ")
#     print()
#
# words=[[' ',0],[' ',0],[' ',0]]
#
#
#
# for i in range(3):
#     print(i+1,'-',end='')
#     word = input()
#     words[i][0] = word
# text = input()
# while text != 'end':
#     for index in range(3):
#         if words[index][0] == text:
#             words[index][1] += 1
#     text = input()
# for i in range(3):
#     print(words[i][0] ,words[i][1])







#
# mun = 1
# martix = []
# nam = int(input('количество команд '))
# for _ in range(nam // 3):
#     martix.append(list(range(mun,mun+3)))
#     mun += 3
# print(martix)
# for _ in martix:
#     for b in _:
#         print(b, end=' ')
#     print()
# mem = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in mem:
#     for b in i:
#         print(b , end=' ')
#     print()



#
# comand = []
# n = int(input('сколько людей '))
# k = int(input('на сколько команд разделить '))
#
# # comand = list(range(1,n+1))
# comand = []
# if n % k != 0:
#     print("Невозможно поделить на команды по", k)
#
# # comands = []  # пустой список для команд
# num = 1
# for i in range(n // k):
#     comand.append(list(range(num, num + k)))
#     num += k
#
# print('comand', comand)






# n = int(input('Сколько всего людей: '))
# k = int(input('На сколько команд разделить: '))
#
# if n % k != 0:
#     print("Невозможно разделить", n, "человек на", k, "команд без остатка")
# else:
#     comand = []
#     people_in_team = n // k   # сколько человек в одной команде
#     num = 1
#
#     for i in range(k):  # именно k команд
#         comand.append(list(range(num, num + people_in_team)))
#         num += people_in_team
#
#     print('comand', comand)



goods = [
 ["яблоки", 50],
 ["апельсины", 190],
 ["груши", 100],
 ["нектарины", 200],
 ["бананы", 77]
]
print(goods)
frikt_name = input("name new frikt")
prise = int(input("prise"))
goods.append([frikt_name, prise])
print(goods)
for i in goods:
    i[1] *= 1.08

print(goods)


