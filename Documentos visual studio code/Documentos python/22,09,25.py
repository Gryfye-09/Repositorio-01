#__________________________________________#
### EJEMPLO INDEX ###
#__________________________________________#


mi_text = "Esta es una prueba de index"
resultado = mi_text[8]
print(resultado)
## Muestra la U ##

mi_text = "Esta es una prueba de index"
resultado = mi_text.index ("i")
print(resultado)
## Index 22 ##

mi_text = "Esta es una prueba de index"
resultado = mi_text.index ("prueba")
print(resultado)
## Index 12 ##

mi_text = "Esta es una prueba de index"
resultado = mi_text.index ("a")
print(resultado)
## Index a ##

mi_text = "Esta es una prueba de index"
resultado = mi_text.index ("a", 5)
print(resultado)
## Segundo parametro el 5 = posicion inicial de busqueda ##

mi_text = "Esta es una prueba de index"
resultado = mi_text.rindex ("a")
print(resultado)
## Rindex busca desde la derecha (Ultima aparicion) ##



#______________________________________#
### EXTRAER POSICIONES ( SLICING ) ###
#______________________________________#



texto = "ABCDEFGHIJKLMÑOPQ"
fragmento = texto[:5]
print(fragmento)
## Desde el inicio hasta 5 ( exclusivo ): 0..4. ##

texto = "ABCDEFGHIJKLMÑOPQ"
fragmento = texto[2:10:2]
print(fragmento)
## Desde 2 hasta 10 (exclusivo),
## saltando de 2 en 2: 2, 4, 6, 8. ##

texto = "ABCDEFGHIJKLMÑOPQ"
fragmento = texto[::3]
print(fragmento)
## Desde el inicio hasta el final;
## de 3 en 3: 0, 3, 6, 9, 12.

texto = "ABCDEFGHIJKLMÑOPQ"
fragmento = texto[::-2]
print(fragmento)
## Paso negativo recorre al reves
## 2 2n 2: 12, 10, 8, 6, 4, 2, 0.

string = "python"
# Desde indice 0 hasta antes del 2
print(string[0:2])
# Desde inicio hasta antes del 4
print(string[:4])
# Desde indice 2 hasta el final
print(string[2:])
# De 2 en 2 (0,2,4)
print(string[::2])
# Al reves
print(string[::-1])


#_________________________________________________#
### STRING: El slicing en python es una tactica que permite extraer parte
#(subcadenas) de un texto, lista, tupla o cualquier secuencia, usando la notacion:
# secuencia[inicio:fin:paso]
#_________________________________________________#

#_________________________________________________#
### OPERADORES MATEMATICOS ###
#_________________________________________________#



# Concatenacion + p1 + p2 + ...........#
# print (p1, p2, p3, ....)#
# formato literal print (f"{x}" mas {y} {x + y})#

X= 10
Y= 7
X= 2

print(f"{x} mas {y} es igual a {x + y}")
print(f"{x} menos {y} es igual a {x-  y}")
print(f"{x} por {y} es igual a {x * y}")
print(f"{x} dividido {y} es igual a {x / y}")