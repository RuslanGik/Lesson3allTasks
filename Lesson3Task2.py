# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def print_data(**kwargs):
    return ' '.join(kwargs.values())


print(print_data(name=input('Введите ваше имя: '), surname=input('Введите вашу фамилию: '),
                 birth_year=input('Введите год вашего рождения: '),
                 city=input('Введите ваш город: '), email=input('Введите ваш email: '),
                 phone=input('Введите ваш телефон: ')))


# Вариант 2
def print_data(name, surname, birthday, city, email, phone):
    return f'Name - {name}, {surname}, {birthday}, {city}, {email}, {phone}'


