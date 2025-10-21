# enumerate, zip, nim/max, random

# importar las funciones o modulos de random

from random import *

# recorremos los numero del 20 al 40 incluye al 20 y 40
print("numeros del 20 al 40: ")
for numero in range(20, 41):
    print (numero)


# crea una lista de numeros del 300 al 50 con paso 2
print("lista de numeros del 30 al 50 con paso 2: ")
lista_numeros = list(range(30, 51, 2)) # paso de 2
print(lista_numeros)


# enumerate: permite obtener el indice y el valor de cada elemento en una lista iterable

print("usando enumerate para obtener indice y valor: ")
lista = ["a","b","c","d"]
for indice, valor in enumerate(lista):
    print(f"indice: {indice}, valor:{valor}")

          
print("ejemplo dos enumerate: ")
lista1 = ["a", "b", "c", "d", "e"]
for item in enumerate(lista1):
    print(item)


# guardar en una tupla la lista con indice y valor
lista2 = ["x", "y", "z"]
tupla_enumerada = tuple(enumerate(lista2))
print("tupla con indice y valor: ", tupla_enumerada)


# usando zip para combinar dos listas, zip() combina varios iterables en tuplas
# NOTA: se detiene ciando la lista mas corta termina
lista_nombres = [ "Ana", "Luis", "Carlos"]
lista_edades = [25, 30, 22]
lista_ciudades = ["Madrid", "Barcelona", "Valencia"]

# emparejar las listas usando zip
combinado = list(zip(lista_nombres, lista_edades, lista_ciudades))
#recorrer cada tupla en la lista combinada
for nombre, edad, ciudad in combinado:
    print(f"Nombre: {nombre}, edad: {edad}, ciudad: {ciudad}")

# min() - max() devuleven el minimo y el maximo de un iterables o menor o mayor entre varios argumentos
menor = min(78, 56, 89, 23, 45)
mayor = max(78, 56, 89, 23, 45)
print(f"el menor es: {menor}")
print(f"el mayor es {mayor}")

#

lista = [12, 45, 7, 23, 89, 34]
print(max(lista)) # maximo en la lista
print(min(lista)) # minimo en la lista

#  min puede funcionar con cadenas; usa orden alfabetico

nombre = ["Ana", "Luis", "Carlos", "Beatriz"]
print("nombre menor alfabeticamente: ", min(nombre))
print("nombre mayor alfabeticamente: ", max(nombre))

#
#en cadenas, min() y max() usan el valor ASCII
cadena = "python"
print("caracter minimo en 'python':", min(cadena)) # 'h'
print("caracter maximo en 'python':", max(cadena)) # 'y'

#
nom = "alejandra"
print("caracter minimo en 'alejandra':", min(nom))
# 'a' letra mas pequeña
print("caracter maximo en 'alejandra':", max(nom))
# 'r' letra mas grande

# en diccionarios, min() y max() trabajan con las claves
diccionario = {'a': 5, 'b':2, 'c':8}
print("clave minima en diccionarios:", min(diccionario)) # 'a'
print("clave maxima en diccionarios:", max(diccionario)) # 'c'
print(min(diccionario.values())) # valor minimo: 2
print(max(diccionario.values())) # valor maximo: 8

#funciones de random

#randint(a,b) devuelve un numero entero aleatorio entre a y b inclusive
num_aleatorio = randint(1,100)
print("numero aleatorio entre 1 y 100:", num_aleatorio)


#uniform(a,b) devuelve un numero flotante - decimal aleatorio entre a y b
aleatorio_flotante = uniform(1.0, 10.0)
print("numero flotante aleatorio entre 1.0 y 10.0:", aleatorio_flotante)

# random() devuelve un numero flotante aleatorio entre 0.0 y 1.0
aleatorio_0_1 = random()
print("numero aleatorio entre 0.0 y 1,0", aleatorio_0_1)

#choice(iterable) selecciona un elemento aleatorio de un iterable
colores = ["rojo", "azul", "verde", "amarillo"]
color_seleccionado = choice(colores)
print("color seleccionado aleatoriamente:", color_seleccionado)

# shuffle(lista) mezcla los elemento de una lista
numeros = [1, 2, 3, 4, 5]
print("lista original de numeros:", numeros)
shuffle(numeros)
print("lista de numeros mezclada:",numeros)

