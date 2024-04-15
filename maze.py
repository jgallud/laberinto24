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

    def isDoor(self):
        return False
    
    def recorrer(self,unBloque):
        pass
    def open(self):
        pass
    def close(self):
        pass
    def recorrer(self,unBloque):
        unBloque(self)

class Container(MapElement):
    # Composite
    def __init__(self):
        super().__init__()
        self.children = []
        self.num = None    
        self.form = None    

    def addChild(self, component):
        self.children.append(component)

    def removeChild(self, component):
        self.children.remove(component)
    
    def print(self):
        print("Container")
    
    def walkRandom(self,someone):
        pass
    def addOrientation(self, orientation):
        #self.orientations.append(orientation)
        self.form.addOrientation(orientation)
    
    def removeOrientation(self, orientation):
        #self.orientations.remove(orientation)
        self.form.removeOrientation(orientation)
    
    def getOrientations(self):
        return self.form.orientations

    def walkRandom(self, someone):        
        orientation = self.form.getRandomOrientation()
        orientation.walkRandom(someone)
   
    def goNorth(self, someone):
        #self.north.enter(someone)
        self.form.goNorth(someone)
    def goEast(self, someone):
        #self.east.enter(someone)
        self.form.goEast(someone)
    def goSouth(self, someone):
        #self.south.enter(someone)
        self.form.goSouth(someone)
    def goWest(self, someone):
        #self.west.enter(someone)
        self.form.goWest(someone)
    def setEMinOr(self, em, orientation):
        #orientation.setEMinOr(em, self)
        self.form.setEMinOr(em, orientation)
    
    def recorrer(self, unBloque):
        unBloque(self)
        for child in self.children:
            child.recorrer(unBloque)
        self.form.recorrer(unBloque)
        #for orient in self.orientations:
        #    orient.recorrerEn(unBloque,self)
    
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
    def recorrer(self, unBloque):
        unBloque(self)
        for child in self.children:
            child.recorrer(unBloque)
    def getOrientations(self):
        pass

class Room(Container):
    def __init__(self, num):
        super().__init__()
        self.num=num

    def enter(self,someone):
        print(str(someone) + " enter room" + str(self.num)+"\n")
        someone.position=self
    
    def print(self):
        print("Room")

    def isRoom(self):
        return True
    def __str__(self):
        return "Room-" + str(self.num)+"\n"    
    
class Leaf(MapElement):
    def __init__(self):
        super().__init__()
    
    def print(self):
        print("Leaf")

class Tunnel(Leaf):
    def __init__(self):
        super().__init__()
        self.maze = None
    def enter(self,someone):
        print(str(someone) + " enter Tunnel"+"\n")
        self.maze=someone.game.cloneMaze()
        self.maze.enter(someone)

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
        print(someone + " walked into a bomb"+"\n")

class Wall(MapElement):
    def __init__(self):
        pass
    
    def print(self):
        print("Wall")

    def enter(self, someone):
        print(someone , " walked into a wall"+"\n")

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
            print("The door "+str(self)+" is locked"+"\n")
    def __str__(self):
     return "Puerta-"+str(self.side1)+"-"+str(self.side2)
    
    def open(self):
        print("Opening the door between "+str(self.side1)+" and "+str(self.side2)+"\n")
        self.opened = True
    
    def close(self):
        print("Closing the door between "+str(self.side1)+" and "+str(self.side2)+"\n")
        self.opened = False

    def isDoor(self):
        return True

class Orientation:
    def __init__(self):
        pass
    def walkRandom(self, someone):
        pass
    def setEMinOr(self, em, aContainer):
        pass
    def recorrerEn(self, unBloque, aContainer):
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

    def recorrerEn(self, unBloque, aContainer):
        aContainer.north.recorrer(unBloque)

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
    
    def recorrerEn(self, unBloque, aContainer):
        aContainer.south.recorrer(unBloque)

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
    def recorrerEn(self, unBloque, aContainer):
        aContainer.east.recorrer(unBloque)
        
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

    def recorrerEn(self, unBloque, aContainer):
        aContainer.west.recorrer(unBloque)

