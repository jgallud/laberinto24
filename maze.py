class Game:
    def __init__(self):
        self.maze = None

    def makeWall(self):
        return Wall()
    
    def makeDoor(self,room1, room2):
        door=Door(room1, room2)
        return door

    def makeRoom(self, id):
        room=Room(id)
        room.north=self.makeWall()
        room.east=self.makeWall()
        room.south=self.makeWall()
        room.west=self.makeWall()
        return room

    def createMaze2Hab(self):
        maze = Maze()
        self.maze = maze
        room1 = Room(1)
        room2 = Room(2)

        door=Door(room1, room2)

        room1.south = door  
        room2.north = door

        self.maze.addRoom(room1)
        self.maze.addRoom(room2)

    def createMaze2HabFM(self):
        room1 = self.makeRoom(1)
        room2 = self.makeRoom(2)
        door = self.makeDoor(room1, room2)
        maze = Maze()
        maze.addRoom(room1)
        maze.addRoom(room2)
      
        room1.south = door 
        room2.north = door

        return maze
    
    def print(self):
        print("Game")

class BombedGame(Game):
  def makeWall(self):
    return BombedWall()

  def print(self):
    print("BombedGame")
  
class MapElement:
    def __init__(self):
        pass
    
    def print(self):
        print("MapElement")

class Container(MapElement):
    # Composite
    def __init__(self):
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)
    
    def print(self):
        print("Container")

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

class Maze(Container):
    def __init__(self):
        self.rooms = []

    def addRoom(self, room):
        self.rooms.append(room)
    
    def print(self):
        print("Maze")

class Room(MapElement):
    def __init__(self, id):
        self.id = id
        self.north = None
        self.south = None
        self.east = None
        self.west = None
    
    def print(self):
        print("Room")

class Wall(MapElement):
    def __init__(self):
        pass
    
    def print(self):
        print("Wall")

class BombedWall(Wall):
    def __init__(self):
        super().__init__()
        self.active = False
    
    def print(self):
        print("BombedWall")

class Door(MapElement):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
    
    def print(self):
        print("Door")

game = Game()
game.createMaze2Hab()

bgame = BombedGame()
bgame.createMaze2Hab()

game = Game()
game.createMaze2HabFM()



