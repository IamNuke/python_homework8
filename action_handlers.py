phone_book = dict()
is_open = False


def show_menu():
    menu = {
        1: 'Открыть файл',
        2: 'Сохранить файл',
        3: 'Показать контакты',
        4: 'Добавить контакт',
        5: 'Изменить контакт',
        6: 'Найти контакт',
        7: 'Удалить контакт',
        8: 'Выход'}

    for item in menu.keys():
        print(f'{item} \t {menu[item]}')
    user_input = input("Введите номер действия: ")
    if user_input.isdigit():
        return int(user_input)
    else:
        return 0


def open_directory(path):
    with open(path, 'r', encoding='utf-8') as data:
        phone_book.clear()
        for current_row in data:
            tmp = current_row.replace('\n', '').split(";")
            phone_book[tmp[1]] = (tuple(tmp[0].split()), tmp[2])
    print("Справочник открыт.")
    return True


def save_directory(path):
    with open(path, 'w', encoding='utf-8') as data:
        for key, value in phone_book.items():
            current_record = ";".join((' '.join(value[0]), key, value[1])) + '\n'
            data.write(current_record)
    print("Файл записан")


def show_directory():
    if not is_open:
        print("Справочник не открыт.")
        return
    for key in phone_book.keys():
        value = phone_book[key]
        print('%30s %30s %30s %30s ' % (value[0][0], value[0][1], value[1], key))


def add_directory():
    if not is_open:
        print("Справочник не открыт.")
        return

    name = tuple(input("Введите имя и фамилию: ").title().split())
    comment = input("Введите комментарий: ")
    value = (name, comment)
    if value in phone_book.values():
        print("Такая запись уже существует!")
    else:
        key = input('Введи номер телефона: ')
        phone_book[key] = value
        print("Запись добавлена.")


def change_directory():
    if not is_open:
        print("Справочник не открыт.")
        return
    key = input("Введите номер телефона: ")
    if key in phone_book:
        name = tuple(input("Введите имя и фамилию: ").title().split())
        comment = input("Введите комментарий: ")
        value = (name, comment)
        if value in phone_book.values():
            print("Такая запись уже существует!")
        else:
            phone_book[key] = value
            print("Запись изменена.")
    else:
        print("Такого номера нет.")


def find_directory():
    if not is_open:
        print("Справочник не открыт.")
        return

    menu = {
        1: 'По имени',
        2: 'По номеру',
        3: 'Отмена'}

    for item in menu.keys():
        print(f'{item} \t {menu[item]}')
    find_user_choise = int(input("Введите номер действия: "))
    match find_user_choise:
        case 1:
            name = tuple(input("Введите имя и фамилию: ").split())
            for key, value in phone_book.items():
                if name == value[0]:
                    print('%30s %30s %30s %30s ' % (value[0][0], value[0][1], value[1], key))
        case 2:
            key = input("Введите номер телефона: ")
            value = phone_book[key]
            print('%30s %30s %30s %30s ' % (value[0][0], value[0][1], value[1], key))
        case 3:
            return


def delete_directory():
    if not is_open:
        print("Справочник не открыт.")
        return

    menu = {
        1: 'По имени',
        2: 'По номеру',
        3: 'Отмена'}

    for item in menu.keys():
        print(f'{item} \t {menu[item]}')
    find_user_choise = int(input("Введите номер действия: "))
    match find_user_choise:
        case 1:
            name = tuple(input("Введите имя и фамилию: ").split())
            for key, value in phone_book.items():
                if name == value[0]:
                    phone_book.pop(key)
        case 2:
            key = input("Введите номер телефона: ")
            if key in phone_book:
                phone_book.pop(key)
        case 3:
            return
    print("Записи удалены")


def close_directory():
    if not is_open:
        print("Справочник не открыт.")
        return

    menu = {
        1: 'Закрыть',
        2: 'Отмена'}

    for item in menu.keys():
        print(f'{item} \t {menu[item]}')
    find_user_choise = int(input("Все не сохраненные изменения будут потеряны. Закрыть?: "))
    match find_user_choise:
        case 1:
            return True
        case 2:
            return False
