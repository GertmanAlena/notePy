import tkinter as tk
from tkinter import ttk, NW
from tkinter.messagebox import showinfo
import create_jeson as crJ
import sort as s
import search as s2
import new_note as nn
import change_note as chN
class App(tk.Tk):
   """Основное окно с кнопками"""
   def __init__(self):
      super().__init__()

      # configure the root window
      self.title('Мои заметки')
      self.geometry('300x250')

      # label
      self.label = ttk.Label(self, text='Выбирай что будем делать!', foreground='red')
      self.label.pack()

      # button
      self.button = ttk.Button(self, text='Просмотр всех моих заметок')
      self.button['command'] = self.show
      self.button.pack(anchor=NW)

      self.button2 = ttk.Button(self, text='Удалить все заметки')
      self.button2['command'] = self.delete_notes
      self.button2.pack(anchor=NW)

      self.button3 = ttk.Button(self, text='Новая заметка')
      self.button3['command'] = self.new_window
      self.button3.pack(anchor=NW)

      self.button4 = ttk.Button(self, text='Сортировка заметок по дате')
      self.button4['command'] = self.sort_window
      self.button4.pack(anchor=NW)

      self.button5 = ttk.Button(self, text='Поиск заметки')
      self.button5['command'] = self.search_window
      self.button5.pack(anchor=NW)

      self.button5 = ttk.Button(self, text='Удалить/Измененить заметку')
      self.button5['command'] = self.change_window
      self.button5.pack(anchor=NW)


   def new_window(self):
      """переход в класс новой заметки"""
      nn.New_note_win().mainloop()
   def search_window(self):
      """поиск заметки заметки"""
      s2.Search_win().mainloop()

   def change_window(self):
      """изменение заметки"""
      chN.Сhange_win().mainloop()
   def sort_window(self):
      """переход в класс новой sort"""
      s.Show_win().mainloop()
   def show(self):
      """переход в класс удаления заметок"""
      res = crJ.show_notes()
      nn.Show_win("ссмотрим все заметки", res).mainloop()

   def delete_notes(self):
      """Функция удаления всех заметок"""

      t = crJ.delete_notes()
      if t == False:
         text = 'Ваш список щаметок ещё пуст. Удалять нечего'
         self.clicked(text)
      else:
         text = 'Удалено'
         self.clicked(text)

   def clicked(self, text):
      tk.messagebox.showinfo(',,,', text)




if __name__ == "__main__":
  app = App()
  app.mainloop()
