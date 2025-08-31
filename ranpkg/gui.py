import random
import pyperclip
from .cli import *
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

# ! даже не пытайтесь сократить код с помощью функции, которая возвращает кнопку
# ! по шаблону ttk.Button(text=text, command=lambda: showinfo(title=title, message=message))
# ! т. к. это возвращает один и тот же результат каждый раз (я проверял)
# ! пусть будет длинный код, я хз как еще сократить


center_position: dict = {'anchor': CENTER, 'relx': 0.5, 'rely': 0.5}

def roll_the_dices_gui(window) -> None:
    dices_num: IntVar = IntVar()
    button_1: ttk.Radiobutton = ttk.Radiobutton(text=1, value=1, variable=dices_num)
    button_2: ttk.Radiobutton = ttk.Radiobutton(text=2, value=2, variable=dices_num)
    def show_result(num_of_dices: int) -> None:
        match num_of_dices:
            case 1:
                showinfo(title='Кубики', message=f'Выпавшее число: {roll_the_dices(1)}')
            case 2:
                showinfo(title='Кубики', message=f'''Выпавшее число: {int(sum(result := roll_the_dices(2)))}
Первый кубик: {result[0]}
Второй кубик: {result[1]}''')

    gen_button: ttk.Button = ttk.Button(text='Сгенерировать!', command=lambda: show_result(dices_num.get()))

    button_1.pack()
    button_2.pack()
    gen_button.pack()


def random_number_gui(window) -> None:
    num_from: ttk.Entry = ttk.Entry(validate='key', validatecommand=(window.register(lambda num: num.isdigit() or num == '-' or int(num) < 0), '%P'))
    num_to: ttk.Entry = ttk.Entry(validate='key', validatecommand=(window.register(lambda num: num.isdigit() or num == '-' or int(num) < 0), '%P'))

    gen_button: ttk.Button = ttk.Button(text='Сгенерировать!', command=lambda: showinfo(title='Число',
                                                                                        message=random.randint(int(num_from.get()), int(num_to.get()))))
    first_num: ttk.Label = ttk.Label(text='Число ОТ')
    second_num: ttk.Label = ttk.Label(text='Число ДО')

    num_from.place(anchor=CENTER, relx=0.3, rely=0.4)
    num_to.place(anchor=CENTER, relx=0.7, rely=0.4)
    first_num.place(anchor=CENTER, relx=0.3, rely=0.3)
    second_num.place(anchor=CENTER, relx=0.7, rely=0.3)
    gen_button.place(anchor=CENTER, relx=0.5, rely=0.5)


def coin_flip_gui(window) -> None:
    flip_button: ttk.Button = ttk.Button(text='Подкинуть', command=lambda: showinfo(title='Монетка', message=coin_flip()))
    flip_button.place(**center_position)

def generate_random_pass_gui(window) -> None:
    len_of_pass: ttk.Entry = ttk.Entry(validate='key', validatecommand=(window.register(lambda num: num.isdigit() and num > 0), '%P'))
    info_label: ttk.Label = ttk.Label(text='Длина пароля')

    def gen_pass(len_of_pass: int) -> None:
        if len_of_pass > 0:
            pyperclip.copy(generate_random_pass(len_of_pass))
            showinfo(title='Пароль', message='Пароль скопирован в буфер обмена') # найдите другой генератор паролей, я метода лучше не нашел
        else:
            showinfo(title='Пароль', message='Некорректная длина пароля!')

    generate_button: ttk.Button = ttk.Button(text='Сгенерировать!', command=lambda: gen_pass(int(len_of_pass.get())))
    len_of_pass.place(**center_position)
    info_label.place(anchor=CENTER, relx=0.5, rely=0.4)
    generate_button.place(anchor=SE, relx=1.0, rely=1.0)

def yes_or_no_gui(window) -> None:
    yes_no_button: ttk.Button = ttk.Button(text='Да / Нет', command=lambda: showinfo(title='Ответ', message=yes_or_no().capitalize()))
    yes_no_button.place(anchor=SE, relx=0.6, rely=0.6)


def magic_8ball_gui(window) -> None:
    question: ttk.Entry = ttk.Entry()
    question.place(**center_position)

    info_label: ttk.Label = ttk.Label(text="Введите свой вопрос:")
    info_label.place(anchor=CENTER, relx=0.5, rely=0.4)

    result_button: ttk.Button = ttk.Button(text='Ответить!', command=lambda: showinfo(title='Ответ', message=magic_8ball()))
    result_button.place(anchor=SE, relx=1.0, rely=1.0)

def random_card_gui(window) -> None:
    card_button: ttk.Button = ttk.Button(text='Выбрать', command=lambda: showinfo(title='Карта', message=random_card()))
    card_button.place(**center_position)

def russian_roulette_gui(window) -> None:
    rr_button: ttk.Button = ttk.Button(text='Выстрелить (или нет)...', command=lambda: showinfo(title='...', message=russian_roulette()))
    rr_button.place(**center_position)