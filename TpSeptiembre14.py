#calculadora que calcula hasta que se le indique se se apaga

while True:
    valor1 = float(input("Escribe un valor"))
    valor2= float(input("Escribe otro valor"))
    Operacion = int(input("Escribe la función que desees. 1: Calcula la raiz cuadrada de los valores 2: Divide ambos valores 3: Multiplica los valores y luego los divide por 2.5 4: Sale"))
    if Operacion == 1:
        print((valor1+valor2)*0.5)
      
    elif Operacion == 2:
        print(valor1/valor2)
    elif Operacion == 3:
        print((valor1*valor2)/2,5)
    elif Operacion == 4:
        break
        