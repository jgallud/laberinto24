# beast.pyclass Beast:

class Beast:
    def __init__(self, mode):
        self.mode = mode
        self.power = 2
        self.life = 10
        self.position = None
        self.mode = mode

    def isAggressive(self):
        return self.mode.isAggressive()

    def isLazy(self):
        return self.mode.isLazy()

class Mode:
    def __init__(self):
        pass
    def isAggressive(self):
        return False
    def isLazy(self):
        return False

class Aggressive(Mode):
    def __init__(self):
        super().__init__()

    def isAggressive(self):
        return True

    def print(self):
        print("Aggressive beast")

class Lazy(Mode):
    def __init__(self):
        super().__init__()
    
    def print(self):
        print("Lazy beast")

    def isLazy(self):
        return True