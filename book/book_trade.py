import tkinter as tk
from tkinter import simpledialog

class BookExchangeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Book Exchange App")
        self.master.geometry("400x300")

        # Создаем метку для заголовка
        self.label = tk.Label(master, text="Добро пожаловать в приложение для обмена книгами!")
        self.label.pack(pady=10)

        # Создаем кнопку для добавления книги
        self.add_button = tk.Button(master, text="Добавить книгу", command=self.add_book)
        self.add_button.pack()

        # Создаем список для отображения добавленных книг
        self.book_listbox = tk.Listbox(master, width=50)
        self.book_listbox.pack(pady=10)

        # Создаем кнопку для удаления выбранной книги
        self.remove_button = tk.Button(master, text="Удалить книгу", command=self.remove_book)
        self.remove_button.pack()

    def add_book(self):
        # Добавление книги в список
        book_title = simpledialog.askstring("Добавить книгу", "Введите название книги:")
        if book_title:
            self.book_listbox.insert(tk.END, book_title)

    def remove_book(self):
        # Удаление выбранной книги из списка
        selected_index = self.book_listbox.curselection()
        if selected_index:
            self.book_listbox.delete(selected_index)

def main():
    root = tk.Tk()
    app = BookExchangeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
