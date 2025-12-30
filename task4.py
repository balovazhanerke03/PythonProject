# 4 зодание
n = input('введите слова ')
n = n.lower()
if n == n[::-1]:
    print("good")
else:
    print("bad")