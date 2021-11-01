date, month = input("Введите дату и месяц рождения через пробел: ").split()
date, month = int(date), int(month)

if (22 <= date <= 31 and month == 3) or (1 <= date <= 21 and month == 4):
    print("Овен")
elif (22 <= date <= 30 and month == 4) or (1 <= date <= 21 and month == 5):
    print("Телец")
elif (22 <= date <= 31 and month == 5) or (1 <= date <= 21 and month == 6):
    print("Близнецы")
elif (22 <= date <= 30 and month == 6) or (1 <= date <= 21 and month == 7):
    print("Рак")
elif (22 <= date <= 31 and month == 7) or (1 <= date <= 21 and month == 8):
    print("Лев")
elif (22 <= date <= 31 and month == 8) or (1 <= date <= 21 and month == 9):
    print("Дева")
elif (22 <= date <= 30 and month == 9) or (1 <= date <= 21 and month == 10):
    print("Весы")
elif (22 <= date <= 31 and month == 10) or (1 <= date <= 21 and month == 11):
    print("Скорпион")
elif (22 <= date <= 30 and month == 11) or (1 <= date <= 21 and month == 12):
    print("Стрелец")
elif (22 <= date <= 31 and month == 12) or (1 <= date <= 21 and month == 1):
    print("Козерог")
elif (22 <= date <= 31 and month == 1) or (1 <= date <= 21 and month == 2):
    print("Водолей")
elif (22 <= date <= 29 and month == 2) or (1 <= date <= 21 and month == 3):
    print("Рыбы")
else:
    print("Неправильно введена дата.")
