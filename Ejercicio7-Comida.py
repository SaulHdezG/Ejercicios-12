#Doña Lore tiene una cocina económica que vende comidas de tres tiempos.
#En el primer tiempo ofrece sopa de lentejas a $20, crema de elote a $25 y
#sopa de fideos a $15. En el segundo tiempo tiene arroz a $15, espagueti a
#$20 y ensalada a $10. En el tercer tiempo tiene pollo con papas a $35, bistec
#en morita a $45 y chile relleno a $30. ¿Cuánto tiene que pagar un comensal
#que elige una opción de cada tiempo?

#Algoritmo Comida 

comidaT1 = input("Comida del primer tiempo")
comidaT2 = input("Comida del segundo tiempo")
comidaT3 = input("Comida del tercer tiempo")

if comidaT1 == "sopa de lentejas":
    precioT1 = 20
elif comidaT1 == "crema de elote":
    precioT1 = 25
else:
    precioT1 = 15
if comidaT2 == "arroz":
    precioT2 = 15
elif comidaT2 == "espagueti":
    precioT2 = 20
else:
    precioT2 = 10
if comidaT3 == "pollo con papas":
    precioT3 = 35
elif comidaT3 == "bistec en morita":
    precioT3 = 45
else:
    precioT3 = 30

precioTotal = int(precioT1) + int(precioT2) + int(precioT3)
print("El precio total es:", precioTotal)