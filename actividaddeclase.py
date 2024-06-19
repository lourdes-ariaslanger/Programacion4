bateria = 53
if bateria < 20:
    print ("Recargar")
elif bateria > 50:
    print("Optimo")
elif bateria > 20:
    print("Normal")
elif bateria > 80:
    print("Full")