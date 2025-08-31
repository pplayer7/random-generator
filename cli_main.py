#!/usr/bin/python3

# ИМПОРТ БИБЛИОТЕК

import random
from ranpkg.cli import *

# main

def main() -> None:
    action = int(input('''Выберите действие:
1) Кинуть кости
2) Случайное число
3) Подброс монетки
4) Генератор паролей
5) Да или нет
6) Magic 8Ball
7) Случайная карта
8) Рулетка
9) Русская рулетка
10) Выйти

''')) # выбор
    match action:
        case 1: # кинуть кости
            num_of_dices = int(input('\nСколько? (1, 2)\n\n')) # кол-во костей
            if num_of_dices in [0, 1]:
                print(f'Выпавшее число: {roll_the_dices(num_of_dices)}')
            elif num_of_dices == 2:
                print((f'''Выпавшее число: {sum(result := roll_the_dices(num_of_dices))}
Первый кубик: {result[0]}
Второй кубик: {result[1]}

'''))
            else:
                print('Введите правильное число!')
        case 2: # случайное число
            first_num = int(input('Введите первое число:\n')) # число ОТ
            second_num = int(input('Введите второе число:\n')) # число ДО
            if first_num > second_num:
                print('\nЧисло "от" не может быть больше числа "до".')
            print(f'\nВыпавшее число: {random.randint(first_num, second_num)}')

        case 3: # подброс монетки
            print(f'\nВыпавшая сторона: {coin_flip()}')

        case 4: # генератор паролей
            lenght_of_pass = int(input('\nВведите длину пароля:\n'))
            print(f'\n{generate_random_pass(lenght_of_pass)}')

        case 5: # да или нет
            print(f'\nОтвет: {yes_or_no()}')

        case 6: # магический шар
            input('\nВведите свой вопрос:\n')
            print(f'\n{magic_8ball()}')

        case 7: # случайная карта
            print(f'\n{random_card()}')

        case 8: # рулетка
            var_list = input('\nВведите варианты через пробел\n').split()
            print(roulette(var_list))

        case 9:
            print(russian_roulette())

        case 10:
            print('Пока!')
            exit()

        case _:
            print('Ошибка.')
            exit()

    global decision
    decision = str(input('\nЕще раз? (y, n)\n\n')) # решение пользователя

decision: str = 'y'

if __name__ == '__main__':
    while decision == 'y' or decision == '': # выбор пользователя (по умолчанию y, чтобы программа хотя бы запустилась)
        main()
    else:
        exit()