# Se crea la clase Container que contendrá los botones para ir a ventas e inventario
#La libreria tkinter es utilizada para crear la interfaz gráfica del sistema
# La libreria PIL es utilizada para manejar las imágenes en la interfaz gráfica
#ventas e inventario serán otras ventanas que se abrirán al presionar los botones correspondientes
from tkinter import *
import tkinter as tk
from tkinter import ttk
from ventas import Ventas
from inventario import Inventario
from PIL import Image, ImageTk

#Se crea la clase Container que contendrá los botones para ir a ventas e inventario
class Container(tk.Frame):
    #Se inicializa la clase Container heredando de tk.Frame
    def __init__(self, padre, controlador):
        # Se inicializa la clase padre
        super().__init__(padre)
        self.controlador = controlador
        self.place(x=0, y=0, width=800, height=400)
        self.config(bg="#C6D9E3")
        self.widgets()
        
        #Se crea una función para mostrar las ventanas de ventas e inventario
        # Esta función recibe como parámetro la clase de la ventana que se desea mostrar al presionar el botón correspondiente
    def show_frames(self, container):
        #Se crea una ventana de nivel superior (Toplevel) para mostrar la ventana de ventas o inventario
        top_level = tk.Toplevel(self)
        frame = container(top_level) #Se instancia la clase de la ventana que se desea mostrar
        frame.config(bg="#C6D9E3")
        frame.pack(fill="both", expand=True)
        top_level.geometry("1100x650+120+20")
        top_level.resizable(False, False)
        
    def ventas(self):
        self.show_frames(Ventas)
        
        
    def inventario(self):
        self.show_frames(Inventario)
        
    
    def widgets(self): #En esta función se realiza toda la parte gráfica del sistema
        style = ttk.Style()
        style.configure("TButton", font=("Sans", 18, "bold"), foreground="white")
        style.map("Ventas.TButton",
                  background=[('active', '#d99a00'), ('!active', '#f4b400')])
        style.map("Inventario.TButton",
                  background=[('active', '#a52620'), ('!active', '#c62e26')])
        
        frame1 = tk.Frame(self, bg="#C6D9E3")
        frame1.place(x=0, y=0, width=800, height=400)
        
        header_frame = tk.Frame(frame1, bg="#0078d7", height=60)
        header_frame.pack(fill="x")
        header_label = tk.Label(header_frame, text="MENÚ PRINCIPAL", font=("Sans", 24, "bold"), fg="white", bg="#0078d7")
        header_label.pack(pady=10)
        
        #Se crean los botones para ir a la pantalla de ventas e inventario
        btnventas = ttk.Button(frame1, text="Ir a ventas", style="Ventas.TButton", command=self.ventas)
        btnventas.place(x=500, y=100, width=240, height=60)
        
        btninventario = ttk.Button(frame1, text="Ir a inventario", style="Inventario.TButton", command=self.inventario)
        btninventario.place(x=500, y=180, width=240, height=60)
        
        #Se agrega una imagen al frame1 usando PIL con try/except
        try:
            self.logo_image = Image.open("imagenes/Castelano2.png")
            self.logo_image = self.logo_image.resize((280,280))
            self.logo_image = ImageTk.PhotoImage(self.logo_image)
            self.logo_label = tk.Label(frame1, image=self.logo_image, bg="#C6D9E3")
            self.logo_label.place(x=100, y=70)
        except Exception:
            pass
        
        #Se agrega un label con el nombre del sistema y el autor
        copyright_label = tk.Label(frame1, text="© 2025 Rodrigo Sida. Todos los derechos reservados", font="sans 12 bold", bg="#C6D9E3", fg="red")
        copyright_label.place(x=180, y=350)