import UI
import create_jeson as crJ


def start():
    while True:
        action = UI.menu()
        if action == 0:
            print("\033[33m {}\033[0m".format("До скорых встреч."))
        elif action == 1:
            r_notes = crJ.read_notes()
            crJ.show_notes(r_notes)
        elif action == 2:
            r_notes = crJ.read_notes()

        elif action == 3:
            name = UI.name_note()
            text = UI.text_note()
            r_notes = crJ.read_notes()
            dict_notes = crJ.new_note(name, text, r_notes)

            crJ.record(r_notes, dict_notes)

