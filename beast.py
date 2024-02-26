# beast.py
class Beast:
    def __init__(self, mode):
        self.mode = mode
        self.power = 2
        self.life = 10

# mode.py
class Mode:
    def __init__(self):
        pass

class Aggressive(Mode):
    def print(self):
        print("Aggressive beast")

class Lazy(Mode):
    def print(self):
        print("Lazy beast")