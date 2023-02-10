import UI
import create_jeson as crJ


def start():
    while True:
        action = UI.menu()
        if action == 0:
            print("\033[33m {}\033[0m".format("До скорых встреч."))
        elif action == 1:
            crJ.read_notes()
        elif action == 3:
            name = UI.name_note()
            text = UI.text_note()
            crJ.new_note(name, text)
