import tkinter as tk
from tkinter import ttk, NW, X, scrolledtext

class Сhange_win(tk.Tk):

    """Изменение заметки"""

    def select(self):
        result = "Выбрано: "

        if self.date.get() == 1: result = f"{result} Ищем по дате"
        if self.name.get() == 1: result = f"{result} Ищем по названию"
        self.search.set(result)

    def __init__(self):
        super().__init__()

        self.title('Изменение заметки')
        self.geometry('400x250')

        self.position = {"padx":6, "pady":6, "anchor":NW}

        self.search = tk.StringVar()
        self.languages_label = ttk.Label(textvariable=self.search)
        self.languages_label.pack(**self.position)

        self.date = tk.IntVar()
        self.date_checkbutton = ttk.Checkbutton(text="Ищем по дате", variable=self.date, command=self.select)
        self.date_checkbutton.pack(**self.position)

        self.name = tk.IntVar()
        self.name_checkbutton = ttk.Checkbutton(text="Ищем по названию", variable=self.name, command=self.select)
        self.name_checkbutton.pack(**self.position)


if __name__ == "__main__":
  app = Сhange_win()
  app.mainloop()

