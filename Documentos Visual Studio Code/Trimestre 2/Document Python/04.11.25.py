import tkinter as tk

## creamos la ventana principal
ventana = tk.Tk()

# asignar titulo a la ventana
ventana.title("Label en Tkinder")

# definir tamaño de la ventana y posicion 
# formato: ancho * alto + posicion_x + posicion_y
ventana.geometry("800x600+20+20")

# establecer minimo de la ventana
ventana.minsize(400, 300)

# establecer maximo de la ventana
ventana.maxsize(1000, 1000)

# fondo pantalla
ventana.config(bg="spring green")

## se crea un contenedor frame (labelframe)
# marco con titulo dentro de la ventana principal
Labelframe = tk.LabelFrame(ventana, text="Este es un labelframe",bg="lightblue", padx=10, pady=10)

# padx y pady son los espacios internos del frame
Labelframe.configure(width=300, height=200)

# empaquetar el frame en la ventana principal
Labelframe.pack()

# se mantiene la ventana en ejecucion hatsa que el 
# usuario lo cierre

ventana.mainloop()