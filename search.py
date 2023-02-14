import tkinter as tk
from tkinter import ttk, NW, X, scrolledtext
import create_jeson as crJ
import new_note as nn
class Search_win(tk.Tk):

    """Функция поиска"""

    def get_text(self):

        name = self.e.get()
        self.clear_text()
        res = crJ.search_note(name)
        text = 'результаты поиска по названию заметки'
        nn.Show_win(text, res).mainloop()
    def get_text2(self):

        dat = self.e.get()
        self.clear_text()
        res = crJ.search_note_date(dat)
        text = 'результаты поиска по дате создания заметки'
        nn.Show_win(text, res).mainloop()
    def selected(self, combobox):

        print("selected")
        selection = self.combobox.get()
        print(selection)

        self.label = tk.Label(self, text=f'будем искать {selection}', foreground='blue')
        self.label.pack()

        if selection == "по названию":
            self.label = tk.Label(self, text='введите название')
            self.label.pack(anchor=NW, padx=6, pady=6)
            self.e = ttk.Entry(self)
            self.e.pack(anchor=NW, padx=6, pady=6)
            self.e.focus()
            self.cal_btn = ttk.Button(self, text='найти', command=self.get_text)
            self.cal_btn.pack(anchor=NW)

        if selection == "по дате":
            self.label = tk.Label(self, text='введите дату в формате дд.мм.год(00.00.0000)')
            self.label.pack(anchor=NW, padx=6, pady=6)
            self.e = ttk.Entry(self)
            self.e.pack(anchor=NW, padx=6, pady=6)
            self.e.focus()
            self.cal_btn = ttk.Button(self, text='найти', command=self.get_text2)
            self.cal_btn.pack(anchor=NW)
    def clear_text(self):
        """очистка строк ввода после добавления данных"""
        self.e.delete(0, 'end')

    def __init__(self):
        super().__init__()

        self.title('Поиск заметки')
        self.geometry('400x250')

        self.label = tk.Label(self, text='Как будем искать заметку??!', foreground='blue')
        self.label.pack()

        search_note = ["по названию", "по дате"]
        search_var = tk.StringVar()

        self.label = tk.Label(self, textvariable=search_var)
        self.label.pack(anchor=NW, padx=6, pady=6)

        self.combobox = ttk.Combobox(self, textvariable=search_var, values=search_note, state="readonly")
        self.combobox.pack(anchor=NW, fill=X, padx=6, pady=6)

        self.combobox.bind("<<ComboboxSelected>>", self.selected)

        self.cal_btn = tk.Button(self, text='Назад', command=self.destroy)
        self.cal_btn.pack(anchor=NW)


if __name__ == "__main__":
  app = Search_win()
  app.mainloop()

