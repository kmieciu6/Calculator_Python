import tkinter as tk
from calculator import Calculator
from history_manager import HistoryManager

def main():
    root = tk.Tk()
    history_manager = HistoryManager()
    calc = Calculator(root, history_manager)
    calc.create_widgets()
    root.mainloop()

if __name__ == "__main__":
    main()