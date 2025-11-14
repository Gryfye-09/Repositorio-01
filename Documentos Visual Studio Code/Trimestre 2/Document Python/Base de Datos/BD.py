# Importar librerias
import re
import sys
import tkinter as tk
from tkinter import ttk, messagebox

# Conector de base de datos MySQL
import mysql.connector as mysql
from mysql.connector import errorcode

## Configuracion de la base de datos
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'Yer@ld1N0912'
DB_NAME = 'gestor_usuarios'
DB_PORT = 3307

### Sentencias sql ###
SQL_CREATE_DB = f"CREATE DATABASE IF NOT EXISTS {DB_NAME} DEFAULT CHARACTER SET 'utf8'"
SQL_CREATE_TABLE = ("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(15)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
""")

SQL_INSERT = "INSERT INTO usuarios (nombre, email, telefono) VALUES (%s, %s, %s)"
SQL_SELECT_ALL = "SELECT * FROM usuarios"
SQL_UPDATE = "UPDATE usuarios SET nombre=%s, email=%s, telefono=%s WHERE id=%s"
SQL_DELETE = "DELETE FROM usuarios WHERE id=%s"

## Validacion del email 
EMAIL_RE = re.compile(r"[^@]+@[^@]+\.[^@]+")

## Funciones de conexion a la bd
def get_server_connection():
    return mysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, port=DB_PORT)

def get_db_connection():
    return mysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME, port=DB_PORT)

def ensure_db_and_table():
    try:
        conn = get_server_connection()
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(SQL_CREATE_DB)
        cur.close(); conn.close()

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(SQL_CREATE_TABLE)
        conn.commit()
        cur.close(); conn.close()

    except mysql.Error as err:
        messagebox.showerror("Error de Base de Datos", f"Error: {err}")
        sys.exit(1)

## Validacion de los campos del formulario.
def validar(nombre, email, telefono):
    if not nombre.strip():
        return False, "El nombre no puede estar vacio."
    if not email.strip():
        return False, "El email no puede estar vacio."
    if not EMAIL_RE.match(email):
        return False, "El email no es valido."
    if telefono and len(telefono) > 15:
        return False, "El telefono no puede tener mas de 15 caracteres."
    return True, ""

## Funciones adicionales o auxiliares a la base de datos
def db_write(query, params=()):
    conn = None
    cur = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(query, params)
        conn.commit()
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def db_read_all(sql):
    conn = None
    cur = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

##  Clase principal de la aplicacion
class Usuarios(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Usuarios")
        self.geometry("800x600")
        self.minsize(800, 600)
        self.selected_id = None

        container = ttk.Frame(self, padding=12)
        container.pack(fill=tk.BOTH, expand=True)

        # Formulario de entrada de datos
        frm_form = ttk.LabelFrame(container, text="Datos del Usuario", padding=12)
        frm_form.pack(fill=tk.X, expand=True)

        # Crear las StringVar ANTES de usarlas
        self.var_nombre = tk.StringVar()
        self.var_email = tk.StringVar()
        self.var_telefono = tk.StringVar()

        # Nombre
        ttk.Label(frm_form, text="Nombre: ").grid(column=0, row=0, sticky=tk.W, padx=0.8, pady=6)
        self.ent_nombre = ttk.Entry(frm_form, textvariable=self.var_nombre, width=35)
        self.ent_nombre.grid(row=0, column=1, sticky=tk.W, pady=6)

        # Email
        ttk.Label(frm_form, text="Email").grid(row=0, column=2, sticky=tk.W, padx=(20.8), pady=6)
        self.ent_email = ttk.Entry(frm_form, textvariable=self.var_email, width=35)
        self.ent_email.grid(row=0, column=3, sticky=tk.W, pady=6)

        # Telefono
        ttk.Label(frm_form, text="Telefono: ").grid(row=1, column=0, sticky=tk.W, padx=0.8, pady=6)
        self.ent_telefono = ttk.Entry(frm_form, textvariable=self.var_telefono, width=20)
        self.ent_telefono.grid(row=1, column=1, sticky=tk.W, pady=6)

        # Botones del crud
        frm_buttons = ttk.Frame(frm_form)
        frm_buttons.grid(row=1, column=3, sticky="e")

        self.btn_guardar = ttk.Button(frm_buttons, text="Guardar", command=self.crear_usuario)
        self.btn_guardar.grid(row=0, column=0, padx=5)

        self.btn_actualizar = ttk.Button(frm_buttons, text="Actualizar", command=self.actualizar_usuario, state="disabled")
        self.btn_actualizar.grid(row=0, column=1, padx=5)

        self.btn_eliminar = ttk.Button(frm_buttons, text="Eliminar", command=self.eliminar_usuario, state="disabled")
        self.btn_eliminar.grid(row=0, column=2, padx=5)

        self.btn_limpiar = ttk.Button(frm_buttons, text="Limpiar", command=self.limpiar_form)
        self.btn_limpiar.grid(row=0, column=3, padx=5)

        # Tabla para mostrar los usuarios (usamos LabelFrame o Frame sin text)
        frm_tabla = ttk.LabelFrame(container, text="Usuarios", padding=10)
        frm_tabla.pack(fill=tk.BOTH, expand=True, pady=10)

        # Definicion de filas y columnas con treeview
        columns = ("id", "nombre", "email", "telefono")
        self.tree = ttk.Treeview(frm_tabla, columns=columns, show="headings", height=12)

        # Definir encabezados
        self.tree.heading("id", text="ID")
        self.tree.column("id", width=60, anchor=tk.CENTER)

        self.tree.heading("nombre", text="Nombre")
        self.tree.column("nombre", width=220, anchor=tk.W)

        self.tree.heading("email", text="Email")
        self.tree.column("email", width=260, anchor=tk.W)

        self.tree.heading("telefono", text="Telefono")
        self.tree.column("telefono", width=120, anchor=tk.W)

        # Barra desplazamiento vertical (una sola vez)
        vsb = ttk.Scrollbar(frm_tabla, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)

        # Grid de tabla + scrollbar
        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")

        frm_tabla.rowconfigure(0, weight=1)
        frm_tabla.columnconfigure(0, weight=1)

        # Evento seleccion de la fila en la tabla
        self.tree.bind("<<TreeviewSelect>>", self.on_select_row)

        self.cargar_datos()

    # --- FUNCIONES CRUD ---
    def cargar_datos(self):
        """Carga todos los usuarios desde la BD al Treeview."""
        for row in self.tree.get_children():
            self.tree.delete(row)
        try:
            rows = db_read_all(SQL_SELECT_ALL)
            for (id_, nombre, email, telefono) in rows:
                self.tree.insert("", "end", values=(id_, nombre, email, telefono or ""))
        except mysql.Error as e:
            messagebox.showerror("Error BD", f"No se pudieron cargar datos:\n{e}")

    def crear_usuario(self):
        """Inserta un nuevo usuario en la base de datos."""
        nombre = self.var_nombre.get().strip()
        email = self.var_email.get().strip()
        telefono = self.var_telefono.get().strip()
        ok, msg = validar(nombre, email, telefono)
        if not ok:
            messagebox.showwarning("Validación", msg)
            return
        try:
            db_write(SQL_INSERT, (nombre, email, telefono or None))
            messagebox.showinfo("Éxito", "Usuario creado correctamente.")
            self.limpiar_form()
            self.cargar_datos()
        except mysql.Error as e:
            if hasattr(e, "errno") and e.errno == errorcode.ER_DUP_ENTRY:
                messagebox.showerror("Error", "El email ya existe.")
            else:
                messagebox.showerror("Error BD", f"No se pudo crear el usuario:\n{e}")

    def on_select_row(self, _):
        """Carga el registro seleccionado en el formulario."""
        sel = self.tree.selection()
        if not sel:
            return
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
        nombre = self.var_nombre.get().strip()
        email = self.var_email.get().strip()
        telefono = self.var_telefono.get().strip()
        ok, msg = validar(nombre, email, telefono)
        if not ok:
            messagebox.showwarning("Validación", msg)
            return
        try:
            db_write(SQL_UPDATE, (nombre, email, telefono or None, self.selected_id))
            messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")
            self.limpiar_form()
            self.cargar_datos()
        except mysql.Error as e:
            if hasattr(e, "errno") and e.errno == errorcode.ER_DUP_ENTRY:
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
            self.limpiar_form()
            self.cargar_datos()
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
    ensure_db_and_table()
    app = Usuarios()
    app.mainloop()

if __name__ == "__main__":
    main()
