tarifa = float(input("Ingresa el valor de la tarifa de este año"))
edad = int(input('Ingresa tu edad: '))
trabaja = str(input('Ingresa si trabaja o no [s/n]')) 

if edad >= 18 and trabaja == "s":
    print(tarifa) 
    print("Paga el 100%")
elif edad >= 18 and trabaja == "n":
    print(tarifa*0.75) 
    print("Paga el 75%")
elif edad < 18 and trabaja == "n":
    print(tarifa*0.50) 
    print("Paga el 50%")