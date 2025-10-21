# 1.
mi_dic = {"nombre":"karen", "apellido":"solis", "edad":"35","ocupacion":"periodista"}
print (type(mi_dic))
print(mi_dic)


# 2.
mi_dict={"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])

# 3.
mi_dic = {"nombre":"karen", "apellido":"solis", "edad":"35","ocupacion":"periodista"}
mi_dic["edad"]="36"
mi_dic["ocupacion"]="editora"
mi_dic["pais"]="colombia"
print(mi_dic)


# 4.
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(int(mi_tupla.count(1)))
print(int(mi_tupla.count(2)))
print(int(mi_tupla.count(3)))


# 5.
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = tuple(mi_tupla)
print(mi_lista)


# 6.
mi_tupla = (1, 2, 3, 4)
a, b, c, d = mi_tupla

print (a) 
print (b) 
print (c) 

print(len(mi_tupla))


# 7.
n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un numero: "))
n3 = int(input("Ingrese un numero: "))
n4 = int(input("Ingrese un numero: "))
n5 = int(input("Ingrese un numero: "))

lista = (n1,n2,n3,n4,n5)

print("con reverso")
for elemento in reversed(lista):
    print(elemento)