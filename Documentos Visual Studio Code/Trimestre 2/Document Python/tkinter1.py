# Importamos todas las funciones y clases del módulo tkinter,
# que sirve para crear interfaces gráficas en Python.
from tkinter import *

# FUNCIONES

# Esta función es la suma de los dos números ingresados.
def sumar():  
    # Obtener el valor del primer cuadro de texto (txt1) y convertirlo a entero
    numero1 = int(txt1.get())
    # Obtener el valor del segundo cuadro de texto (txt2) y convertirlo a entero
    numero2 = int(txt2.get())
    # Calcular la suma
    suma = numero1 + numero2
    # Mostrar el resultado en el cuadro de resultado (txtresult)
    # 'total' es una variable especial (StringVar) que actualiza automáticamente el cuadro de texto asociado
    return total.set(suma)


# Esta función es la resta de los dos números ingresados.
def restar():
    # Obtener el valor del primer cuadro de texto (txt1) y convertirlo a entero
    numero1 = int(txt1.get())
    # Obtener el valor del segundo cuadro de texto (txt2) y convertirlo a entero
    numero2 = int(txt2.get())
    # Calcular la resta
    resta = numero1 - numero2
    # Mostrar el resultado en el cuadro de resultado
    return total.set(resta)


# CONFIGURACIÓN VENTANA PRINCIPAL

# Se crea la ventana principal (objeto Tk)
ventanap = Tk()

# Se define el título que aparecerá en la parte superior de la ventana
ventanap.title("Calculadora suma y resta")

# Se define el tamaño de la ventana (ancho x alto)
ventanap.geometry("500x500")

# Se evita que el usuario pueda cambiar el tamaño de la ventana
ventanap.resizable(False, False)

# Se establece un color de fondo (en este caso azul claro)
ventanap.config(bg="purple")


# PRIMER NÚMERO


# Etiqueta (Label) que indica al usuario que escriba el primer número
lbl1 = Label(ventanap, text="Número 1:", bg="grey", font=("Arial", 12))
# Método pack: organiza el widget dentro de la ventana
# padx/pady = espacio externo; ipadx/ipady = espacio interno; fill=X = ocupa todo el ancho
lbl1.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)

# Cuadro de texto (Entry) donde el usuario escribirá el primer número
txt1 = Entry(ventanap, font=("Arial", 12))
# Se organiza en la ventana con los mismos parámetros
txt1.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)



# BLOQUE: SEGUNDO NÚMERO

# Etiqueta que indica al usuario que escriba el segundo número
lbl2 = Label(ventanap, text="Número 2:", bg="grey", font=("Arial", 12))
# Se organiza igual que la anterior
lbl2.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)

# Cuadro de texto (Entry) para el segundo número
txt2 = Entry(ventanap, font=("Arial", 12))
# Se organiza en la ventana
txt2.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)



# BOTONES DE OPERACIONES


# Botón para SUMAR
# - text: texto que aparece en el botón
# - bg: color de fondo
# - font: tipo y tamaño de letra
# - command=sumar: función que se ejecutará al hacer clic
btnsumar = Button(ventanap, text="Sumar", bg="lavender", font=("Arial", 12), command=sumar)
# Se coloca el botón en la ventana
btnsumar.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)

# Botón para RESTAR
# - command=restar: llama a la función restar cuando se hace clic
btnrestar = Button(ventanap, text="Restar", bg="lavender", font=("Arial", 12), command=restar)
# Se coloca el botón en la ventana
btnrestar.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)


# RESULTADO

# Etiqueta que muestra el texto "Total:"
# fg="red" cambia el color del texto a rojo
lblresult = Label(ventanap, text="Total:", bg="lavender", fg="fuchsia", font=("Arial", 12))
# Se organiza el label en la ventana
lblresult.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)

# Se crea una variable especial tipo StringVar que almacenará el resultado
# y está vinculada con el cuadro de texto donde se mostrará.
total = StringVar()

# Cuadro de texto donde se mostrará el resultado final
# - state="disabled" lo deja solo para lectura (el usuario no puede escribir ahí)
# - textvariable=total vincula la variable con este cuadro
txtresult = Entry(ventanap, state="disabled", font=("Arial", 12), textvariable=total)
# Se organiza el cuadro de resultado
txtresult.pack(padx=5, pady=3, ipadx=10, ipady=10, fill=X)


# INICIAR LA APLICACIÓN (BUCLE PRINCIPAL)

# Con mainloop() se mantiene la ventana abierta.
# Este bucle escucha los eventos del usuario (clics, escritura, etc.)
ventanap.mainloop()