# mapelement.py
class MapElement:
    def __init__(self):
        pass
    
    def enter(self):
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
    

class Maze(Container):
    def __init__(self):
        super().__init__()

    def addRoom(self, room):
        self.addChild(room)

    def enter(self):
        self.children[0].enter()

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
    def enter(self):
        print("You enter room", self.id)
    
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
    pass


class Wall(MapElement):
    def __init__(self):
        pass
    
    def print(self):
        print("Wall")

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
    
    def enter(self):
        if self.opened:
            self.side2.enter()
        else:
            print("The door is locked")
    def print(self):
        print("Door")

class Orientation:
    def __init__(self):
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
        
class East(Orientation):
    _instance = None
    def __init__(self):
        if not East._instance:
            super().__init__()
            East._instance = self

    @staticmethod
    def get_instance():
        if not East._instance:
            East()
        return East._instance
    
    def print(self):
        print("East")
        
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

