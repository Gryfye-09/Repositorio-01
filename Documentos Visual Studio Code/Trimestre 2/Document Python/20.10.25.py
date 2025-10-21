# Comprension de listas
## La comprension de listas es una forma rapida y compacta de crear listas en python usando una sola linea de codigo en lugar de escribir un bucle for tradicional, puedes generar una lista aplicando una expresion a cada elemento iterables como (lista, tupla o rango).

### forma tradicional de crear una lista a partir de un string ###
palabra = "python" # cadena base
lista_tradicional = [] # lista vacia
for letra in palabra: # bucle for para recorrer
    lista_tradicional.append(letra)
    # agregar letra a la lista
print("lista tradicional:", lista_tradicional)

# misma idea usando comprension de listas
palabra = "python"
lista_comprension = [letra for letra in palabra]
# toma cada caracter de palabra y la pone en una lista
print("lista comprension: " , lista_comprension)

# orea variante usando comprension de listas, el nombre de la variable interna puede ser diferente
lista1 = [caracter for caracter in "python"]
# recorre directamente el string "python"
print("otra lista por compresion: ",lista1)

# comprension con numeros:
# crear una lista de pares de 0 a 20
listanum = [n for n in range (0, 21, 2)]
print ("lista de numeros pares: ", listanum)

# convertir pies a metros
pies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
metros = [round(pie * 0.3048, 4) for pie in pies]
print("pies a metros: ", metros)

# conversion de temperaturas

# convertir grados a celcius a fahrenheit
celcius = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
fahrenheit = [round ((temp * 9/5) + 32, 2) for temp in celcius]
print("celcius a fahrenheit: ", fahrenheit)