frase = "Estoy tratando de programar"
print(frase)
contador = 0
for frase in frase.split():
    print(frase)
    contador += 1 
print(f"Total de palabras (FOR): {contador}\n")
