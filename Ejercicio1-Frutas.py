# Una frutería vende manzanas a $45 el kilo, peras a $40 el kilo y naranjas a
#25 el kilo. Si un cliente compra n kilos de alguna de las frutas, ¿cuánto tiene
#que pagar?

#Algoritmo_tipo_fruta
tipodefruta =  input("Ingresa el tipo de fruta")
nkilos = input("Ingresa los kilos comprados")
if tipodefruta == "manzana":
    precio = int(nkilos) * 45
elif tipodefruta == "peras":
    precio = int(nkilos) * 40
else:
    precio = int(nkilos) * 25

print("Por", nkilos, "kilos de", tipodefruta, "se paga", precio)

