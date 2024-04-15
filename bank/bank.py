import tkinter as tk
from tkinter import messagebox

class BudgetApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Budget Manager")
        self.history = {}

        # Создаем метку и поле ввода для баланса
        self.balance_label = tk.Label(master, text="Баланс:", font=("Arial", 12))
        self.balance_label.grid(row=0, column=0, padx=10, pady=5)
        self.balance_entry = tk.Entry(master, font=("Arial", 12))
        self.balance_entry.grid(row=0, column=1, padx=10, pady=5)

        # Создаем метки для категорий
        self.categories = ["Еда", "Накопления", "Инвестиции"]
        self.category_labels = []
        for i, category in enumerate(self.categories):
            label = tk.Label(master, text=category + ":", font=("Arial", 12))
            label.grid(row=i+1, column=0, padx=10, pady=5)
            self.category_labels.append(label)

        # Создаем поля ввода для сумм
        self.category_entries = []
        for i, _ in enumerate(self.categories):
            entry = tk.Entry(master, font=("Arial", 12))
            entry.grid(row=i+1, column=1, padx=10, pady=5)
            self.category_entries.append(entry)

        # Создаем кнопку для распределения баланса
        self.allocate_button = tk.Button(master, text="Распределить", font=("Arial", 12), command=self.allocate_balance)
        self.allocate_button.grid(row=len(self.categories)+1, column=0, columnspan=2, pady=10)

        # Создаем кнопку для просмотра истории вложений
        self.history_button = tk.Button(master, text="Просмотр истории", font=("Arial", 12), command=self.show_history)
        self.history_button.grid(row=len(self.categories)+2, column=0, columnspan=2, pady=10)

    def allocate_balance(self):
        try:
            balance = float(self.balance_entry.get())
        except ValueError:
            messagebox.showerror("Ошибка", "Баланс должен быть числом")
            return

        total_allocated = 0
        allocations = []
        for entry in self.category_entries:
            try:
                allocation = float(entry.get())
                total_allocated += allocation
                allocations.append(allocation)
            except ValueError:
                messagebox.showerror("Ошибка", "Суммы должны быть числами")
                return

        if total_allocated != balance:
            messagebox.showerror("Ошибка", "Сумма распределения не соответствует балансу")
            return

        for i, category in enumerate(self.categories):
            self.history.setdefault(category, []).append(allocations[i])
            messagebox.showinfo("Успешно", f"Сумма {allocations[i]} добавлена в категорию {category}")

        # Очищаем поля ввода после распределения баланса
        self.balance_entry.delete(0, tk.END)
        for entry in self.category_entries:
            entry.delete(0, tk.END)

    def show_history(self):
        history_text = "История вложений:\n"
        for category, amounts in self.history.items():
            history_text += f"{category}: {', '.join(map(str, amounts))}\n"
        messagebox.showinfo("История вложений", history_text)

def main():
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
