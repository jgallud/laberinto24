class Game:
    def __init__(self, maze):
        self.maze = maze

class MapElement:
    def __init__(self):
        pass

class Maze(MapElement):

    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

class Room(MapElement):

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

class Wall(MapElement):
    def __init__(self):
        pass

class Door(MapElement):
    def __init__(self, from_room, to_room):
        self.from_room = from_room
        self.to_room = to_room

maze = Maze()
room1 = Room()
room2 = Room()

maze.addRoom(room1)
maze.addRoom(room2)

door = Door(room1, room2)