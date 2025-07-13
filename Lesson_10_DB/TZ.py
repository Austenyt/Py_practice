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
import psycopg2
from colorama import just_fix_windows_console, init, Fore, Back, Style
from dotenv import load_dotenv

load_dotenv()


class DB:

    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=os.getenv('DBNAME'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            host=os.getenv('HOST'),
            port=os.getenv('PORT')
        )

    def __del__(self):
        self.conn.close()

    def execute(self, query, commit=False):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(query)
                if commit:
                    self.conn.commit()
                else:
                    return cursor.fetchall()
            except psycopg2.OperationalError as e:
                print(f'Unable to connect!\n {e}')
                exit()


db = DB()


def create():
    name = input("Введите задачу\n")
    description = input("Введите описание\n")
    date_due = input("Введите дату\n")
    is_done = input("Введите статус\n")
    db.execute(f"INSERT INTO task (name, description, date_due, is_done) "
               f"VALUES ('{name}','{description}', '{date_due}','{is_done}')", commit=True)


def read_task():
    try:
        b = db.execute("SELECT id, name FROM task ORDER BY id")
        return b
    except psycopg2.OperationalError as e:
        print(f'Unable to connect!\n {e}')
        exit()


def digit_input(a):
    while True:
        index = input()
        if index.isdigit():
            return int(index)
        print("\033[31mВведенный символ вне диапазона или не является числом\033[0m")


def view():
    c = read_task()
    for index, task in c:
        print(f'[{index}] {task}')
    return c


def update():
    c = view()
    if c:
        print("Введите индекс задачи для редактирования:\n")
        index = digit_input(len(c))
        new_task = input("Введите новый текст задачи\n")
        db.execute(
            f"UPDATE task SET name = '{new_task}' WHERE id = {index}", commit=True
        )
        print("Обновленный список задач:")
        view()


def delete():
    print("Выберите индекс задачи для удаления:")
    c = view()
    if c:
        index = digit_input(len(c))
        try:
            db.execute(
                f"DELETE FROM task WHERE id = {index}", commit=True
            )
            print("Обновленный список задач:")
            view()
        except:
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
