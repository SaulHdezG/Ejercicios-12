#Dado un billete de $x, ¿cuáles son los personajes o hechos históricos que
#aparecen en su anverso?
#Algoritmo Billete
billete = input("Ingrese la denominacion del billete")
if int(billete) == 20:
    print("Aparece el Bicentenario de Independencia")
elif int(billete) == 50:
    print("Aparece un Ajolote")
elif int(billete) == 100:
    print("Aparece Sor Juana Ines de la Cruz")
elif int(billete) == 200:
    print("Aparece Miguel Hidalgo y Mario Morelos")
elif int(billete) == 500:
    print("Aparece Benito Juarez")
elif int(billete) == 1000:
    print("Aparece Francisco I. Madero")
else:
    print("Solo billetes existentes")
