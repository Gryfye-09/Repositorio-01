print("Este programa mezcla dos colores.")
print("r. Rojo   a. Azul")
primera = input(" Elija un color (r o a):")
if primera == "r":
        print(" a. Azul   v. Verde")
        segunda = input(" Elija un color (a o v):")
        if segunda == "a":
            print("La mezcla Rojo y Azul produce magenta")
        else: print("La mezcla Rojo y Verde produce amarillo")
else: print("v. Verde   r. Rojo")
segunda = input("Elija otro color (v o r):")
if segunda == "v":
        print("La mezcla azul y verde produce cian.")
else: print("La mezcla azul y rojo produce magenta.")
print("¡Hasta la proxima!")

