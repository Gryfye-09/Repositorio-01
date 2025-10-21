# Las tuplas son colecciones ordenadas e inmutables
# Es decir, una vez creadas no se pueden modificar
# (no se pueden agregar, eliminar o cambiar elementos)
# Se definen usando parentesis()
# Pueden contener elementos de diferentes tipos de datos
# Son utiles para almacenar datos que no deben cambiar
# Como coordenadas geograficas, fehcas, etc.
# Para proteger datos de modificaciones accidentales 
# Caracteristicas 
# Ocupan menos espacio en memoria que las listas 
# Son mas rapidas que las listas para ciertas operaciones
# Pueden tener diferentes tipos de datos 
# Se pueden anidar 

# ejemplo basico de una tupla 
mi_tupla = (1,2,3,4)
print (type(mi_tupla))
print(len(mi_tupla))

# Ejemplo de tupla con diferentes tipos de datos 

mi_tupla1 = (1, "hola", 3.14, True)
print(type(mi_tupla1))
print(mi_tupla1)
tupla = (1,2,3,4,5)

print(tupla[0])#acceder al primer elemnto
print(tupla[1:4])#acceder a la porcion de la tupla
print(tupla[-1])#acceder al ultimo elemento

#tuplas anidadas
tupla_anidada = (1,2,(3,4), (5,6))
print(tupla_anidada[2])#acceder a la tupla (3,4)

#intentar modificar una tupla genera un error
# tupla2 = (1,2,3)
# tupla2[0] = 10 #esto genera un error
# print(tupla2)

#operaciones con tuplas
tupla1 = (1,2,3)
tupla2 = (4,5,6)
tupla3 = tupla1 + tupla2 #concatenacion
print(tupla3)

print(tupla3)
print(tupla3.count (2)) #contar cuantas veces aparece el valor
print(tupla3.index(5)) #encontrar la posicion del valor 5

#desempaquetado de tuplas
tupla4 = (10,20,30)
a, b, c = tupla4

print (a) #10
print (b) #20
print (c) #30
print(len(tupla4))

#tuplas con un solo elemento
tupla5 = (100,) #como el final
print (type(tupla5)) #es una tupla
print (tupla5[0]) # 100

#sin la coma seria un entero

tupla6 = (100) # sin coma

#metodos de tuplas

t = (1,2,3,4,5,1) 
print(t.count(1))# cuantas veces aparece el 1
print(t.index(3)) # en que posicion esta el 3
print(len(t)) #longitud de la tupla
print(3 in t) # verificar si el 3 esta en la dupla


#iterar sobre la tupla

tupla7 = ("a", "b", "c")
for elemento in tupla7:
  print(elemento)


#repetir una tupla
tupla8 = (1,2)
tupla9 = tupla8 * 3
print(tupla9)

#convertir una lista en tupla
mi_lista = [1,2,3]
mi_tupla = tuple(mi_lista)
print(mi_tupla)

#comprobar si un elemento esta en la dupla
tupla10 = 10,20,30
if 30 in tupla10:
  print("30 esta en la tupla")

else:
  print("30 no esta en la tupla")

# crear una tupla con datos y mostrarlos formateados
persona = ("juan",25, "manizales")
print(f"nombre: {persona[0]}, edad: {persona[1]}, ciudad: {persona[2]}")