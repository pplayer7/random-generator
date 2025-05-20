#!/usr/bin/python3

# ИМПОРТ БИБЛИОТЕК

import random

# ФУНКЦИИ
def roll_the_dice() -> int: # КУБИКИ
    dices = range(1, 7) # цифры от 1 до 6
    return random.choice(dices) # возвращает одно из этих цифр

def coin_flip() -> str: # ПОДБРОС МОНЕТКИ
    return random.choices(["Орел", "Решка", "Ребро"], weights=[49.5, 49.5, 1], k=1)[0] # в списке указаны возможные варианты, во втором списке шансы

def generate_random_pass(lenght: int) -> str: # ГЕНЕРАЦИЯ СЛУЧАЙНОГО ПАРОЛЯ
    result = '' # конечный результат
    if lenght >= 1:
        for n in range(1, lenght + 1): # в диапазоне от 1 до длины
            result += random.choice('abcdefghijklomnpqrstuvwxyzABCDEFGHIJKLOMNPQRSTUVWXYZ0123456789!@#$%^&*()')
    else:
        return 'Ошибка. Длина не может быть меньше единицы.'
    return result

def yes_or_no() -> str: # ДА/НЕТ
    decisions = ['да', 'нет']
    return random.choice(decisions)

def magic_8ball() -> str: # МАГИЧЕСКИЙ ШАР
    magic_8ball_replicas = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определенно да', 'Можешь быть уверен в этом', 'Мне кажется — «да»', 'Вероятнее всего', 'Хорошие переспективы', 'Знаки говорят — «да»', 'Пока не ясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ — «нет»', 'По моим данным — «нет»', 'Переспективы не очень хорошие', 'Весьма сомнительно']
    return random.choice(magic_8ball_replicas)

def random_card() -> str: # СЛУЧАЙНАЯ КАРТА
    cards = ['крести', 'пиков', 'червей', 'бубнов']
    cards_value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король']
    return f'{random.choice(cards_value)} {random.choice(cards)}'

def roulette(list_of_vars) -> str:
    return random.choice(list(list_of_vars))

# КЛИЕНТСКАЯ ЧАСТЬ
decision = 'y'

while decision == 'y' or decision == '': # выбор пользователя (по умолчанию y, чтобы программа хотя бы запустилась)

    action = str(input("""Выберите действие:
1) Кинуть кости
2) Случайное число
3) Подброс монетки
4) Генератор паролей
5) Да или нет
6) Magic 8Ball
7) Случайная карта
8) Рулетка
9) Выйти

""")) # выбор

    if action == '1': # кинуть кости
        num_of_dices = input('\nСколько? (1, 2)\n\n') # кол-во костей
        if num_of_dices == '1' or num_of_dices == '':
            print(f"\nВыпавшее число: {roll_the_dice()}\n")
        elif num_of_dices == '2':
            first_dice = roll_the_dice()
            second_dice = roll_the_dice()
            print(f"""Выпавшее число: {first_dice + second_dice}
Первый кубик: {first_dice}
Второй кубик: {second_dice}
""")
        else:
            print("Ошибка")
            exit()

    elif action == '2': # случайное число
        first_num = int(input('Введите первое число:\n')) # число ОТ
        second_num = int(input('Введите второе число:\n')) # число ДО
        if first_num > second_num:
            print('\nЧисло "от" не может быть больше числа "до".')
            exit()
        print(f'\nВыпавшее число: {random.randint(first_num, second_num)}')

    elif action == '3': # подброс монетки
        print(f'\nВыпавшая сторона: {coin_flip()}')

    elif action == '4': # генератор паролей
        lenght_of_pass = int(input('\nВведите длину пароля:\n'))
        print(f'\n{generate_random_pass(lenght_of_pass)}')

    elif action == '5': # да или нет
        print(f'\nОтвет: {yes_or_no()}')

    elif action == '6': # магический шар
        input('Введите свой вопрос:\n')
        print(f'\n{magic_8ball()}')

    elif action == '7': # случайная карта
        print(f'\n{random_card()}')

    elif action == '8': # рулетка
        var_list = list(input('Введите варианты через пробел\n').split())
        if var_list == []:
            print('Введите корректные значения!')
            exit()
        print(roulette(var_list))

    elif action == '9':
        print('Пока!')
        exit()

    else:
        print('Ошибка.')
        exit()

    decision = str(input('\nЕще раз? (y, n)\n\n')) # решение пользователя

