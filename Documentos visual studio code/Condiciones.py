print("Opciones del clima: 1.Soleado 2.Nublado 3.Lluvioso")
clima= input("Elige una opcion de clima ")

print("Opciones de hora: a.Mañana b.Tarde c.Noche")
hora= input("Elige una opcion de hora ")

print("Opciones de estado de animo: A.Activo B.Alegre")
estado_animo= input("Elige una de las opciones de estado de animo ")

if (clima == "1" or clima == "2") and hora == "a" and estado_animo == "A":
    print("Puedes hacer ejercicio")

elif clima == "3" and hora == "b" and estado_animo == "B":
    print("Puedes leer")

elif clima == "2" and hora == "c" and estado_animo == "A":
    print("Puedes escuchar música")

elif clima == "1" and hora == "b" and estado_animo == "B":
    print("Puedes salir con amigos")

elif clima == "2" and hora == "b" and estado_animo == "A":
    print("Puedes ver una película o una serie")

else:
    print("Puedes una actividad de tu preferencia")
