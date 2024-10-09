# Definir el PIN secreto
PIN_SECRETO = "1234"

# Número de intentos máximos
INTENTOS_MAXIMOS = 3

# Inicializar el número de intentos realizados
intentos_realizados = 0

# Bucle while para permitir hasta 3 intentos
while intentos_realizados < INTENTOS_MAXIMOS:
    # Pedir al usuario que introduzca el PIN
    pin_ingresado = input("Introduce el PIN: ")
    
    # Comprobar si el PIN ingresado es correcto
    if pin_ingresado == PIN_SECRETO:
        print("Login correcto")
        break  # Salir del bucle si el PIN es correcto
    else:
        intentos_realizados += 1
        print(f"PIN incorrecto. Te quedan {INTENTOS_MAXIMOS - intentos_realizados} intentos.")
        
    # Si se alcanzan los intentos máximos
    if intentos_realizados == INTENTOS_MAXIMOS:
        print("Llamando al policía...")
