from tkinter import *

# Ventana principal de la aplicación

root = Tk()
root.title("Taller de Tkinter - Marcos y Tablero")
root.config(bg="white")


# 1) Marco

marco_texto = LabelFrame(root, text="Taller Tkinder ", width=300, height=300)

# (2) Márgenes frente a la ventana

marco_texto.pack(padx=25, pady=10)
marco_texto.pack_propagate(False)


# 3) Dos marcos vacíos lado a lado

contenedor = Frame(root)
contenedor.pack(pady=5)

# Marco izquierdo
marco_izq = Frame(contenedor, width=200, height=400, bg="violet", bd=0, relief='flat', highlightthickness=0)
marco_izq.pack(side=LEFT)
marco_izq.pack_propagate(False)

# Marco derecho
marco_der = Frame(contenedor, width=200, height=400, bg="pink", bd=0, relief='flat', highlightthickness=0)
marco_der.pack(side=RIGHT)
marco_der.pack_propagate(False)


# 4) Los marcos no están perfectamente juntos

marco_izq.config(bd=0, relief='flat', highlightthickness=0)
marco_der.config(bd=0, relief='flat', highlightthickness=0)

root.mainloop()