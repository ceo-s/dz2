TOLSTOY = {"name": "Лев Толстой", "age": 1828} 
BALE = {"name": "Кристиан Бейл", "age": 1974}
KNYAZ = {"name": "Князь Владимир", "age": 958}
MIAMOTO = {"name": "Миямото Мусаси", "age": 1584}
TYSON = {"name": "Майк Тайсон", "age": 1966}

list = [TOLSTOY, BALE, KNYAZ, MIAMOTO, TYSON]

counter = 0
polling = True 

while polling == True:
    for person in list:
        answer = input(f"Напиши год рождения для {person['name']}:")
        if str(person["age"]) == answer:
            print("Молодец!")
            counter += 1
        else:
            print("Ну, почти...")
    print("Викторина пройдена. Ваш рейтинг:", f"{counter}/{len(list)}  ({len(list)-counter} ошибок)", f"Процент правильных ответов - {counter/len(list)*100}%. Неправильных - {100 - counter/len(list)*100}%")
    answer = input("Хотите пройти викторину заново? ДА/НЕТ:")
    if answer == "ДА":
        counter = 0
    else:
        print("До новых встреч!")
        polling = False