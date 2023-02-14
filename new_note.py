import tkinter as tk
from tkinter import ttk, scrolledtext
import create_jeson as crJ

class New_note_win(tk.Tk):

    """класс новой заметки"""

    def get_text(self):

        name = self.e1.get()
        input_text = self.e2.get()
        bol = crJ.new_note(name, input_text)
        if bol == True:
            self.clear_text()
            self.label = ttk.Label(self, text=f"{name} {input_text}\nЗаметка успешно добавлена!!!!").grid(row=8)
            self.after(3000, self.destroy)

    def __init__(self):
        super().__init__()

        self.title('Новая заметка')
        self.geometry('300x250')

        self.label = ttk.Label(self, text="Введите имя заметки").grid(row=0)
        self.label = ttk.Label(self, text="Введите заметку").grid(row=1)

        self.e1 = ttk.Entry(self)
        self.e2 = ttk.Entry(self)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)

        self.cal_btn = ttk.Button(self, text='Добавить заметку', command=self.get_text)
        self.cal_btn.grid(row=5, column=0)

        self.cal_btn2 = ttk.Button(self, text='Назад', command=self.destroy)
        self.cal_btn2.grid(row=6, column=0)

    def clear_text(self):
        """очистка строк ввода после добавления данных"""
        self.e1.delete(0, 'end')
        self.e2.delete(0, 'end')

if __name__ == "__main__":
  app = New_note_win()
  app.mainloop()

class Show_win(tk.Tk):
   """Функция вывода всех заметок"""

   def __init__(self, text, res):
      super().__init__()

      self.title(text)
      self.geometry('400x250')

      self.txt = scrolledtext.ScrolledText(self, width=40, height=10)
      self.txt.grid(column=0, row=0)


      self.txt.insert(1.0, ''.join(res))

      cal_btn = ttk.Button(self, text='Назад', command=self.destroy)
      cal_btn.grid(row=6, column=0)

if __name__ == "__main__":
  app = Show_win()
  app.mainloop()
