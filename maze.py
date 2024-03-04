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

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)
    
    def print(self):
        print("Container")

class Maze(Container):
    def __init__(self):
        super().__init__()

    def addRoom(self, room):
        self.children.append(room)

    def enter(self):
        self.children[0].enter()

    def print(self):
        print("Maze")   

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


# maze.py

class Maze(Container):
    def __init__(self):
        self.rooms = []

    def addRoom(self, room):
        self.rooms.append(room)
    
    def enter(self):
        self.rooms[0].enter()
    
    def print(self):
        print("Maze")

# room.py

class Room(MapElement):
    def __init__(self, id):
        self.id = id
        self.north = None
        self.south = None
        self.east = None
        self.west = None
    
    def enter(self):
        print("You enter room", self.id)

    def print(self):
        print("Room")

# wall.py

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
