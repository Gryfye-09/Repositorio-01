from tkinter import *

#FUNCION SUMAR
def sumar():  
   
    numero1 = int(txt1.get())
    numero2 = int(txt2.get())
    suma = numero1 + numero2
    return total.set(suma)

#FUNCION RESTAR
def restar():
   
    numero1 = int(txt1.get())
    numero2 = int(txt2.get())
    resta = numero1 - numero2
    return total.set(resta)

#FUNCION MULTIPLICAR
def multiplicar():
 
    numero1 = int(txt1.get())
    numero2 = int(txt2.get())
    producto = numero1 * numero2
    return total.set(producto)

#FUNCION DIVIDIR
def dividir():
    
    numero1 = int(txt1.get())
    numero2 = int(txt2.get())
    if numero2 != 0:
        division = numero1 / numero2
        return total.set(division)
    else:
        return total.set("Error: división entre 0")


# VENTANA

ventanap = Tk()


ventanap.title("Calculadora suma y resta")

ventanap.geometry("500x500")

ventanap.resizable(False, False)

ventanap.config(bg="purple")

#NUMERO 1

lbl1 = Label(ventanap, text="Número 1:", bg="grey", font=("Arial", 12))
lbl1.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)

txt1 = Entry(ventanap, font=("Arial", 12))
txt1.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)


#NUMERO 2

lbl2 = Label(ventanap, text="Número 2:", bg="grey", font=("Arial", 12))
lbl2.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)

txt2 = Entry(ventanap, font=("Arial", 12))
txt2.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)



# SUMAR
btnsumar = Button(ventanap, text="Sumar", bg="lavender", font=("Arial", 12), command=sumar)
btnsumar.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)

# RESTAR
btnrestar = Button(ventanap, text="Restar", bg="lavender", font=("Arial", 12), command=restar)
btnrestar.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)

# MULTIPLICAR
btnmultiplicar = Button(ventanap, text="Multiplicar", bg="lavender", font=("Arial", 12), command=multiplicar)
btnmultiplicar.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)

#DIVIDIR
btndividir = Button(ventanap, text="Dividir", bg="lavender", font=("Arial", 12), command=dividir)
btndividir.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)


# RESULTADO

lblresult = Label(ventanap, text="Total:", bg="lavender", fg="fuchsia", font=("Arial", 12))
lblresult.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)

total = StringVar()

txtresult = Entry(ventanap, state="disabled", font=("Arial", 12), textvariable=total)
txtresult.pack(padx=5, pady=3, ipadx=10, ipady=10, fill=X)

# INICIAR LA APLICACIÓN (BUCLE PRINCIPAL)

ventanap.mainloop()