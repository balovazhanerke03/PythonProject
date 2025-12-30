# 7 зодание
shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100],
        ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
detail_name = input('name ')
count = 0
total = 0



for i in shop:
    if i[0] == detail_name:
        count += 1
        total += i[1]
if count == 0 :
    print('error')
else:
    print(count, ' count')
    print(total , 'total summ')