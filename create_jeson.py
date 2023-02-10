import json
import datetime as DT

notes = {}


def new_note(name, text):
    data_now = DT.datetime.now().strftime("%d.%m.%Y")

    r_n = read_notes()
    print("r_n ", r_n)
    if r_n is None:
        id = 1
        notes = dict({'идентификатор': id, 'заголовок': name, 'заметка': text, 'дату/время': data_now})
        print('\033[30m\033[42m\033[4m {}\033[0m'.format('Заметка добавлена'))

    else:
        for i in r_n:
            if i == str(data_now):
                print("i ", i)
                print(notes[i])

                notes.update({name: text})
                # i = {name: text}
            else:
                notes = dict({'id': id, 'header': name, 'note': text, 'date/time': data_now})

    try:
        with open('notes.json', 'a', encoding="utf-8") as file:
            json.dump(notes, file, indent=2, ensure_ascii=False)
        print('\033[30m\033[42m\033[4m {}\033[0m'.format('Заметка добавлена'))
        print('-' * 50)

    except Exception as e:
        print("ошибка " + e)

def read_notes():
    """Функция вывода всех заметок"""
    try:

        with open('notes.json', 'r') as file:
            notes = json.load(file)
            if len(notes) == 0:
                print('\033[43m\033[1m {} \033[0m'.format(
                    'Ваш список заметок пуст!'))
            else:
                for i in notes:
                    print(i)
                    # print(f'\033[44m {i}\033[0m\n')

            return notes
    except Exception as e:
        print("ошибка ", e)
        return None

