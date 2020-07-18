from modulos import modulos_menu as menu
from pokemones.golem import Golem
from pokemones.squirtle import Squirtle
from pokemones.pikachu import Pikachu
from pokemones.charizard import Charizad

menu.instrucciones()

#while 
jugadores = 0
jugador1 = None
jugador2 = None
while jugadores < 3:
    opcion = menu.menu1()
    if jugadores == 0:
        jugador1 = menu.seleccionar_personaje(opcion)
    elif jugadores == 1:
        jugador2 = menu.seleccionar_personaje(opcion)
    jugadores += 1
#combate = Combate(jugador1, jugador2)
