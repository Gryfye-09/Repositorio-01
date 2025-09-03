# Instrucciones: 
    # 1. Variables Iniciales: 
        # a. Cuenta: Establece un valor fijo para el total de la cuenta (puede ser un número entero o decimal). 
        # b. Propina: Establece el porcentaje de propina que se desea dejar. 

    # 2. Operaciones: 
        # a. Calcula la propina multiplicando el total de la cuenta por el porcentaje de propina dividido entre 100. 
        # b. Calcula el total a pagar sumando la propina al total de la cuenta. 

    # 3. Mostrar los Resultados: 
        # a. Muestra al usuario: 
        # i. El total de la cuenta. 
        # ii. El porcentaje de propina. 
        # iii. La propina calculada. 
        # iv. El total a pagar.

# Consejos para Realizar el Proyecto: 
    # • Formato de Salida: 
        # No es necesario usar round() ya que los números son enteros. Aún así, puedes optar por hacerlo si deseas mostrar
        # más detalles en el resultado. 

# ==> ESCRIBE TU SOLUCION AQUÍ DEBAJO :)

cuenta = 65.000
propina = 10 
propina_calculada = (cuenta*10)/100
total_pagar = (propina_calculada+cuenta)

print(f"El total de la cuenta es de: {cuenta}")
print(f"El porcentaje de la propina es de: {propina} %")
print(f"La propina calculada es de: {propina_calculada}")
print(f"El total a pagar es de: {total_pagar}")  