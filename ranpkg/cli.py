import random

def roll_the_dices(num_of_dices: int) -> int | list[int] | str: # КУБИКИ
    if num_of_dices in [0, 1]:
        return random.randint(1, 6)
    elif num_of_dices == 2:
        return [random.randint(1, 6), random.randint(1, 6)]
    else:
        return 'Некорректное число кубиков.'

def coin_flip() -> str: # ПОДБРОС МОНЕТКИ
    return random.choices(["Орел", "Решка", "Ребро"], weights=[49.5, 49.5, 1], k=1)[0] # в списке указаны возможные варианты, во втором списке шансы

def generate_random_pass(length: int) -> str: # ГЕНЕРАЦИЯ СЛУЧАЙНОГО ПАРОЛЯ
    result = '' # конечный результат
    if length >= 1:
        for n in range(1, length + 1): # в диапазоне от 1 до длины
            result += random.choice('abcdefghijklomnpqrstuvwxyzABCDEFGHIJKLOMNPQRSTUVWXYZ0123456789!@#$%^&*()')
    else:
        return 'Ошибка. Некорректная длина пароля.'
    return result

def yes_or_no() -> str: # ДА/НЕТ
    return random.choice(('да', 'нет'))

def magic_8ball() -> str: # МАГИЧЕСКИЙ ШАР
    return random.choice(('Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определенно да', 'Можешь быть уверен в этом', 'Мне кажется — «да»',
    'Вероятнее всего', 'Хорошие переспективы', 'Знаки говорят — «да»', 'Пока не ясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать',
    'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ — «нет»', 'По моим данным — «нет»', 'Переспективы не очень хорошие',
    'Весьма сомнительно'))

def random_card() -> str: # СЛУЧАЙНАЯ КАРТА
    cards_value = [*list(range(2, 10 + 1)), 'Валет', 'Дама', 'Король', 'Туз']
    cards = ['крести', 'пиков', 'червей', 'бубнов']
    return f'{random.choice(cards_value)} {random.choice(cards)}'

def roulette(list_of_vars: list) -> str:
    return random.choice(list(list_of_vars)) if list_of_vars != [] else 'Введите правильные значения!'

def russian_roulette() -> str:
    return 'Револьвер выстрелил...' if random.randint(1, 6) == 1 else 'Жив. Пока что...'


if __name__ == '__main__':
    ...