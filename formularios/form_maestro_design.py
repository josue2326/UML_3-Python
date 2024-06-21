import tkinter as tk
from tkinter import ttk, messagebox, font
from PIL import Image, ImageTk
import datetime
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img

class Autor:
    def __init__(self, nombre, apellido, id):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id

    def mostrar_info(self):
        return f"Cliente: {self.nombre}, {self.apellido}, {self.id}"

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        return f"Categoría: {self.nombre}"

class Libro:
    def __init__(self, nombre, id, precio, cantidad):
        self.nombre = nombre
        self.id = id
        self.precio = precio
        self.cantidad = cantidad


    def mostrar_info(self):
        return (f"Producto: {self.nombre}, ID: {self.id}, Precio: {self.precio}, Cantidad: {self.cantidad} ")

class Usuario:
    def __init__(self, nombre, id, apellido, cantidad ):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.cantidad = cantidad

    def mostrar_info(self):
        return f"Producto: {self.nombre}, ID: {self.id}, Categoria: {self.apellido}, Cantidad: {self.cantidad}"

class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion=None):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def mostrar_info(self):
        return (f"Préstamo - Libro: {self.libro.titulo}, Usuario: {self.usuario.nombre} {self.usuario.apellido}, "
                f"Fecha de préstamo: {self.fecha_prestamo}, Fecha de devolución: {self.fecha_devolucion}")

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []
        self.autores = []

    def registrar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        
    def registrar_autor(self, autor):
        self.autores.append(autor)

    def realizar_prestamo(self, libro, usuario, fecha_prestamo):
        prestamo = Prestamo(libro, usuario, fecha_prestamo)
        self.prestamos.append(prestamo)

    def devolver_libro(self, libro, usuario, fecha_devolucion):
        for prestamo in self.prestamos:
            if prestamo.libro == libro and prestamo.usuario == usuario and prestamo.fecha_devolucion is None:
                prestamo.fecha_devolucion = fecha_devolucion
                return

    def mostrar_libros(self):
        if not self.libros:
            return "No hay libros registrados."
        return "\n".join(libro.mostrar_info() for libro in self.libros)

    def mostrar_usuarios(self):
        if not self.usuarios:
            return "No hay usuarios registrados."
        return "\n".join(usuario.mostrar_info() for usuario in self.usuarios)

    def mostrar_autores(self):
        if not self.autores:
            return "No hay Clientes registrados."
        return "\n".join(autor.mostrar_info() for autor in self.autores)

    def mostrar_prestamos(self):
        if not self.prestamos:
            return "No hay préstamos realizados."
        return "\n".join(prestamo.mostrar_info() for prestamo in self.prestamos)

class FormularioMaestroDesign(tk.Tk):
    def __init__(self):
        super().__init__()
        self.biblioteca = Biblioteca()
        self.init_data()
        self.logo = util_img.leer_imagen("./UML_3/imagenes/logo.png", (360, 460))
        self.perfil = util_img.leer_imagen("./UML_3/imagenes/Perfil.png", (100, 100))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()        
        self.controles_menu_lateral()
        self.controles_cuerpo()
    
    def init_data(self):
        autores = [
            Autor("Gabriel", "García Márquez", "1"),
            Autor("Leo", "Tolstoy", "2"),
            Autor("Charles", "Dickens", "3"),
            Autor("Emily", "Brontë", "4"),
            Autor("Herman", "Melville", "5"),
            Autor("Toni", "Morrison", "6"),
            Autor("Fyodor", "Dostoevsky", "7"),
            Autor("Edgar Allan", "Poe", "8"),
            Autor("Margaret", "Atwood", "9"),
            Autor("Jorge Luis", "Borges", "10")
        ]

        categorias = [
            Categoria("Granos"),
            Categoria("Lácteos"),
            Categoria("Panadería"),
            Categoria("Carnes"),
            Categoria("Frutas"),
            Categoria("Verduras"),
            Categoria("Congelados"),
            Categoria("Bebidas"),
            Categoria("Snacks"),
            Categoria("Cuidado Personal"),
            Categoria("Limpieza"),
            Categoria("Otros")
        ]

        libros = [
            Libro("Arroz", "01", 2.5, 100),
            Libro("Leche", "02", 1.8, 50),
            Libro("Pan", "03", 1.0, 80),
            Libro("Huevos", "04", 3.0, 40),
            Libro("Aceite de Oliva", "05", 5.0, 30),
            Libro("Manzanas", "06", 2.0, 60),
            Libro("Pollo", "07", 6.5, 20),
            Libro("Pasta", "08", 1.2, 70),
            Libro("Pasta", "08", 1.2, 70),
            Libro("Cereal", "09", 4.0, 50),
            Libro("Yogur", "10", 2.8, 80)
        ]
        

        for libro in libros:
            self.biblioteca.registrar_libro(libro)

        usuarios = [
            Usuario("Arroz", "01", "Granos", "1"),
            Usuario("Leche", "02", "Lácteos", "2"),
            Usuario("Pan", "03", "Panadería", "1"),
            Usuario("Huevos", "04", "Lácteos", "3"),
            Usuario("Aceite de Oliva", "05", "Aceites", "5"),
            Usuario("Manzanas", "06", "Frutas", "4"),
            Usuario("Pollo", "07", "Carnes", "2"),
            Usuario("Pasta", "08", "Granos", "6"),
            Usuario("Cereal", "09", "Cereales", "3"),
            Usuario("Yogur", "10", "Lácteos", "5")
        ]

        for usuario in usuarios:
            self.biblioteca.registrar_usuario(usuario)
    def on_enter(self, e):
        e.widget['background'] = COLOR_MENU_CURSOR_ENCIMA

    def on_leave(self, e):
        e.widget['background'] = COLOR_MENU_LATERAL
    def config_window(self):
        # Configuración inicial de la ventana
        self.title('Python GUI')
        self.iconbitmap("./UML_3/imagenes/logo.ico")
        w, h = 1024, 600        
        util_ventana.centrar_ventana(self, w, h)        

    def paneles(self):        
        # Crear paneles: barra superior, menú lateral y cuerpo principal
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')      

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False) 
        
        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)
    
    def controles_barra_superior(self):
        # Configuración de la barra superior
        font_awesome = font.Font(family='FontAwesome', size=12)

        # Etiqueta de título
        self.labelTitulo = tk.Label(self.barra_superior, text="¡MENÚ SUPERMERCADO!")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, wraplength=200)
        self.labelTitulo.pack(side=tk.LEFT, padx=(10, 0))

        # Botón del menú lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                        command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)

        # Etiqueta de información
        self.labelInfo = tk.Label(self.barra_superior, text="POOUP@unipamplona.co")
        self.labelInfo.config(fg="#fff", font=("Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10)
        self.labelInfo.pack(side=tk.RIGHT, padx=(0, 10))
    
    def toggle_panel(self):
        # Alternar la visibilidad del menú lateral
        if self.menu_lateral.winfo_viewable():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

    def controles_menu_lateral(self):
        # Configuración del menú lateral
        ancho_menu = 20
        alto_menu = 2
        self.menuLateralBtns = []

        botones_info = [
            ("Inicio", self.mostrar_inicio),
            ("Lista de Productos", self.mostrar_libros),
            ("Lista de Órdenes", self.mostrar_usuarios),
            ("Lista de Clientes", self.mostrar_autores),
            ("Crear una Orden", self.registrar_libro),
            ("Registrar un Producto", self.registrar_usuario),
            ("Registrar un Cliente", self.realizar_cliente),
            ("Salir", self.destroy)
        ]

        for (text, command) in botones_info:
            btn = tk.Button(self.menu_lateral, text=text, bg=COLOR_MENU_LATERAL, fg="white", 
                            font=("Roboto", 13, "bold"), bd=0, padx=10, pady=10, width=ancho_menu, height=alto_menu,
                            command=command)
            btn.bind("<Enter>", self.on_enter)
            btn.bind("<Leave>", self.on_leave)
            btn.pack()
            self.menuLateralBtns.append(btn)


    def controles_cuerpo(self):
        # Controles del cuerpo principal
        self.cuerpo_label = tk.Label(self.cuerpo_principal, image=self.logo, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_label.place(relx=0.5, rely=0.5, anchor='center')

    def mostrar_inicio(self):
        self.limpiar_cuerpo()
        self.cuerpo_label = tk.Label(self.cuerpo_principal, image=self.logo, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_label.place(relx=0.5, rely=0.5, anchor='center')

    def limpiar_cuerpo(self):
        for widget in self.cuerpo_principal.winfo_children():
            widget.destroy()

    def mostrar_libros(self):
        self.limpiar_cuerpo()
        info_libros = self.biblioteca.mostrar_libros()
        self.cuerpo_label = tk.Label(self.cuerpo_principal, text=info_libros, bg=COLOR_CUERPO_PRINCIPAL, justify="left", font=("Roboto", 16))
        self.cuerpo_label.pack(padx=10, pady=10)

    def mostrar_usuarios(self):
        self.limpiar_cuerpo()
        info_usuarios = self.biblioteca.mostrar_usuarios()
        self.cuerpo_label = tk.Label(self.cuerpo_principal, text=info_usuarios, bg=COLOR_CUERPO_PRINCIPAL, justify="left", font=("Roboto", 16))
        self.cuerpo_label.pack(padx=10, pady=10)

    def mostrar_prestamos(self):
        self.limpiar_cuerpo()
        info_prestamos = self.biblioteca.mostrar_prestamos()
        self.cuerpo_label = tk.Label(self.cuerpo_principal, text=info_prestamos, bg=COLOR_CUERPO_PRINCIPAL, justify="left", font=("Roboto", 16))
        self.cuerpo_label.pack(padx=10, pady=10)

    def mostrar_autores(self):
        self.limpiar_cuerpo()
        info_autores = self.biblioteca.mostrar_autores()
        self.cuerpo_label = tk.Label(self.cuerpo_principal, text=info_autores, bg=COLOR_CUERPO_PRINCIPAL, justify="left", font=("Roboto", 16))
        self.cuerpo_label.pack(padx=10, pady=10)


    def registrar_libro(self):
        self.limpiar_cuerpo()

        tk.Label(self.cuerpo_principal, text="Nombre del Producto:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        titulo_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        titulo_entry.pack()

        tk.Label(self.cuerpo_principal, text="ID del Producto:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        isbn_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        isbn_entry.pack()

        tk.Label(self.cuerpo_principal, text="Categoría:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        categoria_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        categoria_entry.pack()

        tk.Label(self.cuerpo_principal, text="Cantidad:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        cantidad_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        cantidad_entry.pack()

        def submit():
            titulo = titulo_entry.get()
            isbn = isbn_entry.get()
            cantidad = int(cantidad_entry.get())  # Convertir cantidad a entero
            categoria = categoria_entry.get()

            precio_por_defecto = 0.0  # Precio por defecto si no se proporciona

            # Crear un objeto Libro con todos los argumentos necesarios
            nuevo_producto = Libro(titulo, isbn, precio_por_defecto, cantidad)

            # Crear un objeto Usuario con la categoría y la cantidad del producto
            nueva_orden = Usuario(titulo, isbn, categoria, cantidad)

            # Registrar el nuevo producto y la nueva orden en la biblioteca
            self.biblioteca.registrar_libro(nuevo_producto)
            self.biblioteca.registrar_usuario(nueva_orden)

            messagebox.showinfo("Éxito", "Producto registrado con éxito")
            self.mostrar_usuarios()

        tk.Button(self.cuerpo_principal, text="Registrar", command=submit, width=20, font=("Roboto", 12)).pack(pady=10)



    def registrar_usuario(self):
        self.limpiar_cuerpo()

        tk.Label(self.cuerpo_principal, text="Nombre del Producto:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        nombre_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        nombre_entry.pack()

        tk.Label(self.cuerpo_principal, text="Precio:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        apellido_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        apellido_entry.pack()

        tk.Label(self.cuerpo_principal, text="Categoria:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        id_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        id_entry.pack()

        tk.Label(self.cuerpo_principal, text="Cantidad:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        cantidad_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        cantidad_entry.pack()

        def submit():
            nombre = nombre_entry.get()
            apellido = float(apellido_entry.get())
            categoria = id_entry.get()
            cantidad = cantidad_entry.get()

            nuevo_usuario = Usuario(nombre, apellido, categoria, cantidad)
            self.biblioteca.registrar_libro(nuevo_usuario)
            messagebox.showinfo("Éxito", "Producto registrado con éxito")
            self.mostrar_libros()

        tk.Button(self.cuerpo_principal, text="Registrar", command=submit, width=20, font=("Roboto", 12)).pack(pady=10)



    def realizar_cliente(self):
        self.limpiar_cuerpo()

        tk.Label(self.cuerpo_principal, text="Nombre del Cliente:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        nombre_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        nombre_entry.pack()

        tk.Label(self.cuerpo_principal, text="Apellido del Cliente:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        apellido_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        apellido_entry.pack()

        tk.Label(self.cuerpo_principal, text="ID del Cliente:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        id_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        id_entry.pack()

        def submit():
            nombre = nombre_entry.get()
            apellido = apellido_entry.get()
            id = id_entry.get()

            nuevo_autor = Autor(nombre, apellido, id)
            self.biblioteca.registrar_autor(nuevo_autor)
            messagebox.showinfo("Éxito", "Cliente registrado con éxito")
            self.mostrar_autores()

        tk.Button(self.cuerpo_principal, text="Registrar", command=submit, width=20, font=("Roboto", 12)).pack(pady=10)





