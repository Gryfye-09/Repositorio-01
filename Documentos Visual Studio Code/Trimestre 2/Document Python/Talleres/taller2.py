# 1.

valores = [5,8,9,12,36,9.5]
valores_cuadrado = [n ** 2 for n in valores]
print("los valores elevado al cuadrado son: ", valores_cuadrado)

# 2.

valores = [5,8,9,12,36,9.5,10]
valores_pares = [n for n in valores if n % 2 == 0]
print("Los valores pares son: ", valores_pares)

# 3.

temperatura_fahrenheit = [32, 212, 275]
grados_celcius = [((f-32)*(5/9)) for f in temperatura_fahrenheit]
print("La temperatura en celcius es: ", grados_celcius)

# 4.

set_1 = {1, 2, "tres", "cuatro"}
set_2 = {"tres", 4, 5}
mi_set_3 = set_1.union(set_2)
print("La union de los dos set es: ",mi_set_3)

# 5. 

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
eliminado = sorteo.pop()
print("El set ahora es: ",sorteo)
print("El que se elimino al azar es: ", eliminado)

# 6.

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damian")
print("El set ahora es: ",sorteo)

# 7. 

prueba = 10>1 and 5<15
print(prueba)

# 8. 

prueba2 = (17834/34) > (87*56)
print(prueba2)

# 9.

prueba3 = (25 ** 0.5) == 5
print(prueba3)

# 10.

# Palabra[4]

palabra = "exito"
resultado = palabra[4]
print(resultado)

# 11.

# Incorrecto

# 12. 

# Listas