#¿Cómo se llama el polígono que tiene n lados? Considera que n va de 5 a 10.
#Algoritmo Tipo de Poligono

nlados = input("Ingrese los lados del poligono")
if nlados == 5:
    poligono = "pentagono"
#elif nlados == 6:
#    poligono = "hexagono"
#elif nlados == 7:
#    poligono = "heptagono"
#elif nlados == 8:
#    poligono = "octagono"
#elif nlados == 9:
#    poligono = "nonagono"
#elif nlados == 10:
#    poligono = "decagono"
#else:
#    print("Favor de ingresar solo del numero 5 al 10")

print("El poligono de", nlados, "lados es un", poligono)