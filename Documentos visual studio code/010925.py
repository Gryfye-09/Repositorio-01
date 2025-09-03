##### BUCLES #####

#Contador
contador = 1
nombre = "Juan"

while contador <= 10:  #Se ejecuta 10 veces
    print("El nombre en el ciclo es " + nombre)  #Muestra el nombre
    contador +=1  #Incrementa el contador

#For
for i in range(5): # 5 iteraciones
    print("El nombre en el ciclo es " + nombre)
    #Muestra el nombre


#While
contador1 = 0
while contador1 < 5: #Se ejecuta 5 veces
    print("El contador es", contador1) #Muestra el contador
    contador =+ 1 

#For
for n in range (1,8):
    print("El contador es", n) #Muestra el contador


#For input
nombre2= input ("Ingrese su nombre")
numero2= int (input("Ingrese un numero para repetir el nombre"))
for i in range (numero2):
    print ("El nombre en el ciclo es " + nombre2)
    #Muestra el nombre

#While
nombre3= input("Ingrese su nombre")
numero3= int (input("Ingrese un numero para repetir el nombre"))
contador2= 0
while contador2 < numero3:
    print("El nombre en el ciclo es " + nombre3)
    contador += 1


#Variable

mi_variable = 5 == 100
variable = "Hola mundo"

print(mi_variable)
print(variable)

variable1 = 5*5 == 18 - 8 

###

variable2 = "Blanco" == "blanco".lower
print(variable2)

###