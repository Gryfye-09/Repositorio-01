## Calculadora suma, resta, multiplicacion, division ##


# Funcion Suma:

def suma(numeros):
    return sum(numeros)

# Funcion Resta:

def resta(numeros):
    resultado = numeros[0]
    for n in numeros[1:]:
        resultado = resultado - n
    return resultado

# Funcion Multiplicacion:

def multiplicar(numeros):
    resultado = 1
    for n in numeros:
        resultado = resultado * n
    return resultado

# Funcion Division:

def dividir(numeros):
    resultado = numeros[0]
    for n in numeros[1:]:
        if n == 0:
            return "No se puede dividir entre 0"
        resultado = resultado / n
    return resultado


# Calculadora, pedir al usuario numeros y operacion que desea realizar: 

print(" CALCULADORA ")

# El usuario ingresa la cantidad de numeros deseados:

entrada = input("A. Ingrese los numeros separados con espacios: ")
numeros = [float(i) for i in entrada.split()]

# El usuario ingresa la opcion depende de la operacion a elegir:

print("B. Seleccione la operacion que desea: ")
print(" 1. Sumar ")
print(" 2. Restar ")
print(" 3. Multiplicar ")
print(" 4. Dividir ")

opcion = input("C. Ingrese el numero de la operacion correspondiente: ")

# Resultados que aparecen dependiendo de la opcion que elige el usuario:

if opcion == "1":
    resultado = suma(numeros)
elif opcion == "2":
    resultado = resta(numeros)
elif opcion == "3":
    resultado = multiplicar(numeros)
elif opcion == "4":
    resultado = dividir(numeros)
else:
    resultado = "Opcion no valida"

# Resultado final:

print("D. El resultado de la operacion es: ", resultado)