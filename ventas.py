import sqlite3
from tkinter import *
import tkinter as tk 
from tkinter import ttk, messagebox


class Ventas(tk.Frame):
    db_name = "database.db" #Se crea la variable db_name para almacenar el nombre de la base de datos
    
    def __init__(self, parent):
        super().__init__(parent)
        self.widgets()
        
    def widgets(self): #Para trabajar con interfaces gráficas
            
            style = ttk.Style()
            style.theme_use("clam")
            style.configure("Treeview.Heading", background="#4a6984", foreground="white", font=("sans", 12, "bold"))
            style.configure("Treeview", font=("sans", 11), rowheight=25, fieldbackground="#e1e1e1")
            style.map("Treeview", background=[('selected', '#347083')], foreground=[('selected', 'white')])
            style.configure("TButton", font=("sans", 12, "bold"))
            
            frame1 = tk.Frame(self, bg="#dddddd", highlightbackground="gray", highlightthickness=1)
            frame1.pack()
            frame1.place(x=0 , y=0, width=1100, height=100)
            
            header_frame = tk.Frame(frame1, bg="#2E86C1")
            header_frame.place(x=5, y=5, width=1090, height=90)
            titulo = tk.Label(
                header_frame,
                text="VENTAS",
                bg="#2E86C1",
                fg="white",
                font=("Helvetica Neue", 32, "bold"),
                anchor="center"
            )
            titulo.pack(expand=True, fill="both")
            3
            frame2 = tk.Frame(self, bg="#dddddd", highlightbackground="gray", highlightthickness=1)
            frame2.place(x=0, y=100, width=1100, height=550)
            
            lblframe = LabelFrame(frame2,text="Información de la venta", bg="#C6D9E3", font="sans 16 bold")
            lblframe.place(x=10, y=10, width=1060, height=80)
            
            label_numero_factura = tk.Label(lblframe, text="Número de \nfactura", bg="#C6D9E3", font="sans 12 bold")
            label_numero_factura.place(x=10, y=5)
            self.numero_factura = tk.StringVar()  
            self.entry_numero_factura = ttk.Entry(lblframe, textvariable=self.numero_factura, state="readonly", font="sans 12 bold", width=12)
            self.entry_numero_factura.place(x=100, y=5, height=28)
            
            label_nombre = tk.Label(lblframe, text="Productos: ", bg="#C6D9E3", font="sans 12 bold")
            label_nombre.place(x=250, y=12)          
            self.entry_nombre = ttk.Combobox(lblframe, font="sans 12 bold", width=25, state="readonly")
            self.entry_nombre.place(x=330, y=10, height=28)
            
            self.cargar_productos() #Llama al método cargar_productos para llenar el combobox con los productos disponibles en la base de datos
            
            label_valor = tk.Label(lblframe, text="Precio: ", bg="#C6D9E3", font="sans 12 bold")
            label_valor.place(x=570, y=12)           
            self.entry_valor = ttk.Entry(lblframe, font="sans 12 bold", width=15, state="readonly")
            self.entry_valor.place(x=630, y=10, height=28)
            
            #Cuando se selecciona un producto del combobox, se llama al método cargar_valor para actualizar el campo de precio
            self.entry_nombre.bind("<<ComboboxSelected>>", lambda event: self.cargar_valor())
            
            label_cantidad = tk.Label(lblframe, text="Cantidad: ", bg="#C6D9E3", font="sans 12 bold")
            label_cantidad.place(x=780, y=12)         
            self.entry_cantidad = ttk.Entry(lblframe, font="sans 12 bold", width=10)
            self.entry_cantidad.place(x=850, y=10, height=28)
            
            #Se crea otro frame dentro del frame2 para colocar la tabla de productos
            treFrame = tk.Frame(frame2, bg="#dddddd", highlightbackground="gray", highlightthickness=1)
            treFrame.place(x=150, y=120, width=800, height=200)
            
            #Barras de desplazamiento para la tabla de productos
            scrol_y = ttk.Scrollbar(treFrame, orient=VERTICAL)
            scrol_y.pack(side=RIGHT, fill=Y)
            
            scrol_x = ttk.Scrollbar(treFrame, orient=HORIZONTAL)
            scrol_x.pack(side=BOTTOM, fill=X)
            
            #Crear la tabla donde se mostrarán los productos agregados a la venta
            self.tree = ttk.Treeview(treFrame, columns=("Producto", "Precio", "Cantidad", "Subtotal"), show="headings", height=10 ,yscrollcommand=scrol_y.set, xscrollcommand=scrol_x.set)
            scrol_y.config(command=self.tree.yview)
            scrol_x.config(command=self.tree.xview)
            
            #Crear los encabezados de la tabla
            self.tree.heading("#1", text="Producto")
            self.tree.heading("#2", text="Precio")
            self.tree.heading("#3", text="Cantidad")
            self.tree.heading("#4", text="Subtotal")
            
            self.tree.column("#1", anchor=CENTER, width=200)
            self.tree.column("#2", anchor=CENTER, width=150)
            self.tree.column("#3", anchor=CENTER, width=150)
            self.tree.column("#4", anchor=CENTER, width=150)
            
            self.tree.tag_configure('oddrow', background='white')
            self.tree.tag_configure('evenrow', background='#f2f2f2')
            
            self.tree.pack(expand=True, fill=BOTH)
            
            #Se van a crear los botones para agregar, eliminar y limpiar productos dentro del frame2
            #Para ello se crea un LabelFrame dentro del frame2 para colocar los botones
            lblframe1 = LabelFrame(frame2,text="Opciones", bg="#C6D9E3", font="sans 16 bold")
            lblframe1.place(x=10, y=380, width=1060, height=100)
            
            #Se agregan los botones dentro del lblframe1 para agregar, eliminar y pagar productos
            btn_agregar = ttk.Button(lblframe1, text="➕ Agregar producto")
            btn_agregar.place(x=50, y=10, width=240, height=50)
            
            btn_pagar = ttk.Button(lblframe1, text="💰 Pagar")
            btn_pagar.place(x=400, y=10, width=240, height=50)
            
            btn_facturas = ttk.Button(lblframe1, text="📄 Ver Facturas")
            btn_facturas.place(x=750, y=10, width=240, height=50)
            
            self.label_suma_total = tk.Label(frame2, text="Total a pagar: 0.00", bg="#C6D9E3", font="sans 20 bold")
            self.label_suma_total.place(x=360, y=335)
         
         #Aquí se realiza la conexión a la base de datos y se cargan los productos en la tabla   
    def cargar_productos(self):
        try:
            conn = sqlite3.connect(self.db_name) #Conecta a la base de datos SQLite especificada por db_name
            c = conn.cursor() #Crea un cursor para ejecutar comandos SQL en la base de datos
            c.execute("SELECT vch_nombre FROM Inventario") #Ejecuta una consulta SQL para seleccionar todos los nombres de productos de la tabla Inventario
            productos = c.fetchall() #fetchall() obtiene todas las filas del resultado de la consulta
            self.entry_nombre["values"] = [producto[0] for producto in productos] #Llena el combobox con los nombres de los productos obtenidos de la base de datos
            if not productos:
                messagebox.showinfo("Información", "No hay productos disponibles en el inventario.")
            conn.close() #Cierra la conexión a la base de datos
        except sqlite3.Error as e:
            #Se imprime el error en la consola y muestra un mensaje de error al usuario
            messagebox.showerror("Error de base de datos", f"Ocurrió un error al cargar los productos: {e}")
            
    def cargar_valor(self, event):
        nombre_producto = self.entry_nombre.get()
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("SELECT precio FROM Inventario WHERE vch_nombre = ?", (nombre_producto,)) #Consulta SQL para obtener el precio del producto seleccionado en el combobox || ? es un marcador de posición para evitar inyecciones SQL
            precio = c.fetchone() #fetchone() obtiene la primera fila del resultado de la consulta
            if precio:
                self.entry_valor.config(state="normal") #Habilita la entrada para poder modificar su contenido
                self.entry_valor.delete(0, tk.END) #Limpia cualquier valor previo en la entrada hasta el final
                self.entry_valor.insert(0, str(precio[0])) #Inserta el precio obtenido de la base de datos en la entrada
                self.entry_valor.config(state="readonly") #Vuelve a poner la entrada en modo solo lectura para evitar modificaciones manuales
            else:
                self.entry_valor.config(state="normal")
                self.entry_valor.delete(0, tk.END)
                self.entry_valor.insert(0, "Precio no encontrado")
                self.entry_valor.config(state="readonly")
        except sqlite3.Error as e:
            messagebox.showerror("Error de base de datos", f"Ocurrió un error al obtener el precio: {e}")
        finally:
            conn.close()
            
    def actualizar_total(self):
        total = 0.0
        for child in self.tree.get_children(): #get_children() obtiene todos los elementos (filas) en el árbol (tabla)
            subtotal = float(self.tree.item(child, 'values')[3]) #item() obtiene los valores de una fila específica, 'values' devuelve una tupla con los valores de las columnas
            total += subtotal #Se suma el subtotal de cada fila al total
        self.label_suma_total.config(text=f"Total a pagar: {total:.2f}") #Actualiza la etiqueta que muestra el total a pagar, formateando el total a dos decimales
        # El método actualizar_total recorre todas las filas de la tabla, suma los subtotales y actualiza la etiqueta que muestra el total a pagar.
        #{total:.2f} formatea el número total para que siempre muestre dos decimales, incluso si es un número entero.
        #2f indica que se desea un número de punto flotante con dos dígitos después del punto decimal.
        
    def registrar(self):
        producto = self.entry_nombre.get() #Obtiene el nombre del producto seleccionado en el combobox
        precio = self.entry_valor.get() #Obtiene el precio del producto desde la entrada de texto
        cantidad = self.entry_cantidad.get() #Obtiene la cantidad ingresada por el usuario en la entrada de texto
        
        if producto and precio and cantidad:
            try:
                cantidad = int(cantidad) #Convierte la cantidad a un entero
                if not self.verificar_stock(producto, cantidad):
                    messagebox.showerror("Error", f"No hay suficiente stock para el producto '{producto}'.")
                    return
                precio = float(precio) #Convierte el precio a un número de punto flotante
                subtotal = precio * cantidad #Calcula el subtotal multiplicando el precio por la cantidad
                
                #Determina si la fila es par o impar para aplicar el color de fondo correspondiente
                if len(self.tree.get_children()) % 2 == 0:
                    fila_tag = 'evenrow'
                else:
                    fila_tag = 'oddrow'
                    
                #Agrega una nueva fila a la tabla con los valores del producto, precio, cantidad y subtotal
                self.tree.insert('', 'end', values=(producto, f"{precio:.2f}", cantidad, f"{subtotal:.2f}"), tags=(fila_tag,))
                
                #Limpia las entradas después de agregar el producto a la tabla
                self.entry_nombre.set('')
                self.entry_valor.config(state="normal")
                self.entry_valor.delete(0, tk.END)
                self.entry_valor.config(state="readonly")
                self.entry_cantidad.delete(0, tk.END)
                
                self.actualizar_total() #Actualiza el total a pagar después de agregar el producto
                
            except ValueError:
                messagebox.showerror("Error de entrada", "Cantidad o precio no válido")
                
        else: 
            messagebox.showerror("Error", "Completar todos los campos")
     
     #Verifica si hay suficiente stock del producto en la base de datos antes de agregarlo a la venta       
    def verificar_stock(self, nombre_producto, cantidad):  #Esta función recibe el nombre del producto y la cantidad solicitada || y self es una referencia a la instancia actual de la clase Ventas
        try:
            conn = sqlite3.connect(self.db_name) #Creamos variable conn para conectar a la base de datos
            c = conn.cursor() #Creamos variable c para ejecutar comandos SQL en la base de datos
            c.execute("SELECT int_stock FROM Inventario WHERE vch_nombre = ?", (nombre_producto,)) #Consulta SQL para obtener el stock del producto especificado
             #? es un marcador de posición para evitar inyecciones SQL
            stock = c.fetchone() #fetchone() obtiene la primera fila del resultado de la consulta
            if stock and stock[0] >= cantidad: #Verifica si se encontró el producto y si el stock es suficiente
                return True
            return False
        except sqlite3.Error as e: #Captura cualquier error relacionado con la base de datos
            messagebox.showerror("Error de base de datos", f"Error al verificar el stock: {e}") #Muestra un mensaje de error al usuario
            return False
        finally:
            conn.close() #Cierra la conexión a la base de datos
        
            
