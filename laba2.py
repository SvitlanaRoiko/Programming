#акаунти
users = {
    "Daniel": {
        "password": "12hdr",
        "name": "Акимов Даниїл",
        "grades": [10, 4, 7, 12, 10, 8, 9],
    },
    "Sasha": {
        "password": "qw58ty",
        "name": "Бойчак Олександр",
        "grades": [11, 10, 3, 6, 5, 2, 10, 8],
    },
    "Maria": {
        "password": "589mm",
        "name": "Бунько Марія",
        "grades": [5, 11, 9, 7, 10, 12, 4],
    },
    "Stas": {
        "password": "trn2024",
        "name": "Мазелюк Станіслав",
        "grades": [9, 10, 11, 8, 5, 2, 6, 7, 10],
    },
    "Artem": {
        "password": "6at7ps",
        "name": "Пивовар Артем",
        "grades": [9, 10, 8, 10, 11, 7, 9, 7, 8],
    },
}

#ведення даних акаунта
login = input("Введіть логін: ")
password = input("Введіть пароль: ")

#перевірка
if login in users and users[login]["password"] == password:
    grades  = users[login]["grades"]

    print("\nВхід успішний!")
    print("Ваші оцінки:")
#оцінки
    for grade in grades:
        print(grade, end=" ")

    #підрахунок оцінок
    satisfactory = 0
    unsatisfactory = 0

    for grade in grades:
        if 5 <= grade <= 12:
            satisfactory += 1
        elif 1 <= grade <= 4:
            unsatisfactory += 1

    print("\n\nКількість задовільних оцінок:", satisfactory)
    print("Кількість незадовільних оцінок:", unsatisfactory)

else:
    print("\nПомилка! Неправильний логін або пароль.")