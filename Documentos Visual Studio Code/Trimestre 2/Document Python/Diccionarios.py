listas = ["a", "b", "c", "d"] #lista
# diccionarios
dic = {"c1":1, "c2":2, "c3":3}
print (type(dic))
print(dic)
print(len(dic))
print(dic["c1"])

dic1 = {"c5":125,"c6":[10,20,30],"c7":{"a":1,"b":2}}
print(dic1["c6"][1])

dic2 = {"c5":125,"c6":[10,20,30],"c8":{"s1":100,"s2":200,"s3":300}}
print(dic2["c8"]["s2"])

diccionario = {"c1":"valor1", "c2":"valor2","c3":"valor3"}
print(diccionario.keys())
print(diccionario.values())
resultado = diccionario ["c1"]
print(resultado)
diccionario["c4"]="valor4"
print(diccionario)
print(diccionario.items())
diccionario["c2"]="nuevo_valor2"

datos= {"nombre":"juan", "edad":25, "ciudad":"manizales", "talla":1.75}


#accedemos al valor asociado a la clave del nombre
consulta = datos["nombre"]
print(consulta)
print(datos)


#modificamos un valor asociado a la clave edad

datos ["edad"] = 26
print (datos)

#agregamos una nueva clave y su valor asociado
datos["peso"] = 70
print(datos)

#eliminamos
del datos["ciudad"]
print(datos)

#verificamos si una clave existe en el diccionario
existe = "nombre" in datos 