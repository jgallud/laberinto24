# beast.pyclass Beast:
import time

class Beast:
    def __init__(self, mode):
        self.mode = mode
        self.power = 2
        self.life = 10
        self.position = None
        self.mode = mode
        self.num=0
    
    def __str__(self):
        template='Beast-{0.mode}{0.num}'
        return template.format(self)
    
    def isAggressive(self):
        return self.mode.isAggressive()

    def isLazy(self):
        return self.mode.isLazy()
    
    def act(self):
        self.mode.act(self)
    
    def walkRandom(self):
        self.position.walkRandom(self)
    
    def goNorth(self):
        self.position.goNorth(self)
    def goEast(self):
        self.position.goEast(self)
    def goSouth(self):
        self.position.goSouth(self)
    def goWest(self):
        self.position.goWest(self)
    def start(self):
        self.act()
    def stop(self):
        print(self , " is stopped")
        exit(0)

class Mode:
    def __init__(self):
        pass
    def __str__(self):    
        pass
    def isAggressive(self):
        return False
    def isLazy(self):
        return False
    def act(self, beast):
        self.sleep(beast)
        self.walk(beast)
    def walk(self, beast):
        beast.walkRandom()
    def sleep(self, beast):
        print(beast," is sleeping")
        time.sleep(3)

class Aggressive(Mode):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return "Aggressive"
    
    def isAggressive(self):
        return True

    def print(self):
        print("Aggressive beast")

class Lazy(Mode):
    def __init__(self):
        super().__init__()
    
    def __str__(self):    
        return "Lazy"
    
    def print(self):
        print("Lazy beast")

    def isLazy(self):
        return True