class Northeast(Orientation):
    _instance = None
    
    def __init__(self):
        if not Northeast._instance:
            super().__init__()
            Northeast._instance = self

    @staticmethod
    def get_instance():
        if not Northeast._instance:
            Northeast()
        return Northeast._instance

    def print(self):
        print("Northeast")

    def walkRandom(self, someone):
        someone.goNortheast()

    def setEMinOr(self, em, aContainer):
        aContainer.northeast = em

    def recorrerEn(self, unBloque, aContainer):
        aContainer.northeast.recorrer(unBloque)
        
class Northwest(Orientation):
    _instance = None
    
    def __init__(self):
        if not Northwest._instance:
            super().__init__()
            Northwest._instance = self

    @staticmethod
    def get_instance():
        if not Northwest._instance:
            Northwest()
        return Northwest._instance

    def print(self):
        print("Northwest")

    def walkRandom(self, someone):
        someone.goNorthwest()

    def setEMinOr(self, em, aContainer):
        aContainer.northwest = em

    def recorrerEn(self, unBloque, aContainer):
        aContainer.northwest.recorrer(unBloque)
        
class Southeast(Orientation):
    _instance = None
    
    def __init__(self):
        if not Southeast._instance:
            super().__init__()
            Southeast._instance = self

    @staticmethod
    def get_instance():
        if not Southeast._instance:
            Southeast()
        return Southeast._instance

    def print(self):
        print("Southeast")

    def walkRandom(self, someone):
        someone.goSoutheast()

    def setEMinOr(self, em, aContainer):
        aContainer.southeast = em

    def recorrerEn(self, unBloque, aContainer):
        aContainer.southeast.recorrer(unBloque)
        
class Southwest(Orientation):
    _instance = None
    
    def __init__(self):
        if not Southwest._instance:
            super().__init__()
            Southwest._instance = self

    @staticmethod
    def get_instance():
        if not Southwest._instance:
            Southwest()
        return Southwest._instance

    def print(self):
        print("Southwest")

    def walkRandom(self, someone):
        someone.goSouthwest()

    def setEMinOr(self, em, aContainer):
        aContainer.southwest = em

    def recorrerEn(self, unBloque, aContainer):
        aContainer.southwest.recorrer(unBloque)


class Form:
    def __init__(self):
        self.orientations = []
    def addOrientation(self, orientation):
        self.orientations.append(orientation)   
    def removeOrientation(self, orientation):
        self.orientations.remove(orientation)
    def getRandomOrientation(self):
        return random.choice(self.orientations)
    def setEMinOr(self, em, orientation):
        orientation.setEMinOr(em, self)
    def recorrer(self,unBloque):
        for orient in self.orientations:
            orient.recorrerEn(unBloque,self)

class Rectangle(Form):
    def __init__(self):
        super().__init__()
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.addAllOrientations()

    def addAllOrientations(self):
        self.addOrientation(North.get_instance())
        self.addOrientation(South.get_instance())
        self.addOrientation(East.get_instance())
        self.addOrientation(West.get_instance())
    def goNorth(self, someone):
        self.north.enter(someone)
    def goEast(self, someone):
        self.east.enter(someone)
    def goSouth(self, someone):
        self.south.enter(someone)
    def goWest(self, someone):
        self.west.enter(someone)

class Hexagon(Form):
    def __init__(self):
        super().__init__()
        self.north = None
        self.northeast = None
        self.southeast = None
        self.south = None
        self.southwest = None
        self.northwest = None
        self.addAllOrientations()
    def addAllOrientations(self):
        self.addOrientation(North.get_instance())
        self.addOrientation(Northeast.get_instance())
        self.addOrientation(Southeast.get_instance())
        self.addOrientation(South.get_instance())
        self.addOrientation(Southwest.get_instance())
        self.addOrientation(Northwest.get_instance())

    def goNorth(self, someone):
        self.north.enter(someone)

    def goNortheast(self, someone):
        self.northeast.enter(someone)

    def goSoutheast(self, someone):
        self.southeast.enter(someone)

    def goSouth(self, someone):
        self.south.enter(someone)

    def goSouthwest(self, someone):
        self.southwest.enter(someone)

    def goNorthwest(self, someone):
        self.northwest.enter(someone)


