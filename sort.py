
import tkinter as tk
from tkinter import ttk, Text, scrolledtext, NW
from tkinter.messagebox import showinfo
import create_jeson as crJ


class Show_win(tk.Tk):
   """Функция сортировки по дате"""

   def __init__(self):
      super().__init__()

      self.title('сортировка')
      self.geometry('400x250')

      self.txt = scrolledtext.ScrolledText(self, width=40, height=10)
      self.txt.grid(column=0, row=0)

      t = crJ.sort_notes()
      self.txt.insert(1.0, ''.join(t))

      cal_btn = ttk.Button(self, text='Назад', command=self.destroy)
      cal_btn.grid(row=6, column=0)

if __name__ == "__main__":
  app = Show_win()
  app.mainloop()