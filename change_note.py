import tkinter as tk
from tkinter import ttk, NW, X, scrolledtext, SOLID
import create_jeson as crJ
import radiobutton_win as rw

class Сhange_win(tk.Tk):
    """Изменение заметки"""

    def get_text(self):

        args_name = self.e.get()
        self.clear_text()
        res = crJ.search_note(args_name)
        rw.Radiobutton_change(res).mainloop()

    def get_text2(self):

        args_date = self.e.get()
        self.clear_text()
        res = crJ.search_note_date(args_date)
        rw.Radiobutton_change(res).mainloop()

    def clear_text(self):
        """очистка строк ввода после добавления данных"""
        self.e.delete(0, 'end')
    def select(self):
        result = "Выбрано: "
        print(result)
        if self.date.get() == 1:

            result = f"{result} Ищем по дате"
            self.search.set(result)

            frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
            input_date = ttk.Label(frame, text="введите дату в формате дд.мм.год(00.00.0000)")
            input_date.pack(anchor=NW)
            self.e = ttk.Entry(frame)
            self.e.pack(anchor=NW)
            frame.pack(anchor=NW, fill=X, padx=5, pady=5)
            self.cal_btn = ttk.Button(self, text='найти', command=self.get_text2)
            self.cal_btn.pack(anchor=NW)

        if self.name.get() == 1:
            result = f"{result} Ищем по названию"
            self.search.set(result)

            frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
            input_date = ttk.Label(frame, text="введите название заметки")
            input_date.pack(anchor=NW)
            self.e = ttk.Entry(frame)
            self.e.pack(anchor=NW)
            frame.pack(anchor=NW, fill=X, padx=5, pady=5)
            self.cal_btn = ttk.Button(self, text='найти', command=self.get_text)
            self.cal_btn.pack(anchor=NW)
    def __init__(self):
        super().__init__()

        self.title('Снова ищем')
        self.geometry('400x250')

        self.position = {"padx": 6, "pady": 6, "anchor": NW}

        self.search = tk.StringVar(self)
        self.search_label = tk.Label(self, textvariable=self.search)
        self.search_label.pack(**self.position)

        self.date = tk.IntVar(self)
        self.date_checkbutton = tk.Checkbutton(self, text="Ищем по дате", variable=self.date, command=self.select)
        self.date_checkbutton.pack(**self.position)

        self.name = tk.IntVar(self)
        self.name_checkbutton = tk.Checkbutton(self, text="Ищем по названию", variable=self.name, command=self.select)
        self.name_checkbutton.pack(**self.position)

if __name__ == "__main__":
    app = Сhange_win()
    app.mainloop()
