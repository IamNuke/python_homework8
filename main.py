# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать контакты
# 4. Добавить контакт
# 5. Изменить контакт
# 6. Найти контакт
# 7. Удалить контакт
# 8. Выход

import action_handlers

path = "phone_book.txt"
while True:
    user_choise = action_handlers.show_menu()
    match user_choise:
        case 1:
            action_handlers.is_open = action_handlers.open_directory(path)
        case 2:
            action_handlers.save_directory(path)
        case 3:
            action_handlers.show_directory()
        case 4:
            action_handlers.add_directory()
        case 5:
            action_handlers.change_directory()
        case 6:
            action_handlers.find_directory()
        case 7:
            action_handlers.delete_directory()
        case 8:
            if action_handlers.close_directory():
                break
        case _:
            print("Ошибка ввода")
