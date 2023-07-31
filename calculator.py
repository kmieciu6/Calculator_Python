import tkinter as tk

class Calculator:
    def __init__(self, root, history_manager):
        self.root = root
        self.history_manager = history_manager
        self.root.title("Kalkulator")

    def create_widgets(self):
        # Tworzymy widżet wyświetlacza
        self.display = tk.Entry(self.root, width=20, font=('Arial', 20), justify='right')
        self.display.grid(row=0, column=0, columnspan=4)

        # Tworzymy przyciski cyfr od 0 do 9
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
            ('0', 4, 1)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(self.root, text=text, font=('Arial', 20), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column)

        # Dodajemy przyciski dla operacji
        operators = ['+', '-', '*', '/']
        for i, operator in enumerate(operators):
            button = tk.Button(self.root, text=operator, font=('Arial', 20),
                               command=lambda o=operator: self.on_operator_click(o))
            button.grid(row=i + 1, column=3)

        # Dodajemy przyciski "=" i "C"
        equals_button = tk.Button(self.root, text='=', font=('Arial', 20), command=self.on_equal_click)
        equals_button.grid(row=4, column=2)
        
        clear_button = tk.Button(self.root, text='C', font=('Arial', 20), command=self.on_clear_click)
        clear_button.grid(row=4, column=0)

        history_button = tk.Button(self.root, text='Historia', font=('Arial', 20), command=self.show_history)
        history_button.grid(row=0, column=4)

    def on_button_click(self, value):
        # Obsługuje kliknięcie na przyciski z cyframi
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, current + value)

    def on_operator_click(self, operator):
        # Obsługuje kliknięcie na przyciski z operacjami (+, -, *, /)
        current = self.display.get()
        if current and current[-1].isdigit():
            self.display.insert(tk.END, operator)

    def on_equal_click(self):
        # Obsługuje kliknięcie na przycisk "="
        equation = self.display.get()
        try:
            result = eval(equation)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
            self.result = result  # Zapisujemy wynik jako liczbę
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Błąd")
            self.result = None  # Ustawiamy wynik na None w przypadku błędu

        if self.result is not None:  # Sprawdzamy, czy wynik nie jest pusty
            history_entry = f"{equation} = {self.result}"
            self.history_manager.add_entry(history_entry)

    def on_clear_click(self):
        # Obsługuje kliknięcie na przycisk "C"
        self.display.delete(0, tk.END)

    def show_history(self):
        # Okno dialogowe do wyświetlenia historii
        history_window = tk.Toplevel(self.root)
        history_window.title("Historia Obliczeń")
        history_text = tk.Text(history_window, width=40, height=10, font=('Arial', 12))
        history_text.pack()

        for entry in self.history_manager.history:
            history_text.insert(tk.END, entry + "\n")

        history_text.config(state=tk.DISABLED)