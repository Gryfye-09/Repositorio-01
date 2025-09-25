# Imprimir los numeros del 1 al 10
for i in range(1,11):
    print(i)

# Imprimir los numeros del 100 al 200
for x in range(100, 200, 2):
    print(x)

#Imprimir los numeros del 5 al 20 de tres en tres
for j in range(5, 21, 3):
    print(j)

#Requrir al usuario que ingrese un numero
#Entero positivo y luego imprimir todos los numeros
#Desde 1 hasta ese numero
num = int(input("Ingrese un numero entero positivo: "))
for k in range(1, num + 1):
    print(k)

#Escribir un programa que solicite al usuario una cantidad
#y luego itere la cantidad de veces dadas. En cada iteracion,
#solicitar al usuario que ingrese un numero. Al finalizar,
#mostrar la suma de todos los numeros ingresados.
cantidad = int(input("Ingrese la cantidad de numeros a sumar: "))
suma = 0
for i in range(cantidad):
    numero = int(input("Ingrese un numero"))
    suma += numero
print("La suma de los numeros ingresados es: ",suma)

#Solicitar al usuario que ingrese una frase y luego imprimir un
#listado de las vocales que aparecen en esa frase(sin reetirlas)
frase = input("Ingrese una frase")
for x in "aeiouAEIOU":
    if x in frase:
     print(x)

#Contar la cantidad de vocales en una frase ingresado por el usuario
frase2 = input("Ingrese una frase")
contador = 0
for l in frase2:
    if l in "aeiouAEIOU":
        cantidad += 1
    print("La cantidad de vocales en la frase es: ", cantidad)

#Ingresar un numero por pantalla y sumar los numeros desde 1 hasta el numero ingresado

num2 = int(input("Ingrese un numero:"))
suma2 = 0
for m in range(1, num2 + 1):
    suma2 += m
print("La suma desde 1 hasta", num2, "es:", suma2)

#Imprimir la tabla de multiplicar del 1 al 10
for n in range(1, 11):
    print("Tabla de multiplicar de", n)
    for p in range(1, 11):
        print(n, "x", p, "=", n * p)
    print()   #Linea en blanco para separar las tablas
  
