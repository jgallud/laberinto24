# mapelement.py
import random

class MapElement:
    def __init__(self):
        pass
    
    def enter(self,someone):
        pass

    def print(self):
        print("MapElement")
    
    def isRoom(self):
        return False

class Container(MapElement):
    # Composite
    def __init__(self):
        super().__init__()
        self.children = []
        self.orientations=[]

    def addChild(self, component):
        self.children.append(component)

    def removeChild(self, component):
        self.children.remove(component)
    
    def print(self):
        print("Container")
    
    def walkRandom(self,someone):
        pass
    def addOrientation(self, orientation):
        self.orientations.append(orientation)
    
    def removeOrientation(self, orientation):
        self.orientations.remove(orientation)

    def walkRandom(self, someone):        
        orientation = self.getRandomOrientation()
        orientation.walkRandom(someone)

    def getRandomOrientation(self):
        return random.choice(self.orientations)
    
    def goNorth(self, someone):
        self.north.enter(someone)
    def goEast(self, someone):
        self.east.enter(someone)
    def goSouth(self, someone):
        self.south.enter(someone)
    def goWest(self, someone):
        self.west.enter(someone)
    def setEMinOr(self, em, orientation):
        orientation.setEMinOr(em, self)
    
class Maze(Container):
    def __init__(self):
        super().__init__()

    def addRoom(self, room):
        self.addChild(room)

    def enter(self,someone):
        self.children[0].enter(someone)

    def print(self):
        print("Maze")   
    
    def getRoom(self, num):
        for room in self.children:
            if room.num == num:
                return room
        return None
   

class Room(Container):
    def __init__(self, num):
        super().__init__()
        self.num = num
        self.north = None
        self.south = None
        self.east = None
        self.west = None
    def enter(self,someone):
        print(str(someone) + " enter room" + str(self.num))
        someone.position=self
    
    def print(self):
        print("Room")

    def isRoom(self):
        return True
    def __str__(self):
        return "Room-" + str(self.num)
    
class Leaf(MapElement):
    def __init__(self):
        super().__init__()
    
    def print(self):
        print("Leaf")

class Decorator(Leaf):
    def __init__(self):
        super().__init__()
        self.comp = None
    
    def print(self):
        print("Decorator")

class Bomb(Decorator):
    def __init__(self):
        super().__init__()
        self.active = False

    def print(self):
        print("Bomb")

    def enter(self, someone):
        print(someone + " walked into a bomb")

class Wall(MapElement):
    def __init__(self):
        pass
    
    def print(self):
        print("Wall")

    def enter(self, someone):
        print(someone , " walked into a wall")

# bombedwall.py

class BombedWall(Wall):
    def __init__(self):
        super().__init__()
        self.active = False
    
    def print(self):
        print("BombedWall")

# door.py

class Door(MapElement):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        self.opened = False
    
    def enter(self,someone):
        if self.opened:
            if someone.position == self.side1:
                self.side2.enter(someone)
            else:
                self.side1.enter(someone)
        else:
            print("The door "+str(self)+" is locked")
    def __str__(self):
     return "Puerta-"+str(self.side1)+"-"+str(self.side2)

class Orientation:
    def __init__(self):
        pass
    def walkRandom(self, someone):
        pass
    def setEMinOr(self, em, aContainer):
        pass

class North(Orientation):
    _instance = None
    def __init__(self):
        if not North._instance:
            super().__init__()
            North._instance = self
    def setEMinOr(self, em, aContainer):
        aContainer.north = em

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = North()
        return cls._instance

    def print(self):
        print("North")
    
    def walkRandom(self, someone):
        someone.goNorth()


class South(Orientation):
    _instance = None
    def __init__(self):
        if not South._instance:
            super().__init__()  
            South._instance = self

    @staticmethod 
    def get_instance():
        if not South._instance:
            South()
        return South._instance
    
    def print(self):
        print("South")
    
    def walkRandom(self, someone):
        someone.goSouth()
    
    def setEMinOr(self, em, aContainer):
        aContainer.south = em

class East(Orientation):
    _instance = None
    def __init__(self):
        raise RuntimeError('Call instance() instead')
        # if not East._instance:
        #     super().__init__()
        #     East._instance = self

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            # Put any initialization here.
        return cls._instance
    
    def walkRandom(self, someone):
        someone.goEast()
    
    def setEMinOr(self, em, aContainer):
        aContainer.east = em
    # @staticmethod
    # def get_instance():
    #     if not East._instance:
    #         East()
    #     return East._instance
    
    # def print(self):
    #     print("East")
        
class West(Orientation):
    _instance = None
    def __init__(self):
        if not West._instance:
            super().__init__()
            West._instance = self

    @staticmethod
    def get_instance():
        if not West._instance:
            West()
        return West._instance
    
    def print(self):
        print("West")
    
    def walkRandom(self, someone):
        someone.goWest()

    def setEMinOr(self, em, aContainer):
        aContainer.west = em