import tkinter as tk
from tkinter import ttk, Text, scrolledtext, NW
from tkinter.messagebox import showinfo
import create_jeson as crJ
import sort as s
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

   def new_window(self):
      """переход в класс новой заметки"""
      Second_win().mainloop()

   def sort_window(self):
      """переход в класс новой sort"""
      s.Show_win().mainloop()
   def show(self):
      """переход в класс удаления заметок"""
      Show_win().mainloop()


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
class Second_win(tk.Tk):
   """класс новой заметки"""
   def get_text(self):
      global e1, e2
      print("....5...")
      name = e1.get()
      print(name, "name")
      input_text = e2.get()
      print("input_text ", input_text)
      bol = crJ.new_note(name, input_text)
      print("bol", bol)
      if bol == True:
         self.clear_text()
         self.label = ttk.Label(self, text=f"{name} {input_text}\nЗаметка успешно добавлена!!!!").grid(row=8)
         self.after(3000, self.destroy)

   def __init__(self):
      super().__init__()

      global e1, e2
      self.title('Новая заметка')
      self.geometry('300x250')

      self.label = ttk.Label(self, text="Введите имя заметки").grid(row=0)
      self.label = ttk.Label(self, text="Введите заметку").grid(row=1)

      e1 = ttk.Entry(self)
      e2 = ttk.Entry(self)

      e1.grid(row=0, column=1)
      e2.grid(row=1, column=1)

      cal_btn = ttk.Button(self, text='Добавить заметку', command=self.get_text)
      cal_btn.grid(row=5, column=0)

      cal_btn2 = ttk.Button(self, text='Назад', command=self.destroy)
      cal_btn2.grid(row=6, column=0)


   def clear_text(self):
      """очистка строк ввода после добавления данных"""
      e1.delete(0, 'end')
      e2.delete(0, 'end')

class Show_win(tk.Tk):
   """Функция вывода всех заметок"""

   def __init__(self):
      super().__init__()

      self.title('Список всех заметок')
      self.geometry('400x250')

      self.txt = scrolledtext.ScrolledText(self, width=40, height=10)
      self.txt.grid(column=0, row=0)

      t = crJ.show_notes()
      self.txt.insert(1.0, ''.join(t))

      cal_btn = ttk.Button(self, text='Назад', command=self.destroy)
      cal_btn.grid(row=6, column=0)

if __name__ == "__main__":
  app = App()
  app.mainloop()
