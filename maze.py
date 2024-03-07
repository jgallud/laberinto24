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

class Maze(Container):
    def __init__(self):
        super().__init__()

    def addRoom(self, room):
        self.addChild(room)

    def enter(self,someone):
        self.children[0].enter(someone)

    def print(self):
        print("Maze")   
    
    def getRoom(self, id):
        for room in self.children:
            if room.id == id:
                return room
        return None
   

class Room(Container):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.north = None
        self.south = None
        self.east = None
        self.west = None
    def enter(self,someone):
        print(someone + " enter room", self.id)
    
    def print(self):
        print("Room")

    def isRoom(self):
        return True
    
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
            self.side2.enter()
        else:
            print("The door is locked")
    def print(self):
        print("Door")

class Orientation:
    def __init__(self):
        pass
    def walkRandom(self, someone):
        pass

class North(Orientation):
    _instance = None
    def __init__(self):
        if not North._instance:
            super().__init__()
            North._instance = self

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

