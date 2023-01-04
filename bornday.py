answer_year = input("Когда родился Пушкин?? Введите год рождения:")
bornyear = "1799"
bornday = "06.06."
if answer_year == bornyear:
    answer_day = input("Неплохо. А в какой день? Введите день рождения в формате day.month. :")
    if answer_day == bornday:
        print("Верно")
    else:
        print("Неверный день рождения")
else:
    print("Неверный год")
