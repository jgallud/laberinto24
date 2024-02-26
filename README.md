# Maze Game 2024
Proyecto del laberinto del curso 23-24

The code in this repository has been developed with the assistance of SourceGraph Cody

Initial prompt:
```
Write a python program with the next objects: Maze, Wall, Door and Room. 
The Maze object has a collection of Room objects. 
The Room object has four sides (north, east, west, south), initially each side is a Wall object. 
The Door object has two sides that might be Room objects. 
The Maze object has an operation addRoom with a Room object as parameter.
```
Decorator prompt:
```
include a new class named Decorator. This new class is subclass of MapElement
```	
Composite prompt:
```	
apply the Composite design pattern to this solution: MapElement is the Component class, Container is subclass of MapElement and Room is subclass of Container class. 
A new class Leaf is subclass of MapElement.
Decorator class is now subclass of Leaf
```