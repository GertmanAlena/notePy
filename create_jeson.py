import json
import datetime as DT


def new_note(name, text):
    data_now = DT.datetime.now().strftime("%d.%m.%Y")
    r_notes = read_notes()

    if r_notes != None:
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

    return dict_notes
    # for i in r_notes:
    #     if i["id"] == id:
    #         id+=1
    #         print(f'id: {i["id"]} header: {i["header"]} note: {i["note"]} date/time: {i["date/time"]}')
    #     else:

def read_notes():
    try:
        with open('notes.json', 'r', encoding="utf-8") as file:
            r_notes = json.load(file)
            return r_notes
    except:
        r_notes = {}
        if len(r_notes) == 0:
            print('\033[43m\033[1m {} \033[0m'.format(
                'ничего не найдено!'))
        return r_notes


def show_notes():
    """Функция вывода всех заметок"""
    all_note = []
    r_notes = read_notes()
    if len(r_notes) == 0:
        text = 'ничего не найдено!'
        print('\033[43m\033[1m {} \033[0m'.format(
            'ничего не найдено!'))
    else:
        for i in r_notes:
            all_note.append(i)
            # print(f'id: {i["id"]} header: {i["header"]} note: {i["note"]} date/time: {i["date/time"]}')
    lbl.configure(text=all_note)

def record(r_notes, dict_notes):

    r_notes.append(dict_notes)

    with open('notes.json', 'w', encoding="utf-8") as file:
        json.dump(r_notes, file, indent=2, ensure_ascii=False)
    print('\033[30m\033[42m\033[4m {}\033[0m'.format('Заметка добавлена!!'))

    print('-' * 50)
