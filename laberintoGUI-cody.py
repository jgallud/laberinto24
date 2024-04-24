import tkinter as tk
#import keyboard
from builder import Director
from maze import Point

class RectApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.game=None
        self.person=None

        director=Director()
        director.procesar('xxxxxx\\laberintos\\maze2room.json')
        self.game=director.getGame()

        self.title("Dibujar Rectángulos")
        self.geometry("1150x900")
        self.menubar = tk.Menu(self)
        
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Salir", command=self.quit)
        
        self.drawmenu = tk.Menu(self.menubar, tearoff=0)
        self.drawmenu.add_command(label="Lanzar bichos", command=self.game.launchThreds)
        self.drawmenu.add_command(label="Parar bichos", command=self.game.stopThreds)
        
        self.menubar.add_cascade(label="Archivo", menu=self.filemenu)  
        self.menubar.add_cascade(label="Bichos", menu=self.drawmenu)
        
        self.config(menu=self.menubar)

        self.toolbar = tk.Frame(self)
        self.b1 = tk.Button(self.toolbar, text="Lanzar bichos", command=self.button1_click)
        self.b2 = tk.Button(self.toolbar, text="Parar bichos", command=self.button2_click)
        self.b3 = tk.Button(self.toolbar, text="Abrir puertas", command=self.button3_click)
        self.b4 = tk.Button(self.toolbar, text="Cerrar puertas", command=self.button4_click)
        
        self.b1.pack(side=tk.LEFT)
        self.b2.pack(side=tk.LEFT) 
        self.b3.pack(side=tk.LEFT)
        self.b4.pack(side=tk.LEFT)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)
       
        self.game.addPerson("Pepe")
        self.person=self.game.person
        
        self.canvas = tk.Canvas(self, width=300, height=300, bg="white")
        self.canvas.pack(expand=True)
        self.mostrarLaberinto()

    def mostrarLaberinto(self):
        self.calcularPosicion()
        self.normalizar()
	    #self.calcularDimensiones
	    #self.asignarPuntosReales
    
    def calcularPosicion(self):
        if not(self.game):
            return
        h1=self.game.getRoom(1)
        h1.setPoint(Point(0,0))
        h1.calcularPosicion()

    def normalizar(self):
        minX=0
        minY=0
        for h in self.game.maze.children:
            if h.getPoint().x<minX:
                minX=h.getPoint().x
            if h.getPoint().y<minY:
                minY=h.getPoint().y
        for h in self.game.maze.children:
            point=h.getPoint()
            h.setPoint(Point(point.x+abs(minX),point.y+abs(minY)))

    def draw_rect(self,x1,y1,width,height):
       # width = int(input("Ingrese el ancho del rectángulo: "))
        #height = int(input("Ingrese el alto del rectángulo: "))
        
        #x1 = 10
        #y1 = 10
        x2 = x1 + width
        y2 = y1 + height
        
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="red")
        
    def button1_click(self):
        self.game.launchThreds()

    def button2_click(self):
        self.game.stopThreds()

    def button3_click(self):
        self.game.openDoors()

    def button4_click(self):
        self.game.closeDoors()

    def animate_sprite(self):
        # Código para animar un sprite en el canvas
        pass

    def keypress(self,event):
        """Recieve a keypress and move the ball by a specified amount"""
        print(event)
        if event.char == 'w':
            app.person.goNorth()
            #ball.move(0,-5)
        elif event.char == 's':
            app.person.goSouth()
            #ball.move(0,5)
        elif event.char == 'a':
            app.person.goWest()
            #ball.move(-5,0)
        elif event.char == 'd':
            app.person.goEast()
            #ball.move(5,0)
        elif event.char == 'enter':
            app.person.attack()
        else:
            pass
        
if __name__ == "__main__":
    app = RectApp()
    app.bind('w',app.keypress)
    app.bind('s',app.keypress)
    app.bind('d',app.keypress)
    app.bind('a',app.keypress)
    app.bind('enter',app.keypress)
    app.mainloop()
    # while True:
    #     if keyboard.is_pressed('q'):
    #         break  # Exit the program
    #     elif keyboard.is_pressed("w"): #curses.KEY_UP:
    #         app.person.goNorth()
    #     elif keyboard.is_pressed("s"): #curses.KEY_DOWN:
    #         app.person.goSouth()
    #     elif keyboard.is_pressed("a"): #curses.KEY_LEFT:
    #         app.person.goWest()
    #     elif keyboard.is_pressed("d"): #curses.KEY_RIGHT:
    #         app.person.goEast()
    #     elif keyboard.is_pressed("enter"):#curses.KEY_ENTER or key in [10, 13]:
    #         app.person.attack()
