Cateto1 = float(input("Escribe el valor de uno de tus catetos"))
Cateto2 = float(input("Escribe el valor del otro cateto"))
Hipotenusa = (Cateto1**2+Cateto2**2)**(1/2)    

while Cateto1 <= 0 or  Cateto2 <= 0:
    print("ERROR, Los valores deben ser mayores a cero")
    Cateto1 = float(input("Escribe el valor de uno de tus catetos"))
    Cateto2 = float(input("Escribe el valor del otro cateto"))
print(Hipotenusa)