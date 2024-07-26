import random                       #se importa libreria random
print("Juguemos cachipun!")
print("ingresa piedra, papel o tijera")
jugada = input()                    #input libre para el jugador

print(f'Tu jugaste {jugada}')

lista = ["piedra", "papel", "tijera"] #lista que contiene elementos válidos de juego

computador= random.choice(lista)    #asigna a la variable computador un elemento al azar de la lista

if jugada in lista:                 #compara el input del jugador y lo compara a los elementos de la lista como condición
    print(f'Computador eligió {computador}')
else:                               #si el input no se encuentra en la lista, el programa advierte al jugador
    print('Argumento inválido: Debe ser piedra, papel o tijera')

if jugada == computador:            #condiciones de victoria y derrota, partiendo por el empate que es la más simple
    print('Empate')
elif jugada=='piedra'and computador == 'tijera':
    print('Ganaste!!!')
elif jugada=='piedra'and computador == 'papel':
    print('Perdiste')
elif jugada=='tijera'and computador == 'papel':
    print('Ganaste!!!')
elif jugada=='tijera'and computador == 'piedra':
    print('Perdiste')
elif jugada=='papel'and computador == 'piedra':
    print('Ganaste!!!')
elif jugada=='papel'and computador == 'tijera':
    print('Perdiste')
    
#hay técnicas para mejorar tus posibilidades de ganar en el cachipun, pero son basadas en psicología y lenguaje corporal
#lamentablemente solo funcionan contra humanos