import tkinter as tk

class RectApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Dibujar Rectángulos")
        self.geometry("400x400")
        
        self.menubar = tk.Menu(self)
        
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Salir", command=self.quit)
        
        self.drawmenu = tk.Menu(self.menubar, tearoff=0)
        self.drawmenu.add_command(label="Dibujar Rectángulo", command=self.draw_rect)
        
        self.menubar.add_cascade(label="Archivo", menu=self.filemenu)  
        self.menubar.add_cascade(label="Dibujar", menu=self.drawmenu)
        
        self.config(menu=self.menubar)
        
        self.canvas = tk.Canvas(self, width=300, height=300, bg="white")
        self.canvas.pack(expand=True)
        
    def draw_rect(self):
        width = int(input("Ingrese el ancho del rectángulo: "))
        height = int(input("Ingrese el alto del rectángulo: "))
        
        x1 = 10
        y1 = 10
        x2 = x1 + width
        y2 = y1 + height
        
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="red")
        
if __name__ == "__main__":
    app = RectApp()
    app.mainloop()