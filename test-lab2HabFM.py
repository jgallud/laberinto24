import unittest
from maze import Maze, Room, Door
from game import Game

class TestMazeGame(unittest.TestCase):

    def test_create_maze(self):
        game = Game()
        maze = game.createMaze2RoomFM()
        
        self.assertIsInstance(maze, Maze)
        
        rooms = maze.rooms
        self.assertEqual(len(rooms), 2)
        
        room1, room2 = rooms
        
        self.assertIsInstance(room1, Room)
        self.assertIsInstance(room2, Room)
        
        # Verificar paredes y puertas
        self.assertIsNotNone(room1.north) 
        self.assertIsNotNone(room1.south)
        self.assertIsNotNone(room1.east)
        self.assertIsNotNone(room1.west)
        
        self.assertIsNotNone(room2.north)
        self.assertIsNotNone(room2.south)
        self.assertIsNotNone(room2.east)
        self.assertIsNotNone(room2.west)  
        
        # Verificar que las paredes sean distintas instancias
        self.assertIsNot(room1.north, room2.north)
        self.assertIsNot(room1.south, room2.south)
        
        #verifica que al sur de room1 hay un objeto de tipo puerta
        self.assertIsInstance(room1.south, Door)


if __name__ == '__main__':
    unittest.main()