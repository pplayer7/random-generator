from ranpkg import gui
from tkinter import Tk, NW # нет надобности за *
from tkinter import ttk

root: Tk = Tk()

root.geometry('400x300+495+270')
root.title('Random Generator')


modes_list: list = ['Кинуть кости', 'Случайное число', 'Монетка',
                    'Генератор паролей', 'Да / нет', '8Ball',
                    'Случайная карта', 'Русская рулетка']

modes_combobox: ttk.Combobox = ttk.Combobox(values=modes_list, state='readonly')
modes_combobox.pack(anchor=NW, padx=6, pady=6)

def delete_elements(window=root) -> None:
    for element in window.winfo_children():
        element.destroy() if element != modes_combobox else ... # это шоб оставить список с режимами


def change_mode(event) -> None:
    selected_mode = modes_combobox.get()
    selected_dict = {'Кинуть кости': 'roll_the_dices_gui',
                    'Случайное число': 'random_number_gui',
                    'Монетка': 'coin_flip_gui',
                    'Генератор паролей': 'generate_random_pass_gui',
                    'Да / нет': 'yes_or_no_gui',
                    '8Ball': 'magic_8ball_gui',
                    'Случайная карта': 'random_card_gui',
                    # а рулетки слов пользователи гуи-версии лишаются, надо быть хардкорщиком в cli
                    'Русская рулетка': 'russian_roulette_gui'}
    delete_elements()
    eval(f'gui.{selected_dict.get(selected_mode)}(root)')


modes_combobox.bind("<<ComboboxSelected>>", change_mode)

def main() -> None:
    root.mainloop()

if __name__ == '__main__':
    main()

