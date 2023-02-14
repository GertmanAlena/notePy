import json
import datetime as DT

def new_note(name, text):
    data_now = DT.datetime.now().strftime("%d.%m.%Y")
    r_notes = read_notes()
    print("r_notes ", r_notes)
    if len(r_notes) != 0:
        print("len(r_notes) ", len(r_notes))
        x = len(r_notes)
        id = x + 1
        print("id + 1 ", id)
    else:
        id = 0
    dict_notes = {}
    dict_notes["id"] = id
    dict_notes["header"] = name
    dict_notes["note"] = text
    dict_notes["date/time"] = data_now
    print("dict_notes ", dict_notes)
    r_notes.append(dict_notes)
    ok_record = record(r_notes)
    print("ok_record ", ok_record)

    return ok_record

def read_notes():
    try:
        with open('notes.json', 'r', encoding="utf-8") as file:
            r_notes = json.load(file)
            return r_notes
    except:
        r_notes = []
        if len(r_notes) == 0:
            print('\033[43m\033[1m {} \033[0m'.format(
                'ничего не найдено!'))
        return r_notes

def show_notes():
    """Функция вывода всех заметок"""
    print("...1.2...")
    all_note = []
    r_notes = read_notes()

    if len(r_notes) == 0:
        t = 'ничего не найдено!'
        print('\033[43m\033[1m {} \033[0m'.format(
            'ничего не найдено!'))
        return t
    else:
        y = ''
        for k in r_notes:
            x = str(k["id"]) + " " + str(k["header"]) + " " + str(k["note"]) + " " + str(k["date/time"]) + '\n'
            all_note.append(x)
        return all_note

def sort_notes():
    """Функция сортировки всех заметок"""
    all_note = []
    r_notes = read_notes()
    data_now = DT.datetime.now().strftime("%d.%m.%Y")
    if len(r_notes) == 0:
        t = 'ничего не найдено!'
        print('\033[43m\033[1m {} \033[0m'.format(
            'ничего не найдено!'))
        return t
    else:
        stocks = sorted(r_notes, key=lambda x: DT.datetime.strptime(x['date/time'], '%d.%m.%Y'), reverse=False)
        print("stocks", stocks)

        for k in stocks:
            x = str(k["id"]) + " " + str(k["header"]) + " " + str(k["note"]) + " " + str(k["date/time"]) + '\n'
            all_note.append(x)
        return all_note

        # return all_note

def record(r_notes):
    try:
        with open('notes.json', 'w', encoding="utf-8") as file:
            json.dump(r_notes, file, indent=2, ensure_ascii=False)
        print('\033[30m\033[42m\033[4m {}\033[0m'.format('записано!!'))

        print('-' * 50)
        return True

    except Exception as e:
        print('\033[30m\033[41m\033[4m {}\033[0m'.format('Заметка не добавлена!!'))
        return False

def delete_notes():
    r_notes = read_notes()
    if len(r_notes) == 0:
        print('\033[43m\033[1m {} \033[0m'.format(
            'ничего не найдено!'))
        return False
    else:
        r_notes.clear()
        record(r_notes)
        return True

def search_note(name):
    """Функция поиска заметки"""

    all_note = []
    r_notes = read_notes()

    if len(r_notes) == 0:
        t = 'ничего не найдено!'
        print('\033[43m\033[1m {} \033[0m'.format(
            'ничего не найдено!'))
        return t
    else:
        for k in r_notes:
            print(".....")
            if str(k["header"]) == name:
                print("k[header]", k["header"])
                x = str(k["id"]) + " " + str(k["header"]) + " " + str(k["note"]) + " " + str(k["date/time"]) + '\n'
                print("x ", x)
                all_note.append(x)
        print("all ", all_note)
        return all_note

def search_note_date(dat):
    """Функция поиска заметки"""

    all_note = []
    r_notes = read_notes()

    if len(r_notes) == 0:
        t = 'ничего не найдено!'
        print('\033[43m\033[1m {} \033[0m'.format(
            'ничего не найдено!'))
        return t
    else:
        for k in r_notes:
            if str(k["date/time"]) == dat:
                x = str(k["id"]) + " " + str(k["header"]) + " " + str(k["note"]) + " " + str(k["date/time"]) + '\n'
                all_note.append(x)
        return all_note
