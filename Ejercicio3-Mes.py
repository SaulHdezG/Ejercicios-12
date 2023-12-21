#¿Cuántos días tiene el mes mes?
#Algoritmo dias del mes

mes = input("Ingrese el mes")
if mes == "Febrero":
    print(mes,"tiene 28 dias")
elif mes == "Enero" or "Marzo" or "Mayo" or "Junio" or "Agosto" or "Octubre" or "Diciembre":
    print(mes,"tiene 31 dias")
else:
    print(mes,"tiene 30 dias")