import tkinter as tk

from tkinter import ttk
from tkinter import *


class Radiobutton_change(tk.Tk):

    def add(self):

        print("-------------", self.selected_langs)
        # languages_listbox.insert(0, new_language)

    def selected(self, notes_listbox):
        # получаем индексы выделенных элементов
        selected_indices = self.notes_listbox.curselection()
        print("selected_indices ", selected_indices)
        # получаем сами выделенные элементы
        self.selected_langs = ",".join([self.notes_listbox.get(i) for i in selected_indices])
        msg = f"вы выбрали: {self.selected_langs}"
        self.label = ttk.Label(self, text=msg).grid(column=0, row=2)
        print(self.selected_langs)

        # self.button = ttk.Button(self, text='>>>')
        # self.button['command'] = self.add
        # self.button.grid(column=1, row=4)

    def __init__(self, res):
        super().__init__()

        self.title('............')
        self.geometry('300x250')
        self.config(bg='#446644')

        self.columnconfigure(index=0, weight=4)
        self.columnconfigure(index=1, weight=1)
        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=3)

        self.label = ttk.Label(self, text="Вот что нашлось").grid(row=1)

        # self.notes_entry = ttk.Entry(self)
        # self.notes_entry.grid(column=0, row=2, padx=6, pady=6, sticky=EW)

        ttk.Button(self, text=">>>", command=self.add).grid(column=2, row=2, padx=6, pady=6)

        self.notes_listbox = Listbox(self)
        self.notes_listbox.grid(row=3, column=0, columnspan=2, sticky=EW, padx=5, pady=5)


        x = 1
        for i in res:
            print(i)
            self.notes_listbox.insert(1, i)
            x += 1
        self.notes_listbox.bind("<<ListboxSelect>>", self.selected)

if __name__ == "__main__":
    app = Radiobutton_change()
    app.mainloop()
