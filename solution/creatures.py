# beast.pyclass Beast:
import time

class Creature:
    def __init__(self):
        self.position = None
        self.game=None
        self.life=None
        self.power=None
    
    def goNorth(self):
        self.position.goNorth(self)
    def goEast(self):
        self.position.goEast(self)
    def goSouth(self):
        self.position.goSouth(self)
    def goWest(self):
        self.position.goWest(self)
    def attack(self):
        enemy=self.findEnemy()
        if enemy:
            enemy.isAttackedBy(self)
    def findEnemy(self):
        pass
    def isAttackedBy(self, other):
        pass

class Person(Creature):
    def __init__(self, name):
        super().__init__()
        self.life=20
        self.power=1
        self.name=name
    def __str__(self):
        return self.name
    def findEnemy(self):
        return self.game.findBeast(self.position)
    def isAttackedBy(self, other):
        self.life -= other.power
        print(self, "is attacked by", other)
        if self.life <= 0:
            print(self, "is dead, GAME OVER")
            self.game.stopThreds()
        else:
            print(self, "life is now", self.life)

class Beast(Creature):
    def __init__(self, mode):
        super().__init__()
        self.mode = mode
        self.power = 2
        self.life = 10
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
    
    #def attack(self):
    #    self.position.attack(self)
    
    def start(self):
        self.act()

    def stop(self):
        print(self , " is stopped")
        exit(0)

    def findEnemy(self):
        return self.game.findPerson(self.position)

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
        while beast.life > 0:
            self.sleep(beast)
            self.walk(beast)
            self.attack(beast)
    def walk(self, beast):
        beast.walkRandom()
    def sleep(self, beast):
        print(beast," is sleeping")
        time.sleep(3)
    def attack(self,beast):
        beast.attack()

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