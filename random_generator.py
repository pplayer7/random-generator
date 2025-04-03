#!/usr/bin/python3

# ИМПОРТ БИБЛИОТЕК
import random
import os

# ПЕРЕМЕННЫЕ
list_of_symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'o', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'O', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

decision = 'y'

yes_or_no = ['Да', 'Нет']

magic_8ball_replics = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определенно да', 'Можешь быть уверен в этом', 'Мне кажется - «да»', 'Вероятнее всего', 'Хорошие переспективы', 'Знаки говорят — «да»', 'Пока не ясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ — «нет»', 'По моим данным — «нет»', 'Переспективы не очень хорошие', 'Весьма сомнительно']

# ФУНКЦИИ
def roll_the_dice() -> int: # КУБИКИ
    dices = range(1, 7) # цифры от 1 до 6
    return random.choice(dices) # возвращает одно из этих цифр

def random_number(x: str, y: str) -> int: # СЛУЧАЙНОЕ ЧИСЛО
    x = int(x) # конвертируем строку в целое число
    y = int(y)
    if y < x:
        return 'Ошибка'
    return random.choice(range(x, y + 1)) # выбираем и возвращаем одно число из данного списка

def coin_flip() -> str: # ПОДБРОС МОНЕТКИ
    return random.choices(["Орел", "Решка", "Ребро"], weights=[49.5, 49.5, 1], k=1)[0] # в списке указаны возможные варианты, во втором списке шансы

def generate_random_pass(lenght: int) -> str: # ГЕНЕРАЦИЯ СЛУЧАЙНОГО ПАРОЛЯ
    i = 0 # счетчик
    result = '' # конечный результат
    while i <= lenght - 1: # пока счетчик меньше заданной длины пароля
        result += random.choice(list_of_symbols)
        i += 1
    return result

def yes_or_no(): # ДА/НЕТ
    decisions = ['Да', 'Нет']
    return random.choice(decisions)

def magic_8ball(): # МАГИЧЕСКИЙ ШАР
    magic_8ball_replics = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определенно да', 'Можешь быть уверен в этом', 'Мне кажется — «да»', 'Вероятнее всего', 'Хорошие переспективы', 'Знаки говорят — «да»', 'Пока не ясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ — «нет»', 'По моим данным — «нет»', 'Переспективы не очень хорошие', 'Весьма сомнительно']
    return random.choice(magic_8ball_replics)

def random_card(): # СЛУЧАЙНАЯ КАРТА
    cards = ['крести', 'пиков', 'червей', 'бубнов']
    cards_value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король']
    return f'{random.choice(cards_value)} {random.choice(cards)}'

# КЛИЕНТСКАЯ ЧАСТЬ
while decision == 'y' or decision == '': # выбор пользователя (по умолчанию y, чтобы программа хотя бы запустилась)

    action = str(input('\nВыберите действие:\n1) Кинуть кости\n2) Случайное число\n3) Подброс монет\n4) Генератор паролей\n5) Да или нет\n6) Magic 8Ball\n7) Случайная карта\n8) Выйти\n\n')) # выбор

    if action == '1': # кинуть кости
        num_of_dices = input('\nСколько? (1, 2)\n\n') # кол-во костей
        if num_of_dices == '1' or num_of_dices == '':
            print(f"\nВыпавшее число: {roll_the_dice()}\n")
        elif num_of_dices == '2':
            first_dice = roll_the_dice()
            second_dice = roll_the_dice()
            print(f'\nВыпавшее число: {first_dice + second_dice}\nПервый кубик: {first_dice}\nВторой кубик: {second_dice}')


    elif action == '2': # случайное число
        first_num = input('Введите первое число:\n') # число ОТ
        second_num = input('Введите второе число:\n') # число ДО
        if first_num > second_num:
            print('\nЧисло "от" не может быть больше числа "до".')
            exit()
        print(f'\nВыпавшее число: {random_number(first_num, second_num)}')

    elif action == '3': # подброс монетки
        print(f'\nВыпавшая сторона: {coin_flip()}')

    elif action == '4': # генератор паролей
        lenght_of_pass = int(input('\nВведите длину пароля:\n'))
        print(f'\nПароль: {generate_random_pass(lenght_of_pass)}')

    elif action == '5': # да или нет
        print(f'\nОтвет: {yes_or_no()}')

    elif action == '6': # магический шар
        str(input('Введите свой вопрос:\n'))
        print(f'\nОтвет: {random.choice(magic_8ball_replics)}')

    elif action == '7':
        print(f'\n{random_card()}')

    elif action == '8':
        print('Пока!')
        exit()

    elif action == 'PLAYERLOX':
        os.system('curl http://ascii.live/rick')

    else:
        print('Ошибка.')
        exit()

    decision = str(input('\nЕще раз? (y, n)\n\n')) # решение пользователя

    if decision != 'y' and decision != 'n' and decision != '' and action != 'PLAYERLOX': # если решение не y, не n и не пустая строка, то завершаем программу
        print('Пока!')
        exit()
