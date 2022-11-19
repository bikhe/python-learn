year = int(input('Введи год: '))
birthyear = int(input('Введи год рождения: '))
month = int(input('Введи месяц: '))
birthmonth = int(input('Введи месяц рождения: '))


raznitsamonth = month-birthmonth
raznitsayear = year-birthyear

print('Вам', raznitsayear, "лет и", raznitsamonth, 'месяцев')