# Importar librerias

import re, sys
import tkinter as tk

# Widgets de tkinder, mensajes emergentes

from tkinter import ttk, messagebox

# Conector de base de datos MySQL

import mysql.connector as mysql
from mysql.connector import errorcode

# Modulo para validar email, sys para salir del programa

## Configuracion de la base de datos

# Conexion servidor mysql
DB_HOST = 'localhost'

# Usuario mysql
DB_USER = 'root'

# Password mysql
DB_PASSWORD = 'Yer@ld1N0912'

# Nombre base de datos
DB_NAME = 'gestor_usuarios'

# Puerto mysql
DB_PORT = 3307

### Sentencias sql ###

# Crear base de datos

SQL_CREATE_DB = f"CREATE DATABASE IF NOT EXISTS {DB_NAME} DEFAULT CHARACTER SET 'utf8'"

SQL_CREATE_TABLE = ("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(15)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
""")

## SENTENCIA INSERTAR USUARIOS

SQL_INSERT = "INSERT INTO usuarios (nombre, email, telefono) VALUES (%s, %s, %s)"

# CONSULTAR

SQL_SELECT_ALL = "SELECT * FROM usuarios"

# UPDATE

SQL_UPDATE = "UPDATE usuarios SET nombre=%s, email=%s, telefono=%s" " WHERE id=%s"

# DELETE

SQL_DELETE = "DELETE FROM usuarios WHERE id=%s"

## Validacion del email 

EMAIL_RE = re.compile(r"[^@]+@[^@]+\.[^@]+")

## Funciones de conexion a la bd
## conecta al servidor Mysql

def get_server_connection():
    return mysql.connect(host=DB_HOST, user=DB_USER, password = DB_PASSWORD, port = DB_PORT)

## Conecta a la base de datos
## conecta a la base de datos indicada o creada

def get_db_connection():
    return mysql.connect(host=DB_HOST, user=DB_USER, password = DB_PASSWORD, database= DB_NAME, port = DB_PORT)

## Asegurar la conexion a la base de datos
## Que la bd y la tabla existan o si no las crea.

def ensure_db_and_table():
    try:
        conn = get_server_connection()
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(SQL_CREATE_DB)
        cur.close; conn.close()

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(SQL_CREATE_TABLE)
        conn.commit()
        cur.close; conn.close()

    except mysql.Error as err:
        messagebox.showerror("Error de Base de Datos", f"Error: {err}")
        sys.exit(1)


## Validacion de los campos del formulario.
## Verificacmos que los datos del form son validos.

def validar (nombre, email, telefono):
    if not nombre.strip():
        return "El nombre no puede estar vacio."
    
    if not email.strip():
        return "El email no puede estar vacio."
    
    if not EMAIL_RE.match(email): ## Se valida el formato del email
        return "El email no es valido."
    
    if telefono and len(telefono) > 15:
        return "El telefono no puede tener mas de 15 caracteres."
    
    return True, ""

## Funciones adicionales o auxiliares a la base de datos

def db_write(query, params = ()): # Conecta a la base de datos
    conn = get_db_connection() # Crea un cursor para ejecutar la consulta (cursor objeto que permite ejecutar consultas)
    cur = conn.cursor() # Ejecuta la consulta
    cur.execute(query, params)
    conn.commit()
    cur.close(); conn.close() # Cierra la conexion


def db_read_all(sql): # Funcion sin parametros
    conn = get_db_connection() # Conecta a la base de datos
    cur = conn.cursor() # Crea un cursor para ejecutar la consulta
    cur.execute(sql) # Ejecuta la consulta
    rows = cur.fetchall() # Obtiene todos los resultados de todas las filas
    cur.close(); conn.close() # Cierra la conexion
    return rows # Devuelve las filas obtenidas


##  Clase principal de la aplicacion

class Usuarios(tk.Tk):
    def __init__(self): # Constructor de la clase
        super().__init__() # Llama al constructor de la clase padre
        self.title("Gestor de Usuarios") # Titulo de la ventana
        self.geometry("800x600") # Tamaño minimo de la ventana
        self.minsize(800,600) # Tamaño minimo de la ventana
        self.selected_id = None # Id del usuario seleccionado


## Contenedor principal

        container = ttk.Frame(self,padding=12)
        container.pack(fill = tk.BOTH, expand=True)

## Formulario de entrada de datos

        frm_form = ttk.LabelFrame(container, text = "Datos del Usuario", padding=12)
        frm_form.pack (fill = tk.X, expand =  True)

        # ---- Crear las StringVar ANTES de usarlas ----
        self.var_nombre = tk.StringVar()
        self.var_email = tk.StringVar()
        self.var_telefono = tk.StringVar()


        # Etiqueta y campo de entrada para el nombre
        ttk.Label(frm_form, text="Nombre: ").grid(column=0, row=0, sticky=tk.W, padx=0.8, pady=6)
        self.ent_nombre = ttk.Entry(frm_form,
        textvariable= self.var_nombre, width=35) # Campo entrada
        self.ent_nombre.grid(row=0, column=1, sticky=tk.W,pady=6)

# Sticky W=alineado a la izquierda
# Alineado a la derecha e.

# Campo Email

        ttk.Label(frm_form, text="Email").grid (row=0 ,column=2, sticky=tk.W, padx=(20.8), pady=6)

        self.var_email = tk.StringVar() # variable para email
        self.ent_email = ttk.Entry(frm_form, textvariable=self.var_email,width=35)
        self.ent_email.grid(row=0, column=3, sticky=tk.W, pady=6)


# Campo Telefono

        ttk.Label(frm_form, text="Telefono: ").grid(row=1, column=0, sticky=tk.W, padx=0.8, pady=6)
        self.var_telefono = tk.StringVar() # Variable para el telefono
        self.ent_telefono = ttk.Entry(frm_form, textvariable=self.var_telefono, width=20)
        self.ent_telefono.grid(row=1, column=1, sticky=tk.W, pady=6)


## Botones del crud insert, delete, update

        frm_buttons =ttk.Frame(frm_form)
        frm_buttons.grid(row=1, column=3, sticky="e")

# Boton Guardar

        self.btn_guardar = ttk.Button(frm_buttons, text="Guardar", command=self.crear_usuario)
        self.btn_guardar.grid(row=0, column=0, padx=5)

# Boton Actualizar

        self.btn_actualizar = ttk.Button(frm_buttons, text="Actualizar", command=self.actualizar_usuario, state="disabled")
        self.btn_actualizar.grid(row=0, column=1, padx=5)

# Boton Eliminar

        self.btn_eliminar = ttk.Button(frm_buttons, text="Eliminar", command=self.eliminar_usuario)
        self.btn_eliminar.grid(row=0, column=2, padx=5)

# Limpiar Campos

        self.btn_limpiar = ttk.Button(frm_buttons, text="Limpiar", command=self.limpiar_form)
        self.btn_limpiar.grid(row=0, column=3, padx=5)  

## Tabla para mostrar los usuarios

        frm_tabla = ttk.Frame(container, text="Usuarios", padding=10)
        frm_tabla.pack(fill=tk.BOTH, expand=True, pady=10)


## Definicion de filas y columnas con treeview
## treeview wdget para mostrar datos en forma de tabla

        self.tree = ttk.Treeview(frm_tabla, columns=("id", "Nombre", "Email", "Telefono"), show="headings", height=12)

    
## height= numero de filas visibles
## Show headings= muestra solo los encabezados de las columnas

# Definicion de los encabezados de las columnas

# For col, txt, w, anc in [...] itera sobre una lista de tuplas
# col es el identificador de la columna
# Txt es el texto de la cabecera
# W es el ancho en pixeles
# Anc es la alineacion (W = izquierda, center=centro)

        for col, txt, w, anc in [("id", "ID", 60, tk.CENTER), ("Nombre", "Nombre",220, tk.W), ("email", "Email", 260, tk.W)]:

            self.tree.heading(col, text=txt) # Encabezado de la columna
            self.tree.column(col, width=w,anchor=anc ) # Ancho y alineacion

## Barra desplazamiento vertical

            vsb= ttk.Scrollbar(frm_tabla, orient="vertical", command=self. tree.yview)
        # Yview es para desplazar verticalmente

            self.tree.configure(yscrollcommand=vsb.set)
        # Conecta la barra con la tabla

            self.tree.grid(row=0, column=0, sticky="nsew")
        # Tabla en posicion (0,0) se llena en la celda con sticky nsew

            vsb.grid(row=0, column=1, sticky="ns")
        # Barra en posicion (0,1) se llena en la celda con stricky ns

            frm_tabla.rowconfigure(0, width=1) # Fila 0 se expande con la ventana
            frm_tabla.columnconfigure(0, width=1) # Columna 0 se expande con la ventana


        # Evento sellecion de la fila en la tabla
            self.tree.bind("<<TreeviewSelect>>", self.on_select_row)
        # Bind es para enlazar un evento con una funcion
        # On select row es la funcion que se ejecuta al seleccionar una fila

            self.cargar_datos() # Carga los usuarios en la tabla

        ## Crear las funciones del crud

# --- FUNCIONES CRUD ---
    def cargar_datos(self):
        """Carga todos los usuarios desde la BD al Treeview."""
        for row in self.tree.get_children():     # limpia la tabla actual
            self.tree.delete(row)
        try:
            for (id_, nombre, email, telefono) in db_read_all(SQL_SELECT_ALL):
                self.tree.insert("", "end", values=(id_, nombre, email, telefono or ""))
        except mysql.Error as e:
            messagebox.showerror("Error BD", f"No se pudieron cargar datos:\n{e}")

    def crear_usuario(self):
        """Inserta un nuevo usuario en la base de datos."""
        nombre, email, telefono = self.var_nombre.get().strip(), self.var_email.get().strip(), self.var_telefono.get().strip()
        ok, msg = validar(nombre, email, telefono)
        if not ok:
            messagebox.showwarning("Validación", msg)
            return
        try:
            db_write(SQL_INSERT, (nombre, email, telefono or None))
            messagebox.showinfo("Éxito", "Usuario creado correctamente.")
            self.limpiar_form(); self.cargar_datos()
        except mysql.Error as e:
            if e.errno == errorcode.ER_DUP_ENTRY:
                messagebox.showerror("Error", "El email ya existe.")
            else:
                messagebox.showerror("Error BD", f"No se pudo crear el usuario:\n{e}")

    def on_select_row(self, _):
        """Carga el registro seleccionado en el formulario."""
        sel = self.tree.selection()
        if not sel: return
        id_, nombre, email, telefono = self.tree.item(sel[0])["values"]
        self.selected_id = int(id_)
        self.var_nombre.set(nombre)
        self.var_email.set(email)
        self.var_telefono.set(telefono)
        self.btn_actualizar.config(state="normal")
        self.btn_eliminar.config(state="normal")
        self.btn_guardar.config(state="disabled")

    def actualizar_usuario(self):
        """Actualiza el registro seleccionado."""
        if self.selected_id is None:
            messagebox.showwarning("Atención", "Selecciona un registro primero.")
            return
        nombre, email, telefono = self.var_nombre.get().strip(), self.var_email.get().strip(), self.var_telefono.get().strip()
        ok, msg = validar(nombre, email, telefono)
        if not ok:
            messagebox.showwarning("Validación", msg)
            return
        try:
            db_write(SQL_UPDATE, (nombre, email, telefono or None, self.selected_id))
            messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")
            self.limpiar_form(); self.cargar_datos()
        except mysql.Error as e:
            if e.errno == errorcode.ER_DUP_ENTRY:
                messagebox.showerror("Error", "El email ya existe.")
            else:
                messagebox.showerror("Error BD", f"No se pudo actualizar:\n{e}")

    def eliminar_usuario(self):
        """Elimina el usuario seleccionado."""
        if self.selected_id is None:
            messagebox.showwarning("Atención", "Selecciona un registro primero.")
            return
        if not messagebox.askyesno("Confirmar", "¿Seguro que deseas eliminar este usuario?"):
            return
        try:
            db_write(SQL_DELETE, (self.selected_id,))
            messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
            self.limpiar_form(); self.cargar_datos()
        except mysql.Error as e:
            messagebox.showerror("Error BD", f"No se pudo eliminar:\n{e}")

    def limpiar_form(self):
        """Limpia los campos del formulario."""
        self.var_nombre.set("")
        self.var_email.set("")
        self.var_telefono.set("")
        self.selected_id = None
        self.btn_actualizar.config(state="disabled")
        self.btn_eliminar.config(state="disabled")
        self.btn_guardar.config(state="normal")
        self.ent_nombre.focus_set()

# --- PUNTO DE ENTRADA ---
def main():
    ensure_db_and_table()   # garantiza que la BD exista
    app = Usuarios()# crea ventana
    app.mainloop()          # ejecuta la interfaz

if __name__ == "__main__":
    main()