## 1
palabra = "Ordenador"
resultado = palabra[4]
print(resultado)

## 2
frase = "En teoria, la teoria y la practica son los mismo. En la practica, no lo son."
resultado = frase.index ("practica")
print(resultado)

## 3
frase = "En teoria, la teoria y la practica son los mismo. En la practica, no lo son."
resultado = frase.rindex ("practica")
print(resultado)

## 4
texto = "Controlar la complejidad es la esencia de la programación"
fragmento = texto[:9]
print(fragmento)

## 5
texto = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
fragmento = texto[9::3]
print(fragmento)

## 6
texto = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
fragmento = texto[::-1]
print(fragmento)

## 7
x=874
y=27
div= 874//27
print(div)

## 8
mod=(456%33)
print(mod)

## 9 
raiz= 783**0.5
print(raiz)

## 10
division= (10/3)
print(round(division,2))

## 11
numero= 10.676767
print(round(numero))

## 12
r= 5**0.5
print(round(r,4))

## 13
nombre= input("Ingrese su nombre")
venta= int(input("Ingrese el valor de venta por mes"))
comision= venta*0.13
print("El valor de la comision es",comision)

## 14
frase="Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado= frase.upper()
print(resultado)

## 15
lista_palabras = ["La", "Legibilidad", "Cuenta"]
resultado = " ".join(lista_palabras)
print(resultado)

## 16
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
frase = frase.replace("dificil", "facil")
frase = frase.replace("mala", "buena")
print(frase)