# 1 зодание
cart = []
new_cart = []
max_cart = 0
n = int(input('сколько видео карт будет '))
for i in range(n):
    cart.append(int(input('введите пораметры карты ')))
max_cart = max(cart)
for j in cart:
    if j != max_cart:
        new_cart.append(j)

print(cart)
print(new_cart)
