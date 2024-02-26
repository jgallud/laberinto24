from maze import Maze, Room, Door, Wall, BombedWall, Bomb 
from beast import Beast, Mode, Aggressive, Lazy

class Game:
    def __init__(self):
        self.maze = None
        self.beasts = []

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

    def createMaze2Room(self):
        maze = Maze()
        self.maze = maze
        room1 = Room(1)
        room2 = Room(2)

        door=Door(room1, room2)

        room1.south = door  
        room2.north = door

        self.maze.addRoom(room1)
        self.maze.addRoom(room2)

    def createMaze2RoomFM(self):
        room1 = self.makeRoom(1)
        room2 = self.makeRoom(2)
        door = self.makeDoor(room1, room2)
        maze = Maze()
        self.maze = maze
        self.maze.addRoom(room1)
        self.maze.addRoom(room2)
      
        room1.south = door 
        room2.north = door
    
    def addBeast(self, beast):
        self.beasts.append(beast)

    def removeBeast(self, beast):
        self.beasts.remove(beast)
    
    def makeAggressiveBeast(self):
        beast= Beast(Aggressive())
        beast.power = 5
        return beast
    
    def makeLazyBeast(self):
        beast= Beast(Lazy())
        beast.power = 1
        return beast
    
    def print(self):
        print("Game")

# BombedGame.py
class BombedGame(Game):
  def makeWall(self):
    return BombedWall()

  def print(self):
    print("BombedGame")

game = Game()
game.createMaze2Room()
game.maze.enter()

game = Game()
game.createMaze2RoomFM

game=BombedGame()
game.createMaze2RoomFM()
game.maze.enter() 