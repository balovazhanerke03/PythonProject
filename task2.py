# 2 зодание

films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия',
         'Город грехов', 'Мементо', 'Отступники', 'Деревня']
print(films)
n = int(input('сколько фильмов хотите добвить к себе '))
my_films = []
for i in range(n):
    film = input("name films ")
    if film in films:
        my_films.append(film)
    else:
        print('такого фильма нет, попробуйте еще раз')

print(my_films)