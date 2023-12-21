#La siguiente tabla contiene rangos de magnitud de sismos en la escala de
#Richter y sus descriptores:
#Magnitud Descriptor
#Menos de 2.0 Micro
#De 2.0 a menos de 4.0 Menor
#De 4.0 a menos de 5.0 Ligero
#De 5.0 a menos de 6.0 Moderado
#De 6.0 a menos de 7.0 Fuerte
#De 7.0 a menos de 8.0 Mayor
#De 8.0 a menos de 10.0 Cataclismo
#Más de 10.0 Legendario
#Dada una magnitud mag, indicar el descriptor apropiado como parte de un
#mensaje significativo.

#Algortimo Sismo Magnitud

magnitud = input("Indique la magnitud del Sismo")
if float(magnitud) < 2:
    tiposismo = "Micro"
elif float(magnitud) >= 2 and float(magnitud) < 4:
    tiposismo = "Menor"
elif float(magnitud) >= 4 and float(magnitud) < 5:
    tiposismo = "Ligero"
elif float(magnitud) >= 5 and float(magnitud) < 6:
    tiposismo = "Moderado"
elif float(magnitud) >= 6 and float(magnitud) < 7:
    tiposismo = "Fuerte"
elif int(magnitud) >= 7 and float(magnitud) < 8:
    tiposismo = "Mayor"
elif float(magnitud) >= 8 and float(magnitud) < 10:
    tiposismo = "Cataclismo"
else:
    tiposismo = "Legendario"

print("El sismo de magnitud", magnitud, "es de tipo", tiposismo)