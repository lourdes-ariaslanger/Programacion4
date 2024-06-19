want_greet = "S"
valid_options = 0

while want_greet  == "S" :
    print("Hola que tal!")
    want_greet = input ("¿Quiere otro saludo?")
    if want_greet not in "SN" : 
        print("No le he entendido pero lo saludo igual")
        want_greet = "S"
        continue
    valid_options += 1
    print(f"{valid_options} respuestas validas")
    print("Que tenga un buen día")
