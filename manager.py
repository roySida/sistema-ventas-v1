from tkinter import Tk, Frame 
from container import Container

#tkinter es una librería estandar de python para poder crear interfaces gráficas.
# TK reprensa la ventana principal de la aplicación
#frame  es un contenedor dentro de la ventana, útil para organizar otros widgets (botones, labels, entradas, etc.)


class Manager(Tk): # La clase manager es una ventana
    def __init__(self, *args, **kwargs): #Se define el constructor de la clase y *args, **kwargs: permiten pasar cualquier cantidad de parámetros adicionales al inicializar la clase. 
        super().__init__(*args, **kwargs) #llama al constructor de la clase Tk, es decir, inicializa correctamente la ventana de tkinter.
        self.title("Caja Registradora v1.0")
        self.resizable(False,False)
        self.configure(bg="#C6D9E3")
        self.geometry("800x400+120+20")
        
        self.container = Frame(self, bg="#C6D9E3")
        self.container.pack(fill="both", expand=True)
        
        self.frames = {
            Container: None
        }
        
        self.load_frames()
        
        self.show_frame(Container)
        
    def load_frames(self):
        for FrameClass in self.frames.keys():
            frame = FrameClass(self.container,self)
            self.frames[FrameClass] = frame
            
    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()
        
        

def main():
    app = Manager()
    app.mainloop()
    if __name__== "__main__":
        main()