#¿Cómo se llama el polígono que tiene n lados? Considera que n va de 5 a 10.
#Algoritmo Tipo de Poligono

#Algoritmo Billetes

nlados = input("Ingrese los lados del poligono")
if int(nlados) == 5:
    figura = "Pentagono"
elif int(nlados) == 6: 
    figura = "Hexagono"
elif int(nlados) == 7:
    figura = "Heptagono"
elif int(nlados) == 8:
    figura = "Octagono"
elif int(nlados) == 9:
    figura = "Nonagono"
elif int(nlados) == 10:
    figura = "Decagono"
else:
   figura = "Solo numeros del 5 al 10"
print(figura)
