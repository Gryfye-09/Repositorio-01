# # seleccion simple con match/case

# def evaluar_numero(numero):
#     match numero:
#         case 1:
#             return "El numero es uno."
#         case 2:
#             return "El numero es dos."
#         case 3:
#             return "El numero es tres."
#         case _:
#             return "El numero no es uno, dos ni tres."
    

# # ejemplo de uso

# resultado = evaluar_numero(2)
# print(resultado) #salida: el numero es dos

# # seleccion multiple con match/case

# opcion = int(input("Ingrese una opcion (1-4)"))
# match opcion:
#     case 1:
#         print("Opcion 1 seleccionada.")
#     case 2:
#         print("Opcion 2 seleccionada.")
#     case 3:
#         print("Opcion 3 seleccionada.")
#     case 4:
#         print("Opcion 4 seleccionada.")
#     case _:
#         print("Opcion no valida.")


# ###

# print("--- Calculadora ---")
# print("1. Suma")
# print("2. Resta")
# print("3. Multiplicacion")
# print("4. Division")


# operacion = int(input("Seleccione una operacion (1-4):"))
# num1 = float(input("Ingrese el primer numero: "))
# num2 = float(input("Ingrese el segundo numero: "))

# match operacion:
#     case 1:
#         print("Resultado: ", num1 + num2)
#     case 2:
#         print("Resultado: ", num1 - num2)
#     case 3:
#         print("Resultado: ", num1 * num2)
#     case 4:
#         if num2 != 0:
#             print("Resultado: ", num1 / num2)
#         else:
#             print("Error: Division por cero.")
#     case _:
#         print("Operacion no valida.")


# dia = int(input("Ingrese un numero del 1 al 7 para el dia de " \
# "la semana: "))
# match dia:
#     case 1:
#         print("Lunes")
#     case 2:
#         print("Martes")
#     case 3:
#         print("Miercoles")
#     case 4:
#         print("Jueves")
#     case 5:
#         print("Viernes")
#     case 6:
#         print("Sabado")
#     case 7:
#         print("Domingo")
#     case _:
#         print("Numero no valido para un dia de la semana.")



###
# Ingrese una nota entre 0 y 5
# 0 <= 0 reprobado
# 3 <= 4 aprobado
# 4 <= excelente
### 

# notas = float(input("Ingrese la nota: "))

# match notas:
#    case n if 0 <= n < 3:
#           print("Reprobado")
#  case n if 3 <= n < 4:
#         print("Aprobado")
#    case n if 4 <= n < 5:
#            print("Excelente")
#    case _:
#        print("No valido")

    
## 
# Ingesar numero de lados 3-6
# 3 triangulo
# 4 cuadrado
# 5 pentagono
# 6 hexagono
##

#lados = float(input("Ingrese un numero de lados 3-6: "))

#match lados:
#    case 3:
#        print("Es un Triangulo.")
#    case 4:
#        print("Es un Cuadrado.")
#    case 5:
#        print("Es un Pentagono.")
#    case 6:
#        print("Es un Hexagono.")
#    case _:
#        print("Opcion No Valida.")

###
# Ingresar comandos start - stop - pause - exit
# start = programa iniciado
# stop = programa detenido
# pause = programa en pausa
# exit = salir del programa
###

# comando = input("Ingrese el comando: ").lower()

# match comando:
#     case "start":
#         print("Programa iniciado")
#     case "Stop":
#         print("Programa detenido")
#     case "Pause":
#         print("Programa en pausa")
#     case "Exit":
#         print("Salir del programa")
#     case _ :
#         print("Comando no reconocido")


#### 
# semaforo
# a = rojo
# b = amarillo
# c = verde
# cuando se ingrese la a, el semaforo esta en rojo detenido
# cuando se ingrese la b, el semaforo esta en amarrillo precaucion
# cuando se ingrese la c, el semaforo esta en verde avanzar

####

print("A. Rojo")
print("B. Amarillo")
print("C. Verde")

semaforo = input("Ingrese el estado del semaforo: ").lower()


match semaforo:
    case "a":
        print("El semaforo esta en rojo detenido")
    case "b":
        print("El semaforo esta en amarrillo precaucion")
    case "c":
        print("El semaforo esta en verde avanzar")
    case _:
        print("Opcion No Valida")