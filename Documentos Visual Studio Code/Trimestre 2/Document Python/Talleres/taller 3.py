## 1.

print("Ejercicio 1")

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel",
"Tomás", "Daniela"]

for nombre in alumnos_clase:
    print("Hola" , nombre)


## 2.
print("\nEjercicio 2")

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma = 0
for n in lista_numeros:
    suma = suma + n
    print("La suma de los numeros es: ", suma)


## 3.

print("\nEjercicio 3")

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

suma_pares = 0
suma_impares = 0

for n in lista_numeros:
    if  n % 2 == 0:
        suma_pares += n
    else:
        suma_impares += n

print("La suma de los numeros impares es: ", suma_impares, "La suma de los numeros pares es: ", suma_pares)


## 4.

print("\nEjercicio 4")

contador = 11

while contador >= 1:

    contador -= 1 

    print("El contador es", contador)


## 5.

print("\nEjercicio 5")

mi_lista= list(range(2500, 2586))
print(mi_lista)


## 6.
print("\nEjercicio 6")

lista_numeros = list(range(3, 301, 3))

## 7.

print("\nEjercicio 7")

suma_cuadrados = 0
for numeros in range (1,16):
    cuadrado = numeros ** 2
    suma_cuadrados += cuadrado
print(suma_cuadrados)

## 8. 

print("\nEjercicio 8")

print("usando enumerate para obtener indice y valor: ")
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier"]
for indice, nombre in enumerate(lista_nombres):
    print(f"{nombre}, esta en el indice:{indice}")


## 9.

print("\nEjercicio 9")

lista_indice = list(enumerate("python"))
print(lista_indice)


## 10.

print("\nEjercicio 10")

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier"]
for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(indice)