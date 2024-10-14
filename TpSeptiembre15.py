#Se combina listas con bucles (la actividad 6 de bucles y actividad 1 de listas)

import random
VidaA= 100
VidaB=100
AtaqueA=25
AtaqueB=25

inicia = random.randrange(1,10,1) 
if inicia >=5:
    VidaB-= AtaqueA
    print(f"El jugador A ataco a B" "\n" f"a el jugador B le restan {VidaB}")
else :
    VidaA-=VidaB
    print(f"El jugador B ataco a A" "\n" f"a el jugador A le restan {VidaA}")


