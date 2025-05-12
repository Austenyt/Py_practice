"""
Управление списком задач (To-Do List)

2. Описание:
Программа представляет собой систему управления списком задач. Пользователь может добавлять, редактировать, удалять и
просматривать задачи.
Программа должна быть текстовой, без использования графического интерфейса.

3. Функциональные требования:
Программа должна иметь следующие функции:
Добавление новой задачи.
Редактирование существующей задачи.
Удаление задачи.
Просмотр всех задач.
Все действия должны быть выполнены через текстовый интерфейс.

4. Нефункциональные требования:
Программа должна работать в терминале или консоли.
Пользовательский интерфейс должен быть простым и понятным.
Взаимодействие с пользователем должно происходить через стандартный ввод и вывод (input, print).
Программа не должна использовать сторонние библиотеки.

5. Данные, с которыми работает программа:
Список задач — хранится в виде списка строк в памяти.
Каждая задача — это строка текста.
Индексы задач — начинаются с 0, но в интерфейсе задачи отображаются с 1.

6. Требования к интерфейсу:
При запуске программы пользователь должен увидеть меню с выбором действий.
Программа должна корректно обрабатывать ошибки (например, неправильный ввод индекса задачи или пустой список задач).
"""
import os
from colorama import just_fix_windows_console, init, Fore, Back, Style

def create():
    task = input("Введите задачу\n")
    with open('file.txt', 'a', encoding='utf-8') as f:
        data = task + '\n'
        f.write(data)


def read_file():
    try:
        with open('file.txt', 'r', encoding='utf-8') as f:
            b = f.readlines()
    except FileNotFoundError:
        with open('file.txt', 'w', encoding='utf-8') as f:
            b = []
    return b


def digit_input(a):
    while True:
        index = input()
        if index.isdigit():
            if 0 < int(index) <= a:
                return int(index)
        print("\033[31mВведенный символ вне диапазона или не является числом\033[0m")


def view():
    c = read_file()
    for index, task in enumerate(c, 1):
        print(f'[{index}] {task}', end='')
    return c


def update():
    c = view()
    if c:
        print("Введите индекс задачи для редактирования:\n")
        index = digit_input(len(c))
        new_task = input("Введите новый текст задачи\n")
        c[index - 1] = new_task + '\n'
        with open('file.txt', 'w', encoding='utf-8') as f:
            f.writelines(c)
        print("Обновленный список задач:")
        view()
        input()


def delete():
    print("Выберите индекс задачи для удаления:")
    c = view()
    if c:
        index = digit_input(len(c))
        del c[index - 1]
        with open('file.txt', 'w', encoding='utf-8') as f:
            f.writelines(c)
        print("Обновленный список задач:")
        view()
        input()


def main():
    init()
    just_fix_windows_console()
    while True:
        os.system('cls')
        print("_            _             \n"
              "| |_  _ ___| | _____ _ __\n"
              "| / _` / | |/ / _ \ '|\n"
              "| || (_| \__ \   <  / |   \n"
              " \__\,_|___/_|\_\___|_|\n")
        print(Back.GREEN + "Данная программа предназначена для работы с задачами. Выберите действие:" + Style.RESET_ALL)
        a = input("1. Создать задачу\n"
                  "2. Просмотреть задачу\n"
                  "3. Редактировать задачу\n"
                  "4. Удалить задачу\n")
        os.system('cls')
        if a == '1':
            create()
        elif a == '2':
            view()
            input()
        elif a == '3':
            update()
        elif a == '4':
            delete()
        else:
            print(Fore.RED + "Неправильный ввод" + Style.RESET_ALL)
            input()
            continue


if __name__ == "__main__":
    main()
# Для трансформации в 1 файл pyinstaller --onefile TZ.py
print(globals())
