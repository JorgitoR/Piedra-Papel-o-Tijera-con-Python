import random
import math


def jugar():

    jugador = input("Elige una de las siguientes opciones: 'p' para piedra, 'h' para Hojay y 't' para tijeras ")
    jugador = jugador.lower()
    lista = ["p", "h", "t"]
    computador = random.choice(lista)

    if jugador == computador:
        return(0, jugador, computador)

    if is_ganador(jugador, computador):
        return(1, jugador, computador)

    return (-1, jugador, computador)


def is_ganador(jugador, oponente):
    #devolvemos true si el jugador gana
    #La condicion para ganar es la siguiente. p>t, h>p, t>h

    if (jugador == 'p' and oponente =='t') or (jugador =='h' and oponente=='p') and (jugador == 't' and oponente=='h'):
        return True
    return False


def el_mejor_jugador(n):
    #Vamos a jugar contra la computadora hasta que alguno de los dos gane mas
    #para ganar, tu tienes ceil(n/2) juegos (ie 2/3, 3/5, 4/7)

    jugador_ganador=0
    computador_ganador =0
    para_ganar = math.ceil(n/2)

    while jugador_ganador < para_ganar and computador_ganador < para_ganar:
        resultado, usuario, computador = jugar()
        #Empate
        if resultado == 0:
            print("Es un empate. Tu y el computador han elegido {}. \n".format(usuario))
        
        #Tu gans
        elif resultado == 1:
            jugador_ganador += 1
            print("Tu has elegido {} y el computador {}. Ganastes \n".format(usuario, computador))

        else:
            computador_ganador += 1
            print("Tu has elegido {} y el computador {}. Perdistes \n".format(usuario, computador))


    if jugador_ganador > computador_ganador:
        print("Haz ganado lo mejor de {} juegos. !Que campeon :D".format(n))
    else:
        print('Desafortunadamente, el computador ha hecho lo mejor de {} juegos. mejor suerte la proxima vex!:'.format(n))


if __name__ == "__main__":
    el_mejor_jugador(3)