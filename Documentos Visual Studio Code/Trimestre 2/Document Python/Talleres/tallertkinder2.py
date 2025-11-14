from tkinter import *

# Ventana principal de la aplicación

root = Tk()
root.title("Taller de Tkinter - Marcos y Tablero")
root.config(bg="white")

# 5) Tablero tipo ajedrez

tablero_contenedor = Frame(root)
tablero_contenedor.pack(pady=10)

FILAS = 8
COLUMNAS = 8
TAM_CASILLA = 40 

COLOR1 = "white"
COLOR2 = "black"


for fila in range(FILAS):
    for col in range(COLUMNAS):
       
        color = COLOR1 if (fila + col) % 2 == 0 else COLOR2
       
        casilla = Frame(tablero_contenedor, width=TAM_CASILLA, height=TAM_CASILLA, bg=color)
        
        casilla.grid(row=fila, column=col)
       
        casilla.grid_propagate(False)

root.mainloop()
