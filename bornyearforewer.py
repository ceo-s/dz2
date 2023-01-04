done = False
right_answer = 1799
while done == False:
    answer = input("Когда родился Пушкин?? Введите год рождения:")

    if int(answer) == right_answer:
        done = True
        print("Верно")
    else:
        print("Неверно")
