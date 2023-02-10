from test import number_action


def menu():
    while True:
        print('\n Меню')
        print("- 1 - Просмотр всех заметок")
        print("- 2 - Поиск заметки")
        print("- 3 - Добавление заметки")
        print("- 4 - Удаление заметки")
        print("- 5 - Удаление всех заметок")
        print("- 6 - Изменение заметки")
        print("- 7 - Экспорт данных")
        print("- 8 - Импорт данных")
        print("- 0 - Завершение работы")

        var = number_action()
        return var

def name_note():
    name = input("Please enter a name.")
    # test //TODO: проверка на ввод имени
    return name


def text_note():
    text = input("Please enter a text.")
    # test //TODO: проверка на ввод имени

    return text