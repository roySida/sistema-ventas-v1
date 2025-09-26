from tkinter import * 
import tkinter as tk
from tkinter import ttk, messagebox

class Inventario(tk.Frame):
    def __init__(self, padre):
        super().__init__(padre)
        self.widgets()
        
    def widgets(self):
            style = ttk.Style()
            style.theme_use("default")

            style.configure("Treeview",
                            background="#f0f0f0",
                            foreground="black",
                            rowheight=30,
                            fieldbackground="#f0f0f0",
                            font=("Helvetica Neue", 12))
            style.map('Treeview', background=[('selected', '#347083')], foreground=[('selected', 'white')])

            style.configure("Treeview.Heading",
                            background="#2E86C1",
                            foreground="white",
                            font=("Helvetica Neue", 14, "bold"))

            style.configure("TButton",
                            font=("Helvetica Neue", 14, "bold"),
                            padding=6)
            style.map("TButton",
                      background=[('active', '#1B4F72'), ('!disabled', '#2E86C1')],
                      foreground=[('active', 'white'), ('!disabled', 'white')])

            frame1 = tk.Frame(self, bg="#2E86C1", highlightbackground="gray", highlightthickness=1)
            frame1.place(x=0 , y=0, width=1100, height=100)

            titulo = tk.Label(frame1, text="INVENTARIOS", bg="#2E86C1", fg="white", font=("Helvetica Neue", 28, "bold"), anchor="center")
            titulo.place(x=5, y=5, width=1090, height=90)

            #Se crea el segundo frame donde van los productos y la información 
            #Se agregan dentro de este frame los productos y la información
            frame2 = tk.Frame(self, bg="#dddddd", highlightbackground="gray", highlightthickness=1)
            frame2.place(x=0, y=100, width=1100, height=550)

            lbl_frame = LabelFrame(frame2,text="Productos", bg="#C6D9E3", font=("Helvetica Neue", 22, "bold"))
            lbl_frame.place(x=20, y=30, width=400, height=500)

            lbl_nombre = Label(lbl_frame, text="Nombre: ", bg="#C6D9E3", font=("Helvetica Neue", 14, "bold"))
            lbl_nombre.place(x=10, y=20)
            self.entry_nombre = ttk.Entry(lbl_frame, font=("Helvetica Neue", 14), width=22)
            self.entry_nombre.place(x=140, y=20, height=35)

            lbl_proveedor = Label(lbl_frame, text="Proveedor: ", bg="#C6D9E3", font=("Helvetica Neue", 14, "bold"))
            lbl_proveedor.place(x=10, y=80)
            self.entry_proveedor = ttk.Entry(lbl_frame, font=("Helvetica Neue", 14), width=22)
            self.entry_proveedor.place(x=140, y=80, height=35)

            lbl_precio = Label(lbl_frame, text="Precio: ", bg="#C6D9E3", font=("Helvetica Neue", 14, "bold"))
            lbl_precio.place(x=10, y=140)
            self.entry_precio = ttk.Entry(lbl_frame, font=("Helvetica Neue", 14), width=22)
            self.entry_precio.place(x=140, y=140, height=35)

            lbl_Costo = Label(lbl_frame, text="Costo: ", bg="#C6D9E3", font=("Helvetica Neue", 14, "bold"))
            lbl_Costo.place(x=10, y=200)
            self.entry_Costo = ttk.Entry(lbl_frame, font=("Helvetica Neue", 14), width=22)
            self.entry_Costo.place(x=140, y=200, height=35)

            lbl_stock = Label(lbl_frame, text="Cantidad: ", bg="#C6D9E3", font=("Helvetica Neue", 14, "bold"))
            lbl_stock.place(x=10, y=260)
            self.entry_stock = ttk.Entry(lbl_frame, font=("Helvetica Neue", 14), width=22)
            self.entry_stock.place(x=140, y=260, height=35)

            btn_agregar = ttk.Button(lbl_frame, text="Agregar", style="TButton")
            btn_agregar.place(x=80, y=340, width=240, height=40)

            btn_editar = ttk.Button(lbl_frame, text="Editar", style="TButton")
            btn_editar.place(x=80, y=400, width=240, height=40)

            #Aquí se va a crear una tabla con scrollbars para mostrar los productos
            frame3 = tk.Frame(frame2, bg="#dddddd", highlightbackground="gray", highlightthickness=1)
            frame3.place(x=440, y=50, width=620, height=400)

            #Se posiciona con pack para que se adapte al frame
            scroll_y = ttk.Scrollbar(frame3)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_x = ttk.Scrollbar(frame3, orient=HORIZONTAL)
            scroll_x.pack(side=BOTTOM, fill=X)

            self.tabla = ttk.Treeview(frame3, columns=("ID", "PRODUCTO", "PROVEEDOR", "PRECIO", "COSTO", "STOCK"),
                                      yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set, height=15, show="headings")
            self.tabla.pack(fill=BOTH, expand=True)

            #Se configura la función de las barras de desplazamiento con la tabla
            scroll_y.config(command=self.tabla.yview)
            scroll_x.config(command=self.tabla.xview)

            self.tabla.heading("ID", text="Id")
            self.tabla.heading("PRODUCTO", text="Producto")
            self.tabla.heading("PROVEEDOR", text="Proveedor")
            self.tabla.heading("PRECIO", text="Precio")
            self.tabla.heading("COSTO", text="Costo")
            self.tabla.heading("STOCK", text="Stock")

            self.tabla.column("ID", anchor=CENTER, width=70)
            self.tabla.column("PRODUCTO", anchor=CENTER, width=110)
            self.tabla.column("PROVEEDOR", anchor=CENTER, width=110)
            self.tabla.column("PRECIO", anchor=CENTER, width=100)
            self.tabla.column("COSTO", anchor=CENTER, width=100)
            self.tabla.column("STOCK", anchor=CENTER, width=70)

            # Zebra striping tags
            self.tabla.tag_configure('oddrow', background='white')
            self.tabla.tag_configure('evenrow', background='#E8E8E8')