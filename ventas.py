from tkinter import *
import tkinter as tk 
from tkinter import ttk, messagebox

class Ventas(tk.Frame):
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
            
            self.entry_nombre = ttk.Entry(lblframe, font="sans 12 bold", width=25)
            self.entry_nombre.place(x=330, y=10, height=28)
            
            label_valor = tk.Label(lblframe, text="Precio: ", bg="#C6D9E3", font="sans 12 bold")
            label_valor.place(x=570, y=12)
            
            self.entry_valor = ttk.Entry(lblframe, font="sans 12 bold", width=15)
            self.entry_valor.place(x=630, y=10, height=28)
            
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
