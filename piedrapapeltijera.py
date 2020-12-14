import random
import math

def jugar():

    usuario = input("Elige una opcion. 'p' para piedra, 'h' para hoja, 't' tijeras\n")
    usuario = usuario.lower()


    computador = random.choice(['p', 'h', 't'])

    if usuario == computador:
        return "Tu y el Computador han elegifo {}. Es un empate".format(computador)

    if is_ganador(usuario, computador):
        return "Tu haz elegido {} y el computador ha elegido {}. Tu Ganastes!".format(usuario, computador)

    return "Tu haz elegido {} y el computador ha elegido {}. Tu perdiste :(".format(usuario, computador)

def is_ganador(jugador, oponente):
    #devolvemos True si el jugador le gana al oponente
    #Condicion para ganar: p > t, t > h, h > p

    if(jugador == 'p' and oponente == 't') or (jugador == 't' and oponente=='h') or (jugador == 'h' and jugador=='p'):
        return True 
    return False

def play_best_of(n):
    #Jugar contra la computadora hasta  que alguno gane el mejor de n juegos
    #para ganr, debes ganar ceil(n/2) juegos (ie 2/3, 3/5, 4/7)

    jugador_gana =0
    computador_gana=0
    necesario_para_ganar = math.ceil(n/2)
    print(necesario_para_ganar)


if __name__ == "__main__":
    play_best_of(5)
    play_best_of(3)
    #print(jugar())