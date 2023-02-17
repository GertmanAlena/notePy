import tkinter as tk
import create_jeson as crJ
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo

class Selected_n(tk.Tk):

    def get_text(self):

        name = self.e1.get()
        input_text = self.e2.get()
        bol = crJ.new_note(name, input_text)
        if bol == True:
            # self.clear_text()
            self.label = ttk.Label(self, text=f"{name} {input_text}\nЗаметка успешно добавлена!!!!").grid(row=8)
            self.after(3000, self.destroy)
    def __init__(self, res):
        super().__init__()
        self.geometry('420x150')
        self.title('окно изменения заметки')

        x = crJ.note_sel(res)
        print(x, "****x****")

        header = x[0]
        note = x[1]

        l = ttk.Label(self, text="Внесите изменения в заметку")
        l.grid()
        l1 = ttk.Label(self, text="Название заметки")
        l1.grid(row=2, column=0)
        self.e1 = ttk.Entry(self, width=50)
        self.e1.grid(row=2, column=1)
        self.e1.insert(0, header)

        l2 = ttk.Label(self, text="Текст заметки")
        l2.grid(row=3)
        self.e2 = ttk.Entry(self, width=50)
        self.e2.grid(row=3, column=1)
        self.e2.insert(0, note)
        ttk.Button(self, text="Изменить", command=self.get_text).grid(row=4, column=0)
        self.quit()
        # showinfo(title="Информация", message="Заметка изменена!! ")
        # self.after(200, self.destroy)



if __name__ == "__main__":
    app = Selected_n()
    app.mainloop()

class Radiobutton_change(tk.Tk):
    def change(self):
        Selected_n(self.selected_note).mainloop()
    def note_del(self):
        bol = crJ.note_del(self.selected_note)
        self.after(200, self.destroy)
        if bol == True:
            showinfo(title="Информация", message="Заметка удалена ")

    def selected(self, notes_listbox):
        # получаем индексы выделенных элементов
        selected_indices = self.notes_listbox.curselection()
        print("selected_indices ", selected_indices)
        # получаем сами выделенные элементы
        self.selected_note = ",".join([self.notes_listbox.get(i) for i in selected_indices])
        msg = f"вы выбрали: {self.selected_note}"
        self.label = ttk.Label(self, text=msg).pack()
        print(self.selected_note)

    def __init__(self, res):

        super().__init__()

        self.title('результат поиска')
        self.geometry('300x300')
        self.config(bg='#446644')

        self.label = ttk.Label(self, text="\nВот что нашлось\n").pack()

        self.notes_listbox = Listbox(self, selectmode=tk.EXTENDED, width=40)
        self.notes_listbox.pack()
        ttk.Button(self, text="Изменить", command=self.change).pack()
        ttk.Button(self, text="Удалить", command=self.note_del).pack()


        x = 1
        if res == 0:
            self.notes_listbox.insert(1, "---")
            showinfo(title="Информация", message="Ничего не найдено!! ")
            self.after(500, self.destroy)
        else:
            for i in res:
                print(i)
                self.notes_listbox.insert(1, i)
                x += 1
        self.notes_listbox.bind("<<ListboxSelect>>", self.selected)
        self.after(5000, self.destroy)

if __name__ == "__main__":
    app = Radiobutton_change()
    app.mainloop()
