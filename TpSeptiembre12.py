PIN_SECRETO = "1234"
INTENTOS_MAXIMOS = 3
intentos_realizados = 0

while intentos_realizados < INTENTOS_MAXIMOS:
    pin_ingresado = input("Introduce el PIN: ")
    if pin_ingresado == PIN_SECRETO:
        print("Login correcto")
        break  
    else:
        intentos_realizados += 1
        print(f"PIN incorrecto. Te quedan {INTENTOS_MAXIMOS - intentos_realizados} intentos.")
    if intentos_realizados == INTENTOS_MAXIMOS:
        print("Llamando al policía...")
