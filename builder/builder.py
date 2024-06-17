import json
#import curses
import keyboard
import sys
import os
sys.path.append(os.getcwd())

from solution.game import Game
from solution.maze import Maze, Room, Door, Wall, Bomb, Rectangle, Hexagon, North, East, South, West, Northeast, Southeast, Southwest, Northwest,Open,Close,Enter
from solution.creatures import Beast,Aggressive,Lazy
import time

class Director:
    def __init__(self):
        self.dict=None
        self.builder=None

    def procesar(self,filename):
        self.leer_archivo(filename)
        self.iniBuilder()
        self.crear_laberinto()
        self.crear_game()
        self.crear_beasts()

    def leer_archivo(self, filename):
        try:
            with open(filename) as f:
                data = json.load(f)
                self.dict= data
        except FileNotFoundError:
            print(f"File {filename} does not exist")
            return None
    
    def iniBuilder(self):
        if (self.dict['form'] == 'rectangle'):
            self.builder=LaberintoBuilder()
        elif (self.dict['form'] == 'hexagon'):
            self.builder=LaberintoHexagonalBuilder()
        else:
            print("Form not found")
            return None

    def getGame(self):
        return self.builder.getGame()

    def crear_game(self):
        self.builder.makeGame()

    def crear_laberinto(self):
        self.builder.makeMaze()
        
        for each in self.dict['maze']:
            self.crear_laberinto_recursivo(each, 'root')
            
        for each in self.dict['doors']:
            n1 = each[0]
            or1 = each[1]
            n2 = each[2]
            or2 = each[3]
            self.builder.makeDoor(n1, or1, n2, or2)
    
    def crear_laberinto_recursivo(self, un_dic, padre):
    
        if un_dic['tipo'] == 'room':
            con = self.builder.makeRoom(un_dic['num'])
            
        if un_dic['tipo'] == 'bomb':
            self.builder.makeBombIn(padre)
            
        if 'hijos' in un_dic:
            for each in un_dic['hijos']:
                self.crear_laberinto_recursivo(each, con)

    def crear_beasts(self):
        for each in self.dict['beasts']:
            modo = each['modo']
            if modo == 'Aggressive':
                self.builder.makeAggressiveBeastPosition(each['posicion'])
            elif modo == 'Lazy':
                self.builder.makeLazyBeastPosition(each['posicion'])

class LaberintoBuilder:
    def __init__(self):
        self.game = None
        self.maze = None
    
    def getGame(self):
        return self.game
    
    def makeGame(self):
        self.game = Game()
        self.game.prototype =self.maze
        self.game.maze = self.game.cloneMaze()

    def makeForm(self,num):
        return Rectangle(num)
     
    def makeMaze(self):
        self.maze= Maze()
    
    def makeWall(self):
        return Wall()
    
    def makeDoor(self,room1, room2):
        door=Door(room1, room2)
        return door

    def makeBombIn(self, room):
        bomb=Bomb()
        room.addChild(bomb)
        return bomb

    def makeRoom(self, num):
        room=Room(num)
        room.form=self.makeForm(num)
        # room.addOrientation(self.makeNorth())
        # room.addOrientation(self.makeEast())
        # room.addOrientation(self.makeSouth())
        # room.addOrientation(self.makeWest())
        for each in room.getOrientations():
            each.setEMinOr(self.makeWall(), room.form)
        self.maze.addRoom(room)
        return room

    def makeNorth(self):
        return North().get_instance()

    def makeEast(self):
        return East.get_instance()
    
    def makeSouth(self):
        return South().get_instance()
    
    def makeWest(self):
        return West().get_instance()
    
    def makeDoor(self, un_num, una_or_string, otro_num, otra_or_string):
        lado1 = self.maze.getRoom(un_num)
        lado2 = self.maze.getRoom(otro_num)
        
        or1 = getattr(self, 'make'+una_or_string)()
        or2 = getattr(self, 'make'+otra_or_string)()
        
        pt = Door(lado1, lado2)
        pt.addCommand(Open(pt))
        lado1.setEMinOr(pt,or1) 
        lado2.setEMinOr(pt,or2)

    def makeAggressiveBeast(self):
        return Beast(Aggressive())
    def makeLazyBeast(self):
        return Beast(Lazy())
    def makeAggressiveBeastPosition(self, num):
        room=self.game.getRoom(num)
        beast=self.makeAggressiveBeast()
        beast.position=room
        self.game.addBeast(beast)
    def makeLazyBeastPosition(self, num):
        room=self.game.getRoom(num)
        beast=self.makeLazyBeast()
        beast.position=room
        self.game.addBeast(beast)

class LaberintoHexagonalBuilder(LaberintoBuilder):
    def makeForm(self):
        return Hexagon()
    
    def makeRoom(self):
        room = Room()
        room.form = self.makeForm()                           
        for each in room.getOrientations():
            each.setEMinOr(self.makeWall(), room.form)
        self.maze.addRoom(room)
        return room
      

def main(): #stdscr

    director=Director()
    director.procesar(os.getcwd()+'\\json\\maze2room.json')
    game=director.getGame()
    game.addPerson("Pepe")
    person=game.person
    game.openDoors()
    game.launchThreds()
    
    while True:
        if keyboard.is_pressed('q'):
            break  # Exit the program
        elif keyboard.is_pressed("w"): #curses.KEY_UP:
            person.goNorth()
        elif keyboard.is_pressed("s"): #curses.KEY_DOWN:
            person.goSouth()
        elif keyboard.is_pressed("a"): #curses.KEY_LEFT:
            person.goWest()
        elif keyboard.is_pressed("d"): #curses.KEY_RIGHT:
            person.goEast()
        elif keyboard.is_pressed("enter"):#curses.KEY_ENTER or key in [10, 13]:
            person.attack()
    game.stopThreds()
#main()


