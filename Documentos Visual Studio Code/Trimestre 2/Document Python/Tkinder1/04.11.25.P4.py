from tkinter import *

ventana = Tk()

## funcion para ejecutar un boton
def click_boton():
    texto = Label(ventana, text="Has presionado el boton").grid()

# grid para organizar los elementos en la ventana

## crear un botonm y presionar para ejecutar el texto de la funcion
boton = Button(ventana, text="Presioname", bg="green", padx=80, pady=30, command=click_boton).grid(row=1, column=0)

## padx y pady son los espacios internos del boton
boton1= Button (ventana, text="Salir", bg="red", padx=80, pady=30, command=ventana.destroy). grid(row=2, column=2)

ventana.mainloop()