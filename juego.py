from modulos import modulos_menu as mod
from pokemones.pokemon import Pikachu, Charizard, Golem, Squirtle

mod.instrucciones()
print()
jugadores = 0
while jugadores <= 1:
    if jugadores == 0:
        jugador1 = input("Nombre de jugador 1: ")
        opcion = mod.menu1()
        pokemon1 = mod.seleccionar_personaje(opcion)
        print()
    elif jugadores == 1:
        jugador2 = input("Nombre de jugador 2: ")
        opcion = mod.menu1()
        pokemon2 = mod.seleccionar_personaje(opcion)
        print()
    jugadores += 1
turno = 0
salida = True
print("______________AH JUGAR!!!______________")
while salida == True:
    if turno == 0:
        print(f"Turno de: {jugador1}, Con: {pokemon1.nombre} Ataque: {pokemon1.ataque} Vida: {pokemon1.vida}")
        accion = mod.menu2()
        print()
        if accion == "1":
            pokemon1.atacar(pokemon2)
            salida = mod.verificar_vida(jugador1,pokemon2)
            if salida == False: break
            mod.estado_actual(pokemon1, jugador1, pokemon2, jugador2)
        elif accion == "2":
            pokemon1.curar()
            mod.estado_actual(pokemon1, jugador1, pokemon2, jugador2)
        elif accion == "3":
            print(f"\nGANADOR: {jugador2}!!!")
            salida = False
        turno = 1
    elif turno == 1:
        print(f"Turno de: {jugador2}, Con: {pokemon2.nombre} Ataque: {pokemon2.ataque} Vida: {pokemon2.vida}")
        accion = mod.menu2()
        if accion == "1":
            pokemon2.atacar(pokemon1)
            salida = mod.verificar_vida(jugador2, pokemon1)
            if salida == False: break
            mod.estado_actual(pokemon1, jugador1, pokemon2, jugador2)
        elif accion == "2":
            pokemon2.curar()
            mod.estado_actual(pokemon1, jugador1, pokemon2, jugador2)
        elif accion == "3":
            print(f"\nGANADOR: {jugador1}!!!")
            salida = False
        turno = 0

