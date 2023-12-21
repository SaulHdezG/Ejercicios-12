#A partir de un peso (en kg) y una estatura (en m) dadas, el índice de masa
#corporal (IMC) se calcula como IMC = peso/estatura . Indicar si una
#persona tiene “peso bajo” (IMC menor que 18.5), “peso normal” (IMC entre
#18.5 y 25) o “sobrepeso” (IMC mayor que 25).

#Algoritmo IMC
peso = input("Ingrese su peso")
estatura = input("Ingrese su estatura")
IMC = int(peso) / float(estatura)**2
if IMC < 18.5:
    print("Tiene un peso bajo")
elif IMC > 18.5 and IMC < 25:
    print("Tiene un peso normal")
else:
    print("Tiene sobrepeso")
