# crear un programa analizador de texto donde solicite al usuario ingresar un texto cualquiera y también 3 letras a su elección. El código deberá de generar lo siguiente: 
# Cuantas veces aparece las letras que ingreso. (almacenar las letras en una lista yluego usar un método de string q permita contar cuantas veces aparece un substringen un string). Recomendar pasar a minúsculas.
# Cuantas palabras hay a lo largo de todo el texto (recordar el método string para transformarlo en una lista y luego función el largo de una lista.)
# Mostrar primera y última letra (recordar el index).
# Mostrar el texto en inverso.


texto = input("Ingrese un texto: ")
letras = []
texto = texto.lower()

letras.append (input("Ingrese una letra: "))
letras.append (input("Ingrese una letra: "))
letras.append (input("Ingrese una letra: "))

letra1 = texto.count(letras[0])
letra2 = texto.count(letras[1])
letra3 = texto.count(letras[2])

print(f"La letra {letras[0]} esta {letra1} veces , la letras {letras[1]} esta {letra2} veces, la letra {letras[2]} esta {letra3} veces.")

palabras = texto.split()
cantidad_palabras = len(palabras)
print("La cantidad de palabras es: ", cantidad_palabras)

primera_letra = texto[0]
ultima_letra = texto[-1]

print("la primera letra es: ", primera_letra)
print("la ultima letra es: ", ultima_letra)

texto_reverso = texto[::-1]
print("el texto al reves es: ", texto_reverso)