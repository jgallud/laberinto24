import unittest
from maze import Room
from game import Game

class TestGame(unittest.TestCase):

    def test_create4Room4BeastFM(self):
        game = Game()
        game.create4Room4BeastFM()
        
        # Check number of rooms
        self.assertEqual(len(game.maze.rooms), 4)
        self.assertEqual(len(game.beasts), 4)
        
        # Check connections between rooms
        room1 = game.maze.rooms[0]
        room2 = game.maze.rooms[1]
        room3 = game.maze.rooms[2]
        room4 = game.maze.rooms[3]
        
        self.assertIs(room1.south, room2.north)
        self.assertIs(room1.east, room3.west)
        self.assertIs(room2.east, room4.west)
        self.assertIs(room3.south, room4.north)
        
        # Check beast positions
        self.assertTrue(game.beasts[0].position.isRoom)
        self.assertTrue(game.beasts[1].position.isRoom)
        self.assertTrue(game.beasts[2].position.isRoom)
        self.assertTrue(game.beasts[3].position.isRoom)
        
        self.assertIs(game.beasts[0].position, room1)
        self.assertIs(game.beasts[1].position, room2)
        self.assertIs(game.beasts[2].position, room3)
        self.assertIs(game.beasts[3].position, room4)
        
        self.assertTrue(game.beasts[0].isAggressive())
        self.assertTrue(game.beasts[1].isLazy())
        self.assertTrue(game.beasts[2].isAggressive())
        self.assertTrue(game.beasts[3].isLazy())

       
if __name__ == '__main__':
    unittest.main()
