edad = int(input("Decime tu edad y te digo si podes pasar"))
acompañado = str(input("Indica si esta acompañdo por un mayor de edad"))
if edad >= 18:
    if acompañado == "si":
        print("Podes pasar")
else:
    print("No podes pasar, andate")