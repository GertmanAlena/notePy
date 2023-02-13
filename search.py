
import tkinter as tk
from tkinter import ttk, Text, scrolledtext, NW, X
from tkinter.messagebox import showinfo
import create_jeson as crJ


class Search_win(tk.Tk):

  """Функция сортировки по дате"""

  global combobox
  global label

  def __init__(self):
      super().__init__()

      self.title('Поиск заметки')
      self.geometry('400x250')

      self.label = ttk.Label(self, text='Как будем искать??!', foreground='blue')
      self.label.pack()

      search_note = ["по названию", "по дате"]
      search_var = tk.StringVar(value=search_note[0])

      self.label = ttk.Label(self, textvariable=search_var)
      self.label.pack(anchor=NW, padx=6, pady=6)

      self.combobox = ttk.Combobox(self, textvariable=search_var, values=search_note, state="readonly")
      self.combobox.pack(anchor=NW, fill=X, padx=6, pady=6)

      self.combobox.bind("<<ComboboxSelected>>", self.selected)

      self.cal_btn = ttk.Button(self, text='Назад', command=self.destroy)
      self.cal_btn.pack(anchor=NW)

  def selected(event):
      global combobox
      global label
      # получаем выделенный элемент
      selection = combobox.get()
      print(selection)
      label["text"] = f"вы выбрали: {selection}"


if __name__ == "__main__":
  app = Search_win()
  app.mainloop()