
bornyear = "1799"
bornday = "06.06."

keep_asking = True

while keep_asking == True:
    answer_year = input("Когда родился Пушкин?? Введите год рождения:")
    if answer_year == bornyear:
        while keep_asking == True:
            answer_day = input("Неплохо. А в какой день? Введите день рождения в формате day.month. :")
            if answer_day == bornday:
                keep_asking = False    
                print("Верно")
            else:
                print("Неверный день рождения")
    else:
        print("Неверный год")
