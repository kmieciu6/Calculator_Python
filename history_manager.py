class HistoryManager:
    def __init__(self):
        self.history = []

    def save_history(self, filename):
        with open(filename, "w") as file:
            for entry in self.history:
                file.write(f"{entry}\n")

    def load_history(self, filename):
        try:
            with open(filename, "r") as file:
                self.history = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            self.history = []

    def add_entry(self, entry):
        self.history.append(entry